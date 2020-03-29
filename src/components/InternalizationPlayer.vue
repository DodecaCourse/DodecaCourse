<template>
    <div>
        <p class="play-button noselect" v-on:click="playing = !playing">
          <i v-bind:class="{'fas fa-play':!this.playing, 'fas fa-pause': this.playing}"></i> {{progression}}
          <i>Status: {{status}}</i>
        </p>
        <label v-if="fixedDegree === undefined">
            <select v-model="chosenDegree">
                <option v-for="o in degreesAvailable" v-bind:value="o.value" v-bind:key="o.key">
                    {{ o.text }}
                </option>
            </select>
        </label>
    </div>
</template>

<script>
    /* global MIDI */
    import { Progression, Chord, Note, Midi, Scale } from "@tonaljs/tonal"

    export default {
        name: "InternalizationPlayer",
        props: ['fixedDegree'],
        data: function() {
            return {
                playing: false,
                status: 'Not loaded',
                tempoBPM: 80,
                progression: ["CMaj7", "Dm7", "G7", "CMaj7"],
                key: "",
                sinceKeyChange: 0,
                changeKeyEvery: 8,
                timeoutRef: null,
                degreesAvailable: [
                    {text: 'Tonic', value: '1P', key: 0},
                    {text: 'Second', value: '2M', key: 1},
                    {text: 'Major Third', value: '3M', key: 2},
                ],
                chosenDegree: "1P",
                played: [],
            };
        },
        computed: {
            duration: function () { return 60 / this.tempoBPM },
            degree: function () {
                return this.fixedDegree !== undefined ? this.fixedDegree : this.chosenDegree;
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
                const chrom = Scale.get("C chromatic").notes;
                if (this.key === "" || (++this.sinceKeyChange % this.changeKeyEvery) === 0) {
                    this.sinceKeyChange = 0;
                    this.key = chrom[Math.floor(Math.random()*chrom.length)];
                }
                this.progression =  Progression.fromRomanNumerals(this.key, ["I", "IIm7", "V7", "I"]);
                let posOff = this.playCadence(this.key, this.progression, 0, this.duration);
                let dur = this.playDegree(this.key, this.degree, true, posOff);
                this.timeoutRef = setTimeout(this.doRepeat, dur * 1000);
            },
            doRepeat: function() {
                this.played = [];
                if (this.playing) this.playRound();
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
                },
                onsuccess: function () {
                    self.status = "Loaded";
                }
            });
        },
        destroyed: function stopAudio() {
            clearTimeout(this.timeoutRef);
            MIDI.stopAllNotes();
        }
    };

</script>

<style scoped>
  .play-button {
    background: #f4f4f4;
    padding: 10px;
    border-bottom: 1px #ccc dotted;
    border-top: 1px #ccc dotted;
    cursor: pointer;
  }

</style>
