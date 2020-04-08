<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="5" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">{{ description }}</b>
        <DegreeCircle v-show="useInput && playing" class="ma-1"
                      :submit-solution="solutionInput" :solution="solution" :enabled-degrees="chosenDegrees">
            <template v-slot:playbtn>
                <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
                    <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
                </v-btn>
            </template>
            <template v-slot:progress>
                <v-progress-circular class="my-progress-circular text-center" :value="progress"
                                     :color="loaded ? 'primary': 'red'" size="90" />
            </template>
            <template v-slot:text>
                {{ roundSincePlay }}
            </template>
        </DegreeCircle>
        <div v-show="!(useInput && playing)">
            <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
                <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
            </v-btn>
            <v-progress-circular class="my-progress-circular ma-1 text-center" :value="progress"
                                 :color="loaded ? 'primary': 'red'" size="50">
                <DegreeCirclePictogram :enabled-degrees="chosenDegrees">
                    {{roundSincePlay}}
                </DegreeCirclePictogram>
            </v-progress-circular>
        </div>
    </v-card>
</template>

<script>
    /* global MIDI */
    import { Midi, Scale } from "@tonaljs/tonal"
    import Vue from "vue";
    import DegreeCircle from "./DegreeCircle";
    import DegreeCirclePictogram from "./DegreeCirclePictogram";

    const INTERNALIZATION = 0;
    const INTERNALIZATION_TEST = 1;
    const RECOGNITION_SINGLE = 2;
    const RECOGNITION_SINGLE_TEST = 3;

    const CADENCE_MAJOR_I_IV_V = 'major_i_iv_v';
    const CADENCE_MAJOR_I_IV_V_I = 'major_i_iv_v_i';

    export default {
        name: "Teacher",
        components: {DegreeCirclePictogram, DegreeCircle},
        data: function() {
            return {
                playing: false,
                status: 'Not loaded',
                loaded: false,
                tempoBPM: 130,
                key: "",
                changeKeyEvery: 1, // set to -1 to never change key
                timeoutRef: null,
                progressRef: null,
                progress: 0,
                roundDuration: 0,
                startTime: 0,
                roundSincePlay: 0,
                stopAfterRounds: 12, // set to -1 to play endlessly
                degreeName: {
                    0: 'Do',
                    1: 'Di/Ra',
                    2: 'Re',
                    3: 'Ri/Me',
                    4: 'Mi',
                    5: 'Fa',
                    6: 'Fi/Se',
                    7: 'So',
                    8: 'Si/Le',
                    9: 'La',
                    10: 'Li/Te',
                    11: 'Ti'
                },
                chosenDegrees: [0, 2, 4, 5, 7, 9, 11],
                played: [],
                cadences: {
                    'major_i_iv_v': [
                        {
                            progression: [[-12, 0, 4, 7], [-7, -3, 0, 5], [-5, -1, 2, 7]],
                            chordLength: [4, 2, 2],
                            resting: [-12, 0, 4, 7]
                        },
                        {
                            progression: [[-12, 4, 7, 12], [-7, 0, 5, 9], [-5, 2, 7, 11]],
                            chordLength: [4, 2, 2],
                            resting: [-12, 4, 7, 12]
                        },
                        {
                            progression: [[-12, -5, 0, 4], [-19, -3, 0, 5], [-17, -5, -1, 2]],
                            chordLength: [4, 2, 2],
                            resting: [-12, -5, 0, 4]
                        },
                    ],
                    'major_i_iv_v_i': [
                        {
                            progression: [[-12, 0, 4, 7], [-7, -3, 0, 5], [-5, -1, 2, 7],[-12, 0, 4, 7]],
                            chordLength: [4, 2, 2, 4],
                            resting: [-12, 0, 4, 7]
                        },
                        {
                            progression: [[-12, 4, 7, 12], [-7, 0, 5, 9], [-5, 2, 7, 11],[-12, 4, 7, 12]],
                            chordLength: [4, 2, 2, 4],
                            resting: [-12, 4, 7, 12]
                        },
                        {
                            progression: [[-12, -5, 0, 4], [-19, -3, 0, 5], [-17, -5, -1, 2],[-12, -5, 0, 4]],
                            chordLength: [4, 2, 2, 4],
                            resting: [-12, -5, 0, 4]
                        },
                    ]
                },
                cadenceType: CADENCE_MAJOR_I_IV_V,
                type: INTERNALIZATION,
                description: "Internalisation",
                fixed: true,
                // tType specific
                // Recognition
                inputDisabled: false,
                fullCadenceEvery: 8,
                solution: 0,
                answer: "",
            };
        },
        computed: {
            quarter: function () { return 60 / this.tempoBPM },
            degrees: function () {
                if (this.chosenDegrees.length === 0) {
                    return [0];
                }
                return this.chosenDegrees;
            },
            multiple: function() {
                if (this.type === INTERNALIZATION) return false;
                else if (this.type === INTERNALIZATION_TEST) return false;
                else if (this.type === RECOGNITION_SINGLE) return true;
                else if (this.type === RECOGNITION_SINGLE_TEST) return true;
                else return false;
            },
            useInput: function() {
                if (this.inputDisabled) return false;

                if (this.type === INTERNALIZATION) return false;
                else if (this.type === INTERNALIZATION_TEST) return false;
                else if (this.type === RECOGNITION_SINGLE) return true;
                else if (this.type === RECOGNITION_SINGLE_TEST) return true;
                else return false;
            }
        },
        watch: {
            playing: function (val) {
                if (val) {
                    this.doStart();
                } else {
                    this.doStop();
                }
            }
        },
        methods: {
            playCadence: function (key, cadenceType, posOff) {
                /* play *cadenceType* in *key* */
                const cadence = this.cadences[cadenceType][Math.floor(
                    Math.random()*this.cadences[cadenceType].length)]; // select cadence randomly
                for (let chordNum=0; chordNum < cadence.progression.length; chordNum++) {
                    // play transposed cadence
                    const velocity = 127; // how hard the note hits
                    const notes = this.transposeToKey(cadence.progression[chordNum], key, 4);
                    // play the notes
                    MIDI.setVolume(0, 127);
                    if(this.playing){
                      this.chordOn(0, notes, velocity, posOff);
                      this.chordOff(0, notes, posOff + this.quarter * cadence.chordLength[chordNum]);
                    }
                    posOff = posOff + this.quarter * cadence.chordLength[chordNum];
                }
                // return duration, cadence for cadence.resting chord
                return [posOff, cadence];
            },
            playResting: function (key, cadence, posOff, duration) {
                /* Playing the transposed resting chord only */
                let delay = posOff;
                const velocity = 110; // how hard the note hits
                // play the notes
                const notes = this.transposeToKey(cadence.resting, key, 4);
                MIDI.setVolume(0, 127);
                if(this.playing){
                    this.chordOn(0, notes, velocity, delay);
                    this.chordOff(0, notes, delay + duration * this.quarter);
                }
                return delay + duration * this.quarter;
            },
            playDrone: function (key, posOff, duration) {
                const velocity = 110;
                const notes = this.transposeToKey([0, 7], key, 3);
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    this.chordOn(0, notes, velocity, posOff);
                    this.chordOff(0, notes, posOff + duration * this.quarter);
                }
                return posOff + duration * this.quarter;
            },
            playDegree: function (key, degree, withResting, posOff, duration, cadence) {
                /* play degree, optionally with resting chord */
                const root = key + '3';
                const note =  Midi.toMidi(root) + degree;
                if (withResting) {
                    this.playResting(key, cadence, posOff, duration);
                }
                const delay = posOff;
                const velocity = 127; // how hard the note hits
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    for (let i=0; i<3; i++) {
                        this.noteOn(0, note + i * 12, velocity, delay);
                        this.noteOff(0, note + i * 12, delay + this.quarter * 4);
                    }
                }
                return delay + this.quarter * 4;
            },
            transposeToKey: function (notes, key, octaves) {
                const keyOffset = Midi.toMidi(key + '0') + 12 * octaves;
                let notesMod = notes.slice();
                for (let i=0; i<notes.length; i++) {
                    notesMod[i] = notesMod[i] + keyOffset;
                }
                return notesMod;
            },
            playRound: function() {
                this.roundSincePlay++;
                // update key
                const chrom = Scale.get("C chromatic").notes; // get list of all twelve notes
                if (this.key === "" ||
                    (0 < this.changeKeyEvery &&
                        (this.roundSincePlay - 1) % this.changeKeyEvery === 0)) {
                    // new random key
                    this.sinceKeyChange = 0;
                    this.key = chrom[Math.floor(Math.random() * chrom.length)];
                }
                if (this.type === INTERNALIZATION) {
                    let [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V, 0);
                    for (let i=0;i<4;i++) {
                        posOff = this.playDegree(this.key, this.degrees[0], true, posOff, 4, cadence);
                        posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 4, cadence);
                    }
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                }
                else if (this.type === INTERNALIZATION_TEST) {
                    let [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V, 0);
                    posOff = this.playResting(this.key, cadence, posOff, 4);
                    posOff = this.rest(posOff, 3 * 4);
                    posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 8, cadence);
                    posOff = this.rest(posOff, 4);
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                }
                else if (this.type === RECOGNITION_SINGLE || this.type === RECOGNITION_SINGLE_TEST) {
                    const degree = this.degrees[Math.floor(Math.random()*this.degrees.length)];     // choose randomly
                    let posOff = 0;
                    let cadence = undefined;
                    if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                        [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V_I, 0);
                    } else {
                        posOff = this.playDrone(this.key, 0, 4);
                    }
                    posOff = this.playDegree(this.key, degree, false, posOff, 4, cadence);

                    this.solution = degree;
                    if (this.useInput) {
                        console.log("USE_INPUT");
                        this.roundDuration = posOff;
                    } else {
                        posOff = this.rest(posOff, 2 * 4);
                        this.roundDuration = posOff;
                        this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                    }
                }


                this.startTime = new Date().getTime();
                this.updateProgress();
            },
            solutionNoInput: function() {
                console.log("SOLUTION_NO_INPUT: ",this.solution);
                let posOff = this.rest(0,  4);
                this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
            },
            solutionInput: function(input) {
                if (this.solution === null) {
                    return;
                }
                let correct;
                console.log("SOLUTION_INPUT: ",input,this.solution,this.solution === input);
                if (this.solution === input) {
                    correct = true;
                    this.answer = "Correct: " + this.degreeName[this.solution];
                } else {
                    correct = false;
                    this.answer = "Wrong! It was " + this.degreeName[this.solution];
                }
                let posOff = this.rest(0, 4);
                this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
                return [correct, this.solution];
            },
            doRepeat: function() {
                this.stopAllNotes();
                this.clearTimeouts();
                if ( 0 < this.stopAfterRounds && this.stopAfterRounds <= this.roundSincePlay) {
                    this.playing = false;
                }
                if (this.playing) this.playRound();
            },
            // setup functions for different practice/test scenarios
            setupInternalization: function(degree, autoplay) {
                console.log("setupInternalization", degree);
                this.description = "Internalisation";
                this.chosenDegrees = [degree];
                this.type = INTERNALIZATION;
                this.stopAfterRounds = -1;
                this.finishSetup(autoplay);
            },
            setupInternalizationTest: function(degree, autoplay) {
                console.log("setupInternalizationTest", degree);
                this.description = "Internalisation Test";
                this.chosenDegrees = [degree];
                this.type = INTERNALIZATION_TEST;
                this.stopAfterRounds = 12;
                this.finishSetup(autoplay);
            },
            setupRecognitionSingle: function(degrees, autoplay, level) {
                console.log("setupRecognitionSingle", degrees);
                this.description = "Recognition";
                this.chosenDegrees = degrees;
                this.type = RECOGNITION_SINGLE;
                this.stopAfterRounds = -1;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = 100;
                else if (level === 2) this.tempoBPM = 135;
                else if (level === 3) this.tempoBPM = 180;
                this.finishSetup(autoplay);
            },
            setupRecognitionSingleTest: function(degrees, autoplay, level) {
                console.log("setupRecognitionSingleTest", degrees);
                this.description = "Recognition Test";
                this.chosenDegrees = degrees;
                this.type = RECOGNITION_SINGLE_TEST;
                this.stopAfterRounds = 32;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = 100;
                else if (level === 2) this.tempoBPM = 135;
                else if (level === 3) this.tempoBPM = 180;
                this.finishSetup(autoplay);
            },
            finishSetup: function (autoplay) {
                if (autoplay || this.playing) {
                    if (this.playing) {
                        this.restart();
                    } else {
                        this.playing = true;
                    }
                }
            },
            updateProgress: function () {
                if (this.playing) {
                    const passed = new Date().getTime() - this.startTime;
                    this.progress = passed / this.roundDuration / 10;
                    if (this.progress < 100) {
                        this.progressRef = setTimeout(this.updateProgress, 100);
                    }
                } else {
                    this.progress = 0;
                }
            },
            restart: function () {
                this.doStop();
                this.doStart();
            },
            doStart: function () {
                this.roundSincePlay = 0;
                this.playRound();
            },
            doStop: function () {
                this.clearTimeouts();
                this.progress = 0;
                this.stopAllNotes();
            },
            stopAllNotes: function () {
                for (let i=0; i<this.played.length;i++) {
                    let source = this.played[i];
                    if (source !== undefined && source) {
                        source.stop();
                    }
                }
                this.played = [];
                try {
                    MIDI.stopAllNotes();
                } catch (e) {
                    console.log('MIDI.stopAllNotes failed:', e);
                }
            },
            noteOn: function(channel, note, velocity, delay) {
                MIDI.noteOn(channel, note, velocity, delay);
            },
            noteOff: function (channel, note, delay) {
                this.played.push(MIDI.noteOff(channel, note, delay));
            },
            chordOn: function (channel, chord, velocity, delay) {
                MIDI.chordOn(channel, chord, velocity, delay);
            },
            chordOff: function (channel, chord, delay) {
                this.played.push(...Object.values(MIDI.chordOff(channel, chord, delay)));
            },
            rest: function (posOff, duration) {
                return posOff + duration * this.quarter;
            },
            clearTimeouts: function () {
                clearTimeout(this.timeoutRef);
                clearTimeout(this.progressRef);
            }
        },
        created: function initAudio() {
            if (this.$teacher !== undefined) {
                this.$teacher.playing = false;
            }
            Vue.prototype.$teacher = this;
            var self = this;
            MIDI.loadPlugin({
                soundfontUrl: "https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/",
                instrument: "acoustic_grand_piano",
                onprogress: function (state, progress) {
                    self.status = "Loading..." + Math.floor(progress * 100) + "%";
                    console.log(state, progress);
                    self.progress = progress * 100;
                },
                onsuccess: function () {
                    self.status = "Loaded";
                    self.progress = 0;
                    self.loaded = true;
                    self.setupInternalization(0, false);
                }
            });
        },
        destroyed: function stopAudio() {
            this.clearTimeouts();
            this.stopAllNotes();
        }
    };

</script>

<style lang="sass">
    .my-progress-circular .v-progress-circular__overlay
        transition: all 0.1s ease-in-out
</style>