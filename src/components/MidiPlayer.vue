<template>

  <div>
    <p class="play-button noselect" v-on:click="playing = !playing">
      <i v-bind:class="{'fas fa-play':!this.playing, 'fas fa-pause': this.playing}"></i> <b>{{song.author}}</b> {{song.name}}
      | <i>Status: {{status}}</i>
    </p>
  </div>

</template>

<script>

  /* global MIDI */
  //import { Progression, Chord, Note, Midi, Scale } from "@tonaljs/tonal"


  export default {
    name: 'MidiPlayer',
    props: ['song'],
    data: function() {
      return {
        playing: false,
        status: 'Not loaded',
        tempoBPM: 80
      }
    },
    watch: {
      playing: function(val) {
        if (val) {
          this.play(this.song.data)
        } else {
          this.stop()
          clearTimeout(this.timeoutRef)
        }
      }
    },
    methods: {
      play: function(url) {
        if (MIDI.Player.currentTime == 0) {
          MIDI.Player.loadFile(url, MIDI.Player.start)
        } else {
          MIDI.Player.resume()
        }
      },
      stop: function() {
        MIDI.Player.pause()
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
    },
    destroyed: function stopAudio() {
      clearTimeout(this.timeoutRef)
      MIDI.stopAllNotes()
    }
  }

</script>

<style scoped>

  .play-button {
    background: #67008a;
    color: white;
    padding: 10px;
    border-bottom: 1px #aaa dotted;
    border-top: 1px #aaa dotted;
    cursor: pointer;
  }

</style>
