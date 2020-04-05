<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="5" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">Play I-IV-V-I:</b>
        <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
            <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
        </v-btn>
            <v-select v-if="multiple" class="mx-1"
                      :readonly="fixed"
                      :items="degreesAvailable"
                      v-model="chosenDegrees"
                      label="Degree"
                      single-line
                      style="max-width: 150px;"
                      dense
                      multiple
                      chips
            />

            <v-select v-else class="mx-1"
                  :readonly="fixed"
                  :items="degreesAvailable"
                  v-model="chosenDegrees[0]"
                  label="Degree"
                  single-line
                  style="max-width: 150px;"
                  dense
            />
        <v-progress-circular class="my-progress-circular ml-2 text-center" :value="progress"
                             :color="loaded ? 'primary': 'red'">{{roundSincePlay}}</v-progress-circular>
        <BasicInput v-show="useInput" :submit-solution="solutionInput" :answer="answer"/>
    </v-card>
</template>

<script>
    /* global MIDI */
    import { Note, Midi, Scale } from "@tonaljs/tonal"
    import BasicInput from "./BasicInput";

    const INTERNALIZATION = 0;
    const INTERNALIZATION_TEST = 1;
    const RECOGNITION = 2;

    const CADENCE_MAJOR_I_IV_V = 'major_i_iv_v';
    const CADENCE_MAJOR_I_IV_V_I = 'major_i_iv_v_i';

    export default {
        name: "Teacher",
        components: {BasicInput},
        props: {
            preselect: Array, // which degrees to select on load || <Teacher ... :preselect="['1P', '5P']"/>
            fixed: Boolean, // fix values of preselect || <Teacher .. :preselect="['1P', '5P']" fixed/>
            tType: String,
        },
        data: function() {
            return {
                playing: false,
                status: 'Not loaded',
                loaded: false,
                tempoBPM: 130,
                key: "",
                sinceKeyChange: 0,
                changeKeyEvery: 1,
                timeoutRef: null,
                progressRef: null,
                progress: 0,
                roundDuration: 0,
                startTime: 0,
                roundSincePlay: 0,
                degreesAvailable: [
                    {text: 'Tonic', value: '1P'},
                    {text: '2nd', value: '2M'},
                    {text: 'Maj 3rd', value: '3M'},
                    {text: '4th', value: '4P'},
                    {text: '5th', value: '5P'},
                    {text: 'Maj 6th', value: '6M'},
                    {text: 'Maj 7th', value: '7M'},
                ],
                chosenDegrees: ["1P", "2M", "3M", "4P", "5P", "6M", "7M"],
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
                // tType specific
                // Recognition
                inputDisabled: false,
                solution: null,
                answer: "",
            };
        },
        computed: {
            quarter: function () { return 60 / this.tempoBPM },
            degrees: function () {
                if (this.chosenDegrees.length === 0) {
                    return ['1P'];
                }
                return this.chosenDegrees;
            },
            multiple: function() {
                if (this.type === INTERNALIZATION) return false;
                else if (this.type === INTERNALIZATION_TEST) return false;
                else if (this.type === RECOGNITION) return true;
                else return false;
            },
            useInput: function() {
                if (this.inputDisabled) return false;

                if (this.type === INTERNALIZATION) return false;
                else if (this.type === INTERNALIZATION_TEST) return false;
                else if (this.type === RECOGNITION) return true;
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
            playDegree: function (key, degree, withResting, posOff, duration, cadence) {
                /* play degree, optionally with resting chord */
                const root = key + '3';
                const note =  Midi.toMidi(Note.transpose(root, degree));
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
                if (this.key === "" || (++this.sinceKeyChange % this.changeKeyEvery) === 0) {
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
                else if (this.type === RECOGNITION) {
                    const degree = this.degrees[Math.floor(Math.random()*this.degrees.length)];     // choose randomly
                    let [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V_I, 0);
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
                console.log("SOLUTION_INPUT: ",input,this.solution,this.solution === input);
                if (this.solution === input) {
                    this.answer = "Correct: " + this.solution;
                } else {
                    this.answer = "Wrong! It was " + this.solution;
                }
                let posOff = this.rest(0, 4);
                this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
            },
            doRepeat: function() {
                this.stopAllNotes();
                this.clearTimeouts();
                if (this.playing) this.playRound();
            },
            // setup functions for different practice/test scenarios
            setupInternalization: function(degree) {
                console.log("setupInternalization", degree);
                this.chosenDegrees = [degree];
                this.type = INTERNALIZATION;
                if (this.playing) {
                    this.restart();
                } else {
                    this.playing = true;
                }
            },
            setupInternalizationTest: function(degree) {
                console.log("setupInternalizationTest", degree);
                this.chosenDegrees = [degree];
                this.type = INTERNALIZATION_TEST;
                if (this.playing) {
                    this.restart();
                } else {
                    this.playing = true;
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
                }
            });
        },
        mounted: function () {
            if (this.preselect !== undefined) {
                this.chosenDegrees = this.preselect;
            }
            if (this.tType === "internalization") this.type = INTERNALIZATION;
            else if (this.tType === "internalization-test") this.type = INTERNALIZATION_TEST;
            else if (this.tType === "recognition") this.type = RECOGNITION;
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

    #player .v-banner__wrapper
        padding-bottom: 0
        padding-top: 0
</style>