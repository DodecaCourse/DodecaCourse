<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="0" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">{{ description }}</b>
        <DegreeCircle v-if="(useInput === 1 || useInput === 2) && playing" class="ma-1"
                      :submit-solution="solutionInput" :enabled-buttons="chosenDegrees"
                      :labels="circleLabels">
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
        <div v-if="(useInput === 0 || useInput === 3) || !playing">
            <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
                <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
            </v-btn>
            <v-progress-circular class="my-progress-circular ma-1 text-center" :value="progress"
                                 :color="loaded ? 'primary': 'red'" size="50" :indeterminate="!loaded">
                <DegreeCirclePictogram :enabled-degrees="chosenDegrees">
                    <span>{{roundSincePlay}}</span>
                </DegreeCirclePictogram>
            </v-progress-circular>
            <div v-if="useInput === 3 && playing">
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
    // const CHORD_INTERNALIZATION_TEST = 11;
    const CHORD_RECOGNITION = 12;
    const CHORD_RECOGNITION_TEST = 13;

    const SPEED_SLOW = 100;
    const SPEED_MEDIUM_SLOW = 125;
    const SPEED_MEDIUM = 140;
    const SPEED_MEDIUM_FAST = 160;
    const SPEED_FAST = 180;

    const NO_INPUT = 0;
    const INPUT_CIRCLE = 1;
    const INPUT_CIRCLE_CHORD = 2;
    const INPUT_CHORD_QUALITY = 3;

    const CADENCE_I_IV_V = 'i_iv_v';
    const CADENCE_I_IV_V_I = 'i_iv_v_i';
    const MODE_IONIAN = 'ionian';
    const MODE_AEOLIAN = 'aeolian';

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
                changeKeyEvery: 1, // set to -1 to never change key
                chosenDegrees: [0, 2, 4, 5, 7, 9, 11], // activated degrees
                type: INTERNALIZATION,
                inputDisabled: false,
                fullCadenceEvery: 8,
                level: 1,
                scale: MODE_AEOLIAN,

                curConfigurator: null,
                // Recognition interval
                intervals: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                // Targeting tone
                targetDegree: 0,
                // Diatonic Chord Recognition
                chordTypes: [],
                diatonic: 0,
                diatonics: [0],
                diatonicCount: 3,

                // exercise state
                roundSincePlay: 0,
                correctSincePlay: 0,
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
                // resting chord is played whenever the tonic should be reinforced without a full cadence
                cadences: {
                    [MODE_IONIAN]: {
                        [CADENCE_I_IV_V]: [
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
                        [CADENCE_I_IV_V_I]: [
                            {
                                progression: [[-12, 0, 4, 7], [-7, -3, 0, 5], [-5, -1, 2, 7], [-12, 0, 4, 7]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, 0, 4, 7]
                            },
                            {
                                progression: [[-12, 4, 7, 12], [-7, 0, 5, 9], [-5, 2, 7, 11], [-12, 4, 7, 12]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, 4, 7, 12]
                            },
                            {
                                progression: [[-12, -5, 0, 4], [-19, -3, 0, 5], [-17, -5, -1, 2], [-12, -5, 0, 4]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, -5, 0, 4]
                            },
                        ],
                    },
                    [MODE_AEOLIAN]: {
                        [CADENCE_I_IV_V]: [
                            {
                                progression: [[-12, 0, 3, 7], [-7, -4, 0, 5], [-5, -1, 2, 7]],
                                chordLength: [4, 2, 2],
                                resting: [-12, 0, 3, 7]
                            },
                            {
                                progression: [[-12, 3, 7, 12], [-7, 0, 5, 8], [-5, 2, 7, 11]],
                                chordLength: [4, 2, 2],
                                resting: [-12, 3, 7, 12]
                            },
                            {
                                progression: [[-12, -5, 0, 3], [-19, -4, 0, 5], [-17, -5, -1, 2]],
                                chordLength: [4, 2, 2],
                                resting: [-12, -5, 0, 3]
                            },
                        ],
                        [CADENCE_I_IV_V_I]: [
                            {
                                progression: [[-12, 0, 3, 7], [-7, -4, 0, 5], [-5, -1, 2, 7], [-12, 0, 3, 7]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, 0, 3, 7]
                            },
                            {
                                progression: [[-12, 3, 7, 12], [-7, 0, 5, 8], [-5, 2, 7, 11], [-12, 3, 7, 12]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, 3, 7, 12]
                            },
                            {
                                progression: [[-12, -5, 0, 3], [-19, -4, 0, 5], [-17, -5, -1, 2], [-12, -5, 0, 3]],
                                chordLength: [4, 2, 2, 4],
                                resting: [-12, -5, 0, 3]
                            },
                        ],
                    }
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
                    CHORD_INTERNALIZATION
                ];
                const input_circle = [
                    RECOGNITION_SINGLE, RECOGNITION_SINGLE_TEST,
                    RECOGNITION_INTERVAL, RECOGNITION_INTERVAL_TEST
                ];
                const input_circle_chord = [
                    CHORD_RECOGNITION, CHORD_RECOGNITION_TEST
                ];
                const input_chord_quality = [
                    CHORD_QUALITY, CHORD_QUALITY_TEST
                ];
                if (no_input.indexOf(this.type) > -1) return NO_INPUT;
                else if (input_circle.indexOf(this.type) > -1) return INPUT_CIRCLE;
                else if (input_circle_chord.indexOf(this.type) > -1) return INPUT_CIRCLE_CHORD;
                else if (input_chord_quality.indexOf(this.type) > -1) return INPUT_CHORD_QUALITY;
                else {
                    console.error("useInput not set for type", this.type);
                    return NO_INPUT;
                }
            },
            description: function () {
                if (this.type === INTERNALIZATION || this.type === INTERNALIZATION_TEST ||
                    this.type === CHORD_INTERNALIZATION)
                    return "Internalisation";
                else if (this.type === RECOGNITION_SINGLE || this.type === RECOGNITION_SINGLE_TEST ||
                         this.type === RECOGNITION_INTERVAL || this.type === RECOGNITION_INTERVAL_TEST ||
                         this.type === CHORD_RECOGNITION || this.type === CHORD_RECOGNITION_TEST)
                    return "Recognition";
                else if (this.type === TARGET_TONE || this.type === TARGET_TONE_TEST) return "Targeting Tones";
                else if (this.type === CHORD_QUALITY || this.type === CHORD_QUALITY_TEST) return "Chord Quality";
                else {
                    console.warn("No description for type", this.type);
                    return ""
                }
            },
            tempoBPM: function () {
                if (this.type === INTERNALIZATION || this.type === INTERNALIZATION_TEST) return SPEED_MEDIUM;
                else if (this.type === RECOGNITION_SINGLE || this.type === RECOGNITION_SINGLE_TEST) {
                    if (this.level === 1) return SPEED_SLOW;
                    else if (this.level === 2) return SPEED_MEDIUM;
                    else if (this.level === 3) return SPEED_FAST;
                }
                else if (this.type === RECOGNITION_INTERVAL || this.type === RECOGNITION_INTERVAL_TEST) {
                    if (this.level === 1) return SPEED_SLOW;
                    else if (this.level === 2) return SPEED_MEDIUM_SLOW;
                    else if (this.level === 3) return SPEED_MEDIUM;
                    else if (this.level === 4) return SPEED_MEDIUM_FAST;
                    else if (this.level === 5) return SPEED_FAST;
                }
                else if (this.type === TARGET_TONE || this.type === TARGET_TONE_TEST) return SPEED_MEDIUM_SLOW;
                else if (this.type === CHORD_QUALITY || this.type === CHORD_QUALITY_TEST) return SPEED_MEDIUM_SLOW;
                else if (this.type === CHORD_INTERNALIZATION) return SPEED_MEDIUM_SLOW;
                else if (this.type === CHORD_RECOGNITION || this.type === CHORD_RECOGNITION_TEST) {
                    if (this.level === 1) return SPEED_SLOW;
                    else if (this.level === 2) return SPEED_MEDIUM;
                    else if (this.level === 3) return SPEED_FAST;
                }
                console.warn("No tempo for type", this.type, "with level", this.level);
                return SPEED_MEDIUM;
            },
            stopAfterRounds: function () {
                // set to -1 to play endlessly
                if (this.type === INTERNALIZATION_TEST) return 12;
                else if (this.type === RECOGNITION_SINGLE_TEST) return 32;
                else if (this.type === RECOGNITION_INTERVAL_TEST) return 32;
                else if (this.type === TARGET_TONE_TEST) return 12;
                else if (this.type === CHORD_QUALITY_TEST) return 16;
                else if (this.type === CHORD_RECOGNITION_TEST) return 32;
                return -1;
            },
            correctToSucceed: function () {
                if (this.type === RECOGNITION_SINGLE_TEST) return 27;
                else if (this.type === RECOGNITION_INTERVAL_TEST) return 27;
                else if (this.type === CHORD_QUALITY_TEST) return 13;
                else if (this.type === CHORD_RECOGNITION_TEST) return 27;
                return -1;
            },
            circleLabels: function () {
                if (this.useInput === INPUT_CIRCLE_CHORD && this.diatonicCount <= 3 &&
                    this.scale === MODE_IONIAN) {
                    return ["I", "", "ii", "", "iii", "IV", "", "V", "", "vi", "", "vii°"]
                } else if (this.useInput === INPUT_CIRCLE_CHORD && this.diatonicCount > 3 &&
                           this.scale === MODE_IONIAN ) {
                    return ["IM7", "", "ii7", "", "iii7", "IVM7",
                        "", "V7", "", "vi7", "", "vii7b5"]
                } else if (this.useInput === INPUT_CIRCLE_CHORD && this.diatonicCount <= 3 &&
                    this.scale === MODE_AEOLIAN) {
                    return ["i", "", "ii°", "III", "", "iv", "", "V", "VI", "", "VII", ""]
                } else if (this.useInput === INPUT_CIRCLE_CHORD && this.diatonicCount > 3 &&
                    this.scale === MODE_AEOLIAN) {
                    return ["i7", "", "ii7b5", "IIIM7", "", "iv7",
                        "", "V7", "VIM7", "", "VII7", ""]
                }
                return ["Do", "Ra", "Re", "Me", "Mi", "Fa", "Fi", "So", "Le", "La", "Te", "Ti"]
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
                const cadence = this.cadences[this.scale][cadenceType][Math.floor(
                    Math.random()*this.cadences[this.scale][cadenceType].length)]; // select cadence randomly
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
                            // raise seventh in minor on dominant chord
                            let move = 0;
                            if (this.scale === MODE_AEOLIAN && this.degrees[basePos] === 7 &&
                                this.degrees[curPos] === 10) {
                                move = 1;
                            }
                            this.noteOn(0,
                                note + this.degrees[curPos] + 12 * (oct + j) + move, VELOCITY, posOff);
                            this.noteOff(0,
                                note + this.degrees[curPos] + 12 * (oct + j) + move, posOff + this.quarter * duration);
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
            roundInternalization: function () {
                let [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V, 0);
                for (let i=0;i<4;i++) {
                    posOff = this.playDegree(this.key, this.degrees[0], true, posOff, 4, cadence, true);
                    posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 4, cadence, true);
                }
                this.roundDuration = posOff;
                this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
            },
            roundInternalizationTest: function () {
                let [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V, 0);
                posOff = this.playResting(this.key, cadence, posOff, 4);
                posOff = this.rest(posOff, 3 * 4);
                posOff = this.playDegree(this.key, this.degrees[0], false, posOff, 8, cadence, true);
                posOff = this.rest(posOff, 4);
                this.roundDuration = posOff;
                this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
            },
            roundRecognitionSingle: function () {
                const degree = this.degrees[Math.floor(Math.random()*this.degrees.length)];     // choose randomly
                let posOff;
                let cadence = undefined;
                if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                    [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V_I, 0);
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
            },
            roundRecognitionInterval: function () {
                let degree = this.degrees[Math.floor(Math.random()*this.degrees.length)]; // choose randomly
                // shift randomly up/down
                degree += 12 * (Math.floor(Math.random() * 2 ) - 1);
                const secondDegree = this.randomInterval(degree);
                let posOff;
                let cadence = undefined;
                if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                    [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V_I, 0);
                } else {
                    posOff = this.playDrone(this.key, 0, 4);
                }
                posOff = this.playDegree(this.key, degree, false, posOff, 2, cadence, false);
                posOff = this.playDegree(this.key, secondDegree, false, posOff, 2, cadence, false);

                this.solution = [this.normalizeDegree(degree), this.normalizeDegree(secondDegree)];

                if (this.useInput !== NO_INPUT) {
                    console.log("USE_INPUT");
                    this.roundDuration = posOff;
                } else {
                    posOff = this.rest(posOff, 2 * 4);
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                }
            },
            roundTargetTone: function () {
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
            },
            roundTargetToneTest: function () {
                let root = Math.floor(Math.random()*12) + 5 * 12; // choose randomly
                let chordType = this.chordTypes[Math.floor(Math.random()*this.chordTypes.length)]; // choose randomly
                root += 12 * (Math.floor(Math.random() * 2 ) - 1);
                let posOff = this.playChord(root, chordType, 0, 4);
                posOff = this.rest(posOff, 4);
                posOff = this.playNote(root + this.targetDegree, posOff, 4);
                posOff = this.rest(posOff, 4);
                this.roundDuration = posOff;
                this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
            },
            roundChordQuality: function () {
                let root = Math.floor(Math.random()*12) + 5 * 12; // choose randomly
                let chordType = this.chordTypes[Math.floor(Math.random()*this.chordTypes.length)]; // choose randomly
                root += 12 * (Math.floor(Math.random() * 2 ) - 1);
                let posOff = this.playChord(root, chordType, 0, 4);
                this.solution = [chordType];

                if (this.useInput !== NO_INPUT) {
                    console.log("USE_INPUT");
                    this.roundDuration = posOff;
                } else {
                    posOff = this.rest(posOff, 2 * 4);
                    this.roundDuration = posOff;
                    this.timeoutRef = setTimeout(this.solutionNoInput, this.roundDuration * 1000);
                }
            },
            roundChordInternalization: function () {
                let [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V, 0);
                for (let i=0;i<4;i++) {
                    posOff = this.playResting(this.key, cadence, posOff, 4);
                    posOff = this.playDiatonic(this.key, this.diatonic, this.diatonicCount, posOff, 4, cadence, false);
                }
                this.roundDuration = posOff;
                this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
            },
            roundChordRecognition: function () {
                let diatonic = this.diatonics[Math.floor(Math.random()*this.diatonics.length)]; // choose randomly
                let posOff;
                let cadence = undefined;
                if ((this.roundSincePlay - 1) % this.fullCadenceEvery === 0) {
                    [posOff, cadence] = this.playCadence(this.key, CADENCE_I_IV_V_I, 0);
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
                    this.key = chrom[Math.floor(Math.random() * chrom.length)];
                }
                if (this.type === INTERNALIZATION) this.roundInternalization();
                else if (this.type === INTERNALIZATION_TEST) this.roundInternalizationTest();
                else if (this.type === RECOGNITION_SINGLE || this.type === RECOGNITION_SINGLE_TEST)
                    this.roundRecognitionSingle();
                else if (this.type === RECOGNITION_INTERVAL || this.type === RECOGNITION_INTERVAL_TEST)
                    this.roundRecognitionInterval();
                else if (this.type === TARGET_TONE) this.roundTargetTone();
                else if (this.type === TARGET_TONE_TEST) this.roundTargetToneTest();
                else if (this.type === CHORD_QUALITY || this.type === CHORD_QUALITY_TEST)
                    this.roundChordQuality();
                else if (this.type === CHORD_INTERNALIZATION)
                    this.roundChordInternalization();
                else if (this.type === CHORD_RECOGNITION || this.type === CHORD_RECOGNITION_TEST)
                    this.roundChordRecognition();

                // state to calculate progress
                this.startTime = new Date().getTime();
                this.updateProgress();
            },
            solutionNoInput: function() {
                /* TODO: Output solution via audio for the user to compare */
                console.log("SOLUTION_NO_INPUT: ",this.solution);
                let posOff = this.rest(0,  4);
                this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
            },
            solutionInput: function(input) {
                /* returns: correct (bool), solution (Object if correct, else Array) */
                if (this.solution === null || this.inputPos >= this.solution.length) {
                    // no solution to compare with
                    return;
                }
                const curSolution = this.solution[this.inputPos];
                console.log("SOLUTION_INPUT: ",input,curSolution,curSolution === input);
                if (curSolution === input) {
                    this.inputPos++;
                    if (this.inputPos === this.solution.length) {
                        // finished round
                        let posOff = this.rest(0, 2);
                        this.correctSincePlay++;
                        this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
                    }
                    return [true, curSolution];
                } else {
                    // wrong -> round ends
                    let posOff = this.rest(0, 2 * this.solution.length - this.inputPos);
                    this.timeoutRef = setTimeout(this.doRepeat, posOff * 1000);
                    // return the correct solution not yet answered
                    return [false, this.solution.slice(this.inputPos)]
                }
            },
            doRepeat: function() {
                /* Automatically play a new round */
                // clear up previous round
                this.stopAllNotes();
                this.clearTimeouts();
                if ( 0 < this.stopAfterRounds && this.stopAfterRounds <= this.roundSincePlay) {
                    // autostop for tests -> test finished
                    this.playing = false;
                    if (this.correctToSucceed > -1 && this.curConfigurator != null) {
                        this.curConfigurator.setCompleted(this.level,
                            this.correctSincePlay >= this.correctToSucceed);
                    }
                }
                if (this.playing) this.playRound();
            },
            setConfigurator: function (configurator) {
                this.curConfigurator = configurator;
            },
            // setup functions for different practice/test scenarios
            setupInternalization: function(degree, autoplay, level, scale) {
                console.log("setupInternalization", degree);
                this.type = INTERNALIZATION;
                this.chosenDegrees = [degree];
                this.finishSetup(autoplay, level, scale);
            },
            setupInternalizationTest: function(degree, autoplay, level, scale) {
                console.log("setupInternalizationTest", degree);
                this.type = INTERNALIZATION_TEST;
                this.chosenDegrees = [degree];
                this.finishSetup(autoplay, level, scale);
            },

            setupRecognitionSingle: function(degrees, autoplay, level, scale) {
                console.log("setupRecognitionSingle", degrees);
                this.type = RECOGNITION_SINGLE;
                this.chosenDegrees = degrees;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },
            setupRecognitionSingleTest: function(degrees, autoplay, level, scale) {
                console.log("setupRecognitionSingleTest", degrees);
                this.type = RECOGNITION_SINGLE_TEST;
                this.chosenDegrees = degrees;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },

            setupRecognitionInterval: function(degrees, intervals, autoplay, level, scale) {
                console.log("setupRecognitionInterval", degrees);
                this.type = RECOGNITION_INTERVAL;
                this.chosenDegrees = degrees;
                this.intervals = intervals;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },
            setupRecognitionIntervalTest: function(degrees, intervals, autoplay, level, scale) {
                console.log("setupRecognitionIntervalTest", degrees);
                this.type = RECOGNITION_INTERVAL_TEST;
                this.chosenDegrees = degrees;
                this.intervals = intervals;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },

            setupTargetTone(chordTypes, autoplay, level, scale) {
                console.log("setupTargetTone", chordTypes);
                this.type = TARGET_TONE;
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.finishSetup(autoplay, level, scale);
            },
            setupTargetToneTest(chordTypes, autoplay, level, scale) {
                console.log("setupTargetToneTest", chordTypes);
                this.type = TARGET_TONE_TEST;
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.finishSetup(autoplay, level, scale);
            },

            setupChordQuality(chordTypes, autoplay, level, scale) {
                console.log("setupChordQuality", chordTypes);
                this.type = CHORD_QUALITY;
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.finishSetup(autoplay, level, scale);
            },
            setupChordQualityTest(chordTypes, autoplay, level, scale) {
                console.log("setupChordQualityTest", chordTypes);
                this.type = CHORD_QUALITY_TEST;
                this.chosenDegrees = [];
                this.chordTypes = chordTypes;
                this.finishSetup(autoplay, level, scale);
            },

            setupChordInternalization(diatonic, degrees, count, autoplay, level, scale) {
                this.type = CHORD_INTERNALIZATION;
                console.log("setupChordInternalization", diatonic);
                this.chosenDegrees = degrees;
                this.diatonic = diatonic;
                this.diatonicCount = count;
                this.finishSetup(autoplay, level, scale);
            },
            setupChordRecognition(diatonics, degrees, count, autoplay, level, scale) {
                this.type = CHORD_RECOGNITION;
                console.log("setupChordRecognition", diatonics);
                this.chosenDegrees = degrees;
                this.diatonics = diatonics;
                this.diatonicCount = count;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },
            setupChordRecognitionTest(diatonics, degrees, count, autoplay, level, scale) {
                this.type = CHORD_RECOGNITION_TEST;
                console.log("setupChordRecognitionTest", diatonics);
                this.chosenDegrees = degrees;
                this.diatonics = diatonics;
                this.diatonicCount = count;
                this.changeKeyEvery = this.fullCadenceEvery;
                this.finishSetup(autoplay, level, scale);
            },

            finishSetup: function (autoplay, level, scale) {
                this.level = level || 1;
                this.scale = scale || MODE_IONIAN;
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
            },
            loadMIDI: function () {
                const self = this;
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
            }
        },
        created: function initAudio() {
            if (this.$teacher !== undefined) {
                this.$teacher.playing = false;
            }
            Vue.prototype.$teacher = this;
            // Initialize MIDI
            if (typeof MIDI !== 'undefined') {
                this.loadMIDI();
            } else {
                window.onload = this.loadMIDI;
            }
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