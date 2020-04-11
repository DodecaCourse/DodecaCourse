<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="0" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">{{ description }}</b>
        <DegreeCircle v-show="useInput === 1 && playing" class="ma-1"
                      :submit-solution="solutionInput" :enabled-degrees="chosenDegrees"
        :t-type="circleType">
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
        <div v-show="(useInput === 0 || useInput === 2) || !playing">
            <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
                <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
            </v-btn>
            <v-progress-circular class="my-progress-circular ma-1 text-center" :value="progress"
                                 :color="loaded ? 'primary': 'red'" size="50">
                <DegreeCirclePictogram :enabled-degrees="chosenDegrees">
                    {{roundSincePlay}}
                </DegreeCirclePictogram>
            </v-progress-circular>
            <div v-show="useInput === 2 && playing">
                <ChordQualityInput
                        :submit-solution="solutionInput" :enabled-qualities="chordTypes">
                </ChordQualityInput>
            </div>
        </div>
    </v-card>
</template>

<script>
    /* global MIDI */
    import { Midi, Scale } from "@tonaljs/tonal"
    import Vue from "vue";
    import DegreeCircle from "./DegreeCircle";
    import DegreeCirclePictogram from "./DegreeCirclePictogram";
    import ChordQualityInput from "./ChordQualityInput";

    const INTERNALIZATION = 0;
    const INTERNALIZATION_TEST = 1;
    const RECOGNITION_SINGLE = 2;
    const RECOGNITION_SINGLE_TEST = 3;
    const RECOGNITION_INTERVAL = 4;
    const RECOGNITION_INTERVAL_TEST = 5;
    const TARGET_TONE = 6;
    const TARGET_TONE_TEST = 7;
    const CHORD_QUALITY = 8;
    const CHORD_QUALITY_TEST = 9;
    const CHORD_INTERNALIZATION = 10;
    const CHORD_INTERNALIZATION_TEST = 11;
    const CHORD_RECOGNITION = 12;
    const CHORD_RECOGNITION_TEST = 13;

    const SPEED_SLOW = 100;
    const SPEED_MEDIUM_SLOW = 125;
    const SPEED_MEDIUM = 140;
    const SPEED_MEDIUM_FAST = 160;
    const SPEED_FAST = 180;

    const NO_INPUT = 0;
    const INPUT_CIRCLE = 1;
    const INPUT_CHORD_QUALITY = 2;

    const CADENCE_MAJOR_I_IV_V = 'major_i_iv_v';
    const CADENCE_MAJOR_I_IV_V_I = 'major_i_iv_v_i';

    const VELOCITY = 127;

    export default {
        name: "Teacher",
        components: {ChordQualityInput, DegreeCirclePictogram, DegreeCircle},
        data: function() {
            return {
                hidden: false,
                loaded: false,
                playing: false,

                // references to cancel setTimeout
                timeoutRef: null,
                progressRef: null,

                // settings
                tempoBPM: 130,
                stopAfterRounds: 12, // set to -1 to play endlessly
                changeKeyEvery: 1, // set to -1 to never change key
                chosenDegrees: [0, 2, 4, 5, 7, 9, 11], // activated degrees
                type: INTERNALIZATION,
                description: "Internalisation",
                cadenceType: CADENCE_MAJOR_I_IV_V,
                inputDisabled: false,
                fullCadenceEvery: 8,
                // Recognition interval
                intervals: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                // Recognition
                circleType: "degree",
                // Targeting tone
                targetDegree: 0,
                // Diatonic Chord Recognition
                chordTypes: [],
                diatonic: 0,
                diatonics: [0],
                diatonicCount: 3,

                // exercise state
                roundSincePlay: 0,
                key: "", // ['C', 'C#', 'D', ...]
                progress: 0, // progress in percent
                roundDuration: 0,
                startTime: 0,
                played: [],
                inputPos: 0,
                solution: [0],

                // NAMES & MAPPINGS
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
                // cadences with multiple options
                // resting chord is played whenever the tpnic should be reinforced without a full cadence
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
                chordTones: {
                    'maj': [0, 4, 7],
                    'min': [0, 3, 7],
                    'dim': [0, 3, 6],
                    'aug': [0, 4, 8],
                    'maj7': [0, 4, 7, 11],
                    'min7': [0, 3, 7, 10],
                    'dom7': [0, 4, 7, 10],
                    'dim7': [0, 3, 6, 9],
                    'min7b5': [0, 3, 6, 10]
                },
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
            useInput: function() {
                if (this.inputDisabled) return NO_INPUT;

                const no_input = [
                    INTERNALIZATION, INTERNALIZATION_TEST,
                    TARGET_TONE, TARGET_TONE_TEST,
                    CHORD_INTERNALIZATION, CHORD_INTERNALIZATION_TEST
                ];
                const input_circle = [
                    RECOGNITION_SINGLE, RECOGNITION_SINGLE_TEST,
                    RECOGNITION_INTERVAL, RECOGNITION_INTERVAL_TEST,
                    CHORD_RECOGNITION, CHORD_RECOGNITION_TEST
                ];
                const input_chord_quality = [
                    CHORD_QUALITY, CHORD_QUALITY_TEST
                ];
                if (no_input.indexOf(this.type) > -1) return NO_INPUT;
                else if (input_circle.indexOf(this.type) > -1) return INPUT_CIRCLE;
                else if (input_chord_quality.indexOf(this.type) > -1) return INPUT_CHORD_QUALITY;
                else {
                    console.error("useInput not set for type", this.type);
                    return NO_INPUT;
                }
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
                    const notes = this.transposeToKey(cadence.progression[chordNum], key, 4);
                    // play the notes
                    MIDI.setVolume(0, 127);
                    if(this.playing){
                      this.chordOn(0, notes, VELOCITY, posOff);
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
                /* play drone of tonic and fifth */
                const velocity = 110;
                const notes = this.transposeToKey([0, 7], key, 3);
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    this.chordOn(0, notes, velocity, posOff);
                    this.chordOff(0, notes, posOff + duration * this.quarter);
                }
                return posOff + duration * this.quarter;
            },
            playDegree: function (key, degree, withResting, posOff, duration, cadence, playOctaves) {
                /* play degree, optionally with resting chord */
                const root = key + '3';
                const note =  Midi.toMidi(root) + degree;
                if (withResting) {
                    this.playResting(key, cadence, posOff, duration);
                }
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    if (playOctaves) {
                        for (let i = 0; i < 3; i++) {
                            this.noteOn(0, note + i * 12, VELOCITY, posOff);
                            this.noteOff(0, note + i * 12, posOff + this.quarter * duration);
                        }
                    } else {
                        this.noteOn(0, note + 12, VELOCITY, posOff);
                        this.noteOff(0, note + 12, posOff + this.quarter * duration);
                    }
                }
                return posOff + this.quarter * duration;
            },
            playDiatonic: function (key, degree, count, posOff, duration, playOctaves) {
                /* Play a diatonic chord
                *
                * Builds a diatonic chord by choosing every second degree in self.degrees
                * _count_ times, starting on _degree_
                *  */
                const root = key + '3';
                const note =  Midi.toMidi(root);
                MIDI.setVolume(0, 127);
                const basePos = this.degrees.indexOf(degree);
                if (basePos < 0) {
                    console.error("Invalid configuration: degree ",
                        degree, "not in degrees", this.degrees)
                }
                if (this.playing) {
                    for (let i=0; i<count; i++) {
                        let oct = Math.floor((basePos + 2 * i) / this.degrees.length); // which octave
                        const curPos = (basePos + 2 * i) % this.degrees.length; // octave independent
                        const it = playOctaves ? 2 : 1;
                        for (let j=0; j<it; j++) {
                            this.noteOn(0, note + this.degrees[curPos] + 12 * (oct + j), VELOCITY, posOff);
                            this.noteOff(0, note + this.degrees[curPos] + 12 * (oct + j), posOff + this.quarter * duration);
                        }
                    }
                }
                return posOff + this.quarter * duration;
            },
            playChord:function (root, chordType, posOff, duration) {
                /* PLay chord specified by _chordType_ with root note _root_ */
                MIDI.setVolume(0, 127);
                const notes = this.transposeBy(this.chordTones[chordType], root);
                if (this.playing) {
                    this.chordOn(0, notes, VELOCITY, posOff);
                    this.chordOff(0, notes, posOff + duration * this.quarter);
                }
                return posOff + duration * this.quarter;
            },
            playNote:function (note, posOff, duration) {
                /* Play a MIDI note with a duration */
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    this.noteOn(0, note, VELOCITY, posOff);
                    this.noteOff(0, note, posOff + duration * this.quarter);
                }
                return posOff + duration * this.quarter;
            },
            transposeToKey: function (notes, key, octaves) {
                /* Transpose to _key_ and up/down _octaves_ octaves */
                const keyOffset = Midi.toMidi(key + '0') + 12 * octaves;
                let notesMod = [];
                for (let i=0; i<notes.length; i++) {
                    notesMod.push(notes[i] + keyOffset);
                }
                return notesMod;
            },
            transposeBy: function (notes, halfsteps) {
                let notesMod = [];
                for (let i=0; i<notes.length; i++) {
                    notesMod.push(notes[i] + halfsteps);
                }
                return notesMod;
            },
            playRound: function() {
                this.inputPos = 0;
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
                        posOff = this.playDegree(this.key, this.degrees[0], true, posOff, 4, cadence, true);
                        posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 4, cadence, true);
                    }
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                }
                else if (this.type === INTERNALIZATION_TEST) {
                    let [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V, 0);
                    posOff = this.playResting(this.key, cadence, posOff, 4);
                    posOff = this.rest(posOff, 3 * 4);
                    posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 8, cadence, true);
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
                    posOff = this.playDegree(this.key, degree, false, posOff, 4, cadence, false);

                    this.solution = [degree];
                    if (this.useInput !== NO_INPUT) {
                        console.log("USE_INPUT");
                        this.roundDuration = posOff;
                    } else {
                        posOff = this.rest(posOff, 2 * 4);
                        this.roundDuration = posOff;
                        this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                    }
                }
                else if (this.type === RECOGNITION_INTERVAL || this.type === RECOGNITION_INTERVAL_TEST) {
                    let degree = this.degrees[Math.floor(Math.random()*this.degrees.length)]; // choose randomly
                    // shift randomly up/down
                    degree += 12 * (Math.floor(Math.random() * 2 ) - 1);
                    const secondDegree = this.randomInterval(degree);
                    let posOff = 0;
                    let cadence = undefined;
                    if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                        [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V_I, 0);
                    } else {
                        posOff = this.playDrone(this.key, 0, 4);
                    }
                    posOff = this.playDegree(this.key, degree, false, posOff, 2, cadence, false);
                    posOff = this.playDegree(this.key, secondDegree, false, posOff, 2, cadence, false);

                    this.solution = [this.normalizeDegree(degree),
                        this.normalizeDegree(secondDegree)];

                    if (this.useInput !== NO_INPUT) {
                        console.log("USE_INPUT");
                        this.roundDuration = posOff;
                    } else {
                        posOff = this.rest(posOff, 2 * 4);
                        this.roundDuration = posOff;
                        this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                    }
                }
                else if (this.type === TARGET_TONE) {
                    let root = Math.floor(Math.random()*12) + 5 * 12; // choose randomly
                    let chordType = this.chordTypes[Math.floor(Math.random()*this.chordTypes.length)]; // choose randomly
                    root += 12 * (Math.floor(Math.random() * 2 ) - 1);
                    let posOff = 0;
                    for (let i=0; i<4; i++) {
                        posOff = this.playChord(root, chordType, posOff, 4);
                        posOff = this.playNote(root + this.targetDegree, posOff, 4);
                    }
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                } else if (this.type === TARGET_TONE_TEST) {
                    let root = Math.floor(Math.random()*12) + 5 * 12; // choose randomly
                    let chordType = this.chordTypes[Math.floor(Math.random()*this.chordTypes.length)]; // choose randomly
                    root += 12 * (Math.floor(Math.random() * 2 ) - 1);
                    let posOff = 0;
                    posOff = this.playChord(root, chordType, posOff, 4);
                    posOff = this.rest(posOff, 4);
                    posOff = this.playNote(root + this.targetDegree, posOff, 4);
                    posOff = this.rest(posOff, 4);
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                } else if (this.type === CHORD_QUALITY || this.type === CHORD_QUALITY_TEST) {
                    let root = Math.floor(Math.random()*12) + 5 * 12; // choose randomly
                    let chordType = this.chordTypes[Math.floor(Math.random()*this.chordTypes.length)]; // choose randomly
                    root += 12 * (Math.floor(Math.random() * 2 ) - 1);
                    let posOff = 0;
                    posOff = this.playChord(root, chordType, posOff, 4);
                    this.solution = [chordType];

                    if (this.useInput !== NO_INPUT) {
                        console.log("USE_INPUT");
                        this.roundDuration = posOff;
                    } else {
                        posOff = this.rest(posOff, 2 * 4);
                        this.roundDuration = posOff;
                        this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                    }
                }
                else if (this.type === CHORD_INTERNALIZATION || this.type === CHORD_INTERNALIZATION_TEST) {
                    let [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V, 0);
                    for (let i=0;i<4;i++) {
                        posOff = this.playResting(this.key, cadence, posOff, 4);
                        posOff = this.playDiatonic(this.key, this.diatonic, this.diatonicCount, posOff, 4, cadence, false);
                    }
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                }
                else if (this.type === CHORD_RECOGNITION || this.type === CHORD_RECOGNITION_TEST) {
                    let diatonic = this.diatonics[Math.floor(Math.random()*this.diatonics.length)]; // choose randomly
                    let posOff = 0;
                    let cadence = undefined;
                    if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                        [posOff, cadence] = this.playCadence(this.key, CADENCE_MAJOR_I_IV_V_I, 0);
                    } else {
                        posOff = this.playDrone(this.key, 0, 4);
                    }
                    posOff = this.playDiatonic(this.key, diatonic, this.diatonicCount, posOff, 4, cadence, false);

                    this.solution = [diatonic];
                    if (this.useInput !== NO_INPUT) {
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
                if (this.solution === null || this.inputPos >= this.solution.length) {
                    return;
                }
                const curSolution = this.solution[this.inputPos];
                console.log("SOLUTION_INPUT: ",input,curSolution,curSolution === input);
                if (curSolution === input) {
                    this.inputPos++;
                    if (this.inputPos === this.solution.length) {
                        let posOff = this.rest(0, 2);
                        this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
                    }
                    return [true, curSolution];
                } else {
                    let posOff = this.rest(0, 2 * this.solution.length - this.inputPos);
                    this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
                    return [false, this.solution.slice(this.inputPos)]
                }
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
                this.tempoBPM = SPEED_MEDIUM;
                this.finishSetup(autoplay);
            },
            setupInternalizationTest: function(degree, autoplay) {
                console.log("setupInternalizationTest", degree);
                this.description = "Internalisation Test";
                this.chosenDegrees = [degree];
                this.type = INTERNALIZATION_TEST;
                this.stopAfterRounds = 12;
                this.tempoBPM = SPEED_MEDIUM;
                this.finishSetup(autoplay);
            },

            setupRecognitionSingle: function(degrees, autoplay, level) {
                console.log("setupRecognitionSingle", degrees);
                this.description = "Recognition";
                this.chosenDegrees = degrees;
                this.type = RECOGNITION_SINGLE;
                this.circleType = "degree";
                this.stopAfterRounds = -1;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 3) this.tempoBPM = SPEED_FAST;
                this.finishSetup(autoplay);
            },
            setupRecognitionSingleTest: function(degrees, autoplay, level) {
                console.log("setupRecognitionSingleTest", degrees);
                this.description = "Recognition Test";
                this.chosenDegrees = degrees;
                this.type = RECOGNITION_SINGLE_TEST;
                this.circleType = "degree";
                this.stopAfterRounds = 32;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 3) this.tempoBPM = SPEED_FAST;
                this.finishSetup(autoplay);
            },

            setupRecognitionInterval: function(degrees, intervals, autoplay, level) {
                console.log("setupRecognitionInterval", degrees);
                this.description = "Recognition";
                this.chosenDegrees = degrees;
                this.intervals = intervals;
                this.type = RECOGNITION_INTERVAL;
                this.circleType = "degree";
                this.stopAfterRounds = -1;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM_SLOW;
                else if (level === 3) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 4) this.tempoBPM = SPEED_MEDIUM_FAST;
                else if (level === 5) this.tempoBPM = SPEED_FAST;
                this.finishSetup(autoplay);
            },
            setupRecognitionIntervalTest: function(degrees, intervals, autoplay, level) {
                console.log("setupRecognitionIntervalTest", degrees);
                this.description = "Recognition Test";
                this.chosenDegrees = degrees;
                this.intervals = intervals;
                this.type = RECOGNITION_INTERVAL_TEST;
                this.circleType = "degree";
                this.stopAfterRounds = 32;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM_SLOW;
                else if (level === 3) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 4) this.tempoBPM = SPEED_MEDIUM_FAST;
                else if (level === 5) this.tempoBPM = SPEED_FAST;
                this.finishSetup(autoplay);
            },

            setupTargetTone(chordTypes, autoplay) {
                console.log("setupTargetTone", chordTypes);
                this.description = "Target Tones";
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.stopAfterRounds = -1;
                this.type = TARGET_TONE;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.finishSetup(autoplay);
            },
            setupTargetToneTest(chordTypes, autoplay) {
                console.log("setupTargetToneTest", chordTypes);
                this.description = "Target Tones";
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.type = TARGET_TONE_TEST;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.stopAfterRounds = 12;
                this.finishSetup(autoplay);
            },

            setupChordQuality(chordTypes, autoplay) {
                console.log("setupChordQuality", chordTypes);
                this.description = "Chord Quality";
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.stopAfterRounds = -1;
                this.type = CHORD_QUALITY;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.finishSetup(autoplay);
            },
            setupChordQualityTest(chordTypes, autoplay) {
                console.log("setupChordQualityTest", chordTypes);
                this.description = "Chord Quality";
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.type = CHORD_QUALITY_TEST;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.stopAfterRounds = 12;
                this.finishSetup(autoplay);
            },

            setupChordInternalization(diatonic, degrees, count, autoplay) {
                console.log("setupChordInternalization", diatonic);
                this.description = "Chord Internalization";
                this.chosenDegrees = degrees;
                this.diatonic = diatonic;
                this.diatonicCount = count;
                this.stopAfterRounds = -1;
                this.type = CHORD_INTERNALIZATION;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.finishSetup(autoplay);
            },
            setupChordInternalizationTest(diatonic, degrees, count, autoplay) {
                console.log("setupChordInternalization", diatonic);
                this.description = "Chord Internalization";
                this.chosenDegrees = degrees;
                this.diatonic = diatonic;
                this.diatonicCount = count;
                this.stopAfterRounds = 12;
                this.type = CHORD_INTERNALIZATION_TEST;
                this.tempoBPM = SPEED_MEDIUM_SLOW;
                this.finishSetup(autoplay);
            },
            setupChordRecognition(diatonics, degrees, count, autoplay, level) {
                console.log("setupChordRecognition", diatonics);
                this.description = "Chord Recognition";
                this.chosenDegrees = degrees;
                this.diatonics = diatonics;
                this.diatonicCount = count;
                this.type = CHORD_RECOGNITION;
                this.circleType = "chord";
                this.stopAfterRounds = -1;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 3) this.tempoBPM = SPEED_FAST;
                this.finishSetup(autoplay);
            },
            setupChordRecognitionTest(diatonics, degrees, count, autoplay, level) {
                console.log("setupChordRecognitionTest", diatonics);
                this.description = "Chord Recognition";
                this.chosenDegrees = degrees;
                this.diatonics = diatonics;
                this.diatonicCount = count;
                this.type = CHORD_RECOGNITION_TEST;
                this.circleType = "chord";
                this.stopAfterRounds = 32;
                this.changeKeyEvery = this.fullCadenceEvery;
                if (level === 1) this.tempoBPM = SPEED_SLOW;
                else if (level === 2) this.tempoBPM = SPEED_MEDIUM;
                else if (level === 3) this.tempoBPM = SPEED_FAST;
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
            normalizeDegree: function (degree) {
                // Bring degree into range from 0 to 11
                return Math.abs(degree % 12 > -1 ? degree % 12 : degree % 12 + 12);
            },
            randomInterval: function (degree) {
                /* Return a random interval (up or down) from _degree_ from this.intervals */
                let intervalsAvailable = [];
                for (let i=0; i<this.intervals.length; i++) {
                    if (this.degrees.indexOf(this.normalizeDegree(degree + this.intervals[i])) > -1) {
                        intervalsAvailable.push(degree + this.intervals[i]);
                    }
                    if (this.degrees.indexOf(this.normalizeDegree(degree - this.intervals[i])) > -1) {
                        intervalsAvailable.push(degree - this.intervals[i]);
                    }
                }
                return intervalsAvailable[Math.floor(Math.random()*intervalsAvailable.length)];
            },
            updateProgress: function () {
                /* Update the progress property */
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
                    console.log('MIDI.stopAllNotes failed:');
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
            // Initialize MIDI
            MIDI.loadPlugin({
                soundfontUrl: "/soundfont/",
                instrument: "acoustic_grand_piano",
                onprogress: function (state, progress) {
                    console.log(state, progress);
                    self.progress = progress * 100;
                },
                onsuccess: function () {
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