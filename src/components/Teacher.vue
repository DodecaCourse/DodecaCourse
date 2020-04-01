<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="5" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">Play I-IV-V-I:</b>
        <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
            <v-icon>{{ playing ? 'mdi-stop' : 'mdi-play' }}</v-icon>
        </v-btn>
            <v-select class="mx-1"
                      :readonly="fixedDegree !== undefined"
                      :items="degreesAvailable"
                      v-model="chosenDegree"
                      label="Degree"
                      single-line
                      style="max-width: 150px;"
                      dense
            />
        <v-progress-circular class="my-progress-circular ml-2" :value="progress"
                             :color="loaded ? 'primary': 'red'"/>
    </v-card>
</template>

<script>
    /* global MIDI */
    import { Note, Midi, Scale } from "@tonaljs/tonal"

    export default {
        name: "Teacher",
        props: ['fixedDegree'],
        data: function() {
            return {
                playing: false,
                status: 'Not loaded',
                loaded: false,
                tempoBPM: 80,
                progression: ["CMaj7", "Dm7", "G7", "CMaj7"],
                key: "",
                sinceKeyChange: 0,
                changeKeyEvery: 1,
                timeoutRef: null,
                progressRef: null,
                progress: 0,
                roundDuration: 0,
                startTime: 0,
                degreesAvailable: [
                    {text: 'Tonic', value: '1P'},
                    {text: 'Second', value: '2M'},
                    {text: 'Major Third', value: '3M'},
                    {text: 'Fourth', value: '4P'},
                    {text: 'Fifth', value: '5P'},
                    {text: 'Major Sixth', value: '6M'},
                    {text: 'Major Seventh', value: '7M'},
                ],
                chosenDegree: "1P",
                played: [],
                cadences: {
                    'major_authentic': [
                        {
                            progression: [[-12, 0, 4, 7], [-7, -3, 0, 5], [-5, -1, 2, 7], [-12, 0, 4, 7]],
                            resting: [-12, 0, 4, 7]
                        },
                        {
                            progression: [[-12, 4, 7, 12], [-7, 0, 5, 9], [-5, 2, 7, 11], [-12, 4, 7, 12]],
                            resting: [-12, 4, 7, 12]
                        },
                        {
                            progression: [[-12, -5, 0, 4], [-19, -3, 0, 5], [-17, -5, -1, 2], [-12, -5, 0, 4]],
                            resting: [-12, -5, 0, 4]
                        },
                    ]
                },
                cadenceType: 'major_authentic',
            };
        },
        computed: {
            duration: function () { return 60 / this.tempoBPM },
            degree: function () {
                return this.fixedDegree !== undefined ? this.fixedDegree : this.chosenDegree;
            },
            degreeName: function () {
                for (let i=0; i<this.degreesAvailable.length;i++) {
                    if (this.degreesAvailable[i]['value'] === this.degree) {
                        return this.degreesAvailable[i]['text']
                    }
                }
                return 'None'
            }
        },
        watch: {
            playing: function (val) {
                if (val) {
                    this.playRound();
                } else {
                    this.clearTimeouts();
                    this.progress = 0;
                    this.stopAllNotes();
                }
            }
        },
        methods: {
            playCadence: function (key, cadenceType, posOff, duration) {
                /* play *cadenceType* in *key* */
                let dur = posOff; // total duration
                const cadence = this.cadences[cadenceType][Math.floor(
                    Math.random()*this.cadences[cadenceType].length)]; // select cadence randomly
                for (let chordNum=0; chordNum < cadence.progression.length; chordNum++) {
                    // play transposed cadence
                    let delay = posOff + chordNum * duration; // play one note every quarter second
                    const velocity = 110; // how hard the note hits
                    const notes = this.transposeToKey(cadence.progression[chordNum], key, 4);
                    // play the notes
                    MIDI.setVolume(0, 127);
                    if(this.playing){
                      this.chordOn(0, notes, velocity, delay);
                      this.chordOff(0, notes, delay + duration);
                    }
                    if (delay + duration > dur) dur = delay + duration; // set total duration
                }
                // return duration, cadence for cadence.resting chord
                return [dur, cadence];
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
                    this.chordOff(0, notes, delay + duration);
                }
                return delay + duration;
            },
            playDegree: function (key, degree, withResting, posOff, cadence) {
                /* play degree, optionally with resting chord */
                const root = key + '3';
                const note =  Midi.toMidi(Note.transpose(root, degree));
                if (withResting) {
                    this.playResting(key, cadence, posOff, 4*this.duration);
                }
                const delay = posOff;
                const velocity = 127; // how hard the note hits
                MIDI.setVolume(0, 127);
                if (this.playing) {
                    for (let i=0; i<3; i++) {
                        this.noteOn(0, note + i * 12, velocity, delay);
                        this.noteOff(0, note + i * 12, delay + this.duration * 4);
                    }
                }
                return delay + this.duration * 4;
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
                const chrom = Scale.get("C chromatic").notes; // get list of all twelve notes
                if (this.key === "" || (++this.sinceKeyChange % this.changeKeyEvery) === 0) {
                    // new random key
                    this.sinceKeyChange = 0;
                    this.key = chrom[Math.floor(Math.random()*chrom.length)];
                }
                const [posOff, cadence] = this.playCadence(this.key, this.cadenceType, 0, this.duration);
                this.roundDuration = this.playDegree(this.key, this.degree, true, posOff, cadence);

                this.startTime = new Date().getTime();
                this.timeoutRef = setTimeout(this.doRepeat, this.roundDuration * 1000);
                this.updateProgress();
            },
            doRepeat: function() {
                this.played = [];
                if (this.playing) this.playRound();
            },
            updateProgress: function () {
                if (this.playing) {
                    const passed = new Date().getTime() - this.startTime;
                    this.progress = passed / this.roundDuration / 10;
                    this.progressRef = setTimeout(this.updateProgress, 100);
                } else {
                    this.progress = 0;
                }
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