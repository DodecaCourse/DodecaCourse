<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="5" width="100%"
    >
        <b class="mr-3 hidden-sm-and-down">Play I-IV-V-I:</b>
        <v-btn color="primary" small fab elevation="1" v-on:click="playing = !playing" :disabled="!loaded">
            <v-icon>{{ playing ? 'mdi-pause' : 'mdi-play' }}</v-icon>
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
    import { Progression, Chord, Note, Midi, Scale } from "@tonaljs/tonal"

    export default {
        name: "Teacher",
        props: ['fixedDegree','mode'],
        data: function() {
            return {
                playing: false,
                status: 'Not loaded',
                loaded: false,
                tempoBPM: 80,
                progression: ["CMaj7", "Dm7", "G7", "CMaj7"],
                key: "",
                sinceKeyChange: 0,
                changeKeyEvery: 8,
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
                    clearTimeout(this.timeoutRef);

                    this.stopAllNotes();
                }
            }
        },
        methods: {
            playCadence: function (key, progr, posOff, duration) {
                let dur = posOff;
                for (let chordNum=0; chordNum < progr.length; chordNum++) {
                    const chord = Chord.get(progr[chordNum]);
                    const root = chord.tonic + '4';
                    for (let i=0; i<chord.intervals.length; i++) {
                        let note =  Midi.toMidi(Note.transpose(root, chord.intervals[i]));
                        if (i >= 2 && chordNum > 1) {
                            note -= 12;
                        }
                        var delay = posOff + chordNum * duration; // play one note every quarter second
                        var velocity = 110; // how hard the note hits
                        // play the note
                        MIDI.setVolume(0, 127);
                        if(this.playing){
                          this.noteOn(0, note, velocity, delay);
                          this.played.push(this.noteOff(0, note, delay + duration));
                        }

                        if (i === 0) {
                            MIDI.setVolume(0, 127);
                            if(this.playing){
                              this.noteOn(0, note-12, velocity, delay);
                              this.played.push(this.noteOff(0, note-12, delay + duration));
                            }
                        }
                        if (delay + duration > dur) dur = delay + duration;
                    }
                }
                return dur;
            },
            playDegree: function (key, degree, withChord, posOff) {
                const root = key + '4';
                const note =  Midi.toMidi(Note.transpose(root, degree));
                if (withChord) {
                    this.playCadence(key, Progression.fromRomanNumerals(key, ["I"]), posOff,
                        this.duration * 4)
                }
                var delay = posOff; // play one note every quarter second
                var velocity = 127; // how hard the note hits
                MIDI.setVolume(0, 127);
                if(this.playing){
                  this.noteOn(0, note, velocity, delay);
                  this.played.push(this.noteOff(0, note, delay + this.duration * 4));
                }
                if(this.playing){
                  this.noteOn(0, note-12, velocity, delay);
                  this.played.push(this.noteOff(0, note-12, delay + this.duration * 4));
                }
                if(this.playing){
                  this.noteOn(0, note+12, velocity, delay);
                  this.played.push(this.noteOff(0, note+12, delay + this.duration * 4));
                }
                return delay + this.duration * 4;
            },
            playRound: function() {
                // update key
                const chrom = Scale.get("C chromatic").notes;
                if (this.key === "" || (++this.sinceKeyChange % this.changeKeyEvery) === 0) {
                    this.sinceKeyChange = 0;
                    this.key = chrom[Math.floor(Math.random() * chrom.length)];
                }
                // establish a tonic
                this.progression = Progression.fromRomanNumerals(this.key, ["I", "IIm7", "V7", "I"]);
                let posOff = this.playCadence(this.key, this.progression, 0, this.duration);

                if (this.mode === 'internalize') {
                    this.roundDuration = this.playDegree(this.key, this.degree, true, posOff);


                } else if (this.mode === 'test') {
                    this.roundDuration = this.playDegree(this.key, this.degree, false, posOff);
                }
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
                    console.log(this.progress);
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
            clearTimeout(this.timeoutRef);
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