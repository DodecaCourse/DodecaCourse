<template>

  <div>
    <p class="play-button noselect" v-on:click="playing = !playing">
      <i v-bind:class="{'fas fa-play':!this.playing, 'fas fa-pause': this.playing}"></i> Play Cadence {{progression}}
      <i>Status: {{status}}</i>
    </p>
  </div>


</template>

<script>

  /* global MIDI */
  import { Progression, Chord, Note, Midi } from '@tonaljs/tonal'

  export default {
    name: 'InternalizationPlayer',
    data: function() {
      return {
        playing: false,
        status: 'Not loaded',
        tempoBPM: 120,
        progression: ['CMaj7', 'Dm7', 'G7', 'CMaj7']
      }
    },
    watch: {
      playing: function(val) {
        let key = 'D';
        this.progression = Progression.fromRomanNumerals(key, ['I', 'IIm7', 'V7', 'I']);
        if (val) {
          this.playCadence(key, this.progression, 0);
          this.playDegree(key, '3m', true, 4);
          //this.playMidi("../assets/fruehlingsrauschen.mid");
          this.playing == false;
        }
      }
    },
    methods: {
      playMidi: function(url) {
        MIDI.Player.loadFile(url, MIDI.Player.start);
        MIDI.Player.start();
      },
      playCadence: function(key, progr, posOff) {
        for (let chordNum = 0; chordNum < progr.length; chordNum++) {
          const chord = Chord.get(progr[chordNum]);
          console.log(chord);
          const root = chord.tonic + '4';
          for (let i = 0; i < chord.intervals.length; i++) {
            let note = Midi.toMidi(Note.transpose(root, chord.intervals[i]))
            console.log(note);
            if (i >= 2 && chordNum > 1) {
              note -= 12
            }
            var duration = 1;
            var delay = posOff + chordNum * duration // play one note every quarter second
            var velocity = 110 // how hard the note hits
            // play the note
            MIDI.setVolume(0, 127)
            MIDI.noteOn(0, note, velocity, delay)
            MIDI.noteOff(0, note, delay + duration)

            if (i === 0) {
              MIDI.setVolume(0, 127)
              MIDI.noteOn(0, note - 12, velocity, delay)
              MIDI.noteOff(0, note - 12, delay + duration)
            }
          }
        }
      },
      playDegree: function(key, degree, withChord, posOff) {
        const root = key + '4'
        const note = Midi.toMidi(Note.transpose(root, degree))
        if (withChord) {
          this.playCadence(key, Progression.fromRomanNumerals(key, ['I']), posOff)
        }
        var duration = 2
        var delay = posOff // play one note every quarter second
        var velocity = 127 // how hard the note hits
        MIDI.setVolume(0, 127)
        MIDI.noteOn(0, note, velocity, delay)
        MIDI.noteOff(0, note, delay + duration)
        MIDI.noteOn(0, note - 12, velocity, delay)
        MIDI.noteOff(0, note - 12, delay + duration)
        MIDI.noteOn(0, note + 12, velocity, delay)
        MIDI.noteOff(0, note + 12, delay + duration)
      }
    },
    created: function initAudio() {
      var self = this
      MIDI.loadPlugin({
        soundfontUrl: 'https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/',
        instrument: 'acoustic_grand_piano',
        onprogress: function(state, progress) {
          self.status = 'Loading...' + Math.floor(progress * 100) + '%'
          console.log(state, progress)
        },
        onsuccess: function() {
          self.status = 'Loaded'
        }
      })
    }
  }

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
