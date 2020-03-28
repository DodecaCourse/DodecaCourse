<template>

  <p class="play-button noselect" v-on:click="clickPlayer"><i class="fas fa-play"></i> Play Sound</p>
  <!--<p class="play-button noselect" v-on:click="clickSinding"><i class="fas fa-play"></i> Sinding - Rustles of Spring Op-32 No-3</p>-->

</template>

<script>

  /* global MIDI */
  export default {
    name: 'InternalizationPlayer',
    methods: {
      clickPlayer: function() {
        MIDI.loadPlugin({
          soundfontUrl: 'https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/',
          instrument: 'acoustic_grand_piano',
          onprogress: function(state, progress) {
            console.log(state, progress)
          },
          onsuccess: function() {
            var delay = 0 // play one note every quarter second
            var note = 66 // the MIDI note
            var velocity = 127 // how hard the note hits
            // play the note
            MIDI.setVolume(0, 127)
            MIDI.noteOn(0, note, velocity, delay)
            MIDI.noteOff(0, note, delay + 0.75)
            MIDI.noteOn(0, note + 7, velocity, delay + 0.75)
            MIDI.noteOff(0, note + 7, delay + 2 * 0.75)
          }
        })
      }
      // clickSinding: function() {
      //     MIDI.loadPlugin({
      //       soundfontUrl: "https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/",
      //       instrument: "acoustic_grand_piano",
      //       onprogress: function (state, progress) {
      //           console.log(state, progress);
      //       },
      //       onsuccess: function () {
      //
      //
      //       }
      //     });
      //     function onsuccess(){
      //       MIDI.Player.start();
      //     }
      //     // Sinding - Rustles of Spring Op-32 No-3
      //     MIDI.Player.loadFile("../assets/fruehlingsrauschen.mid", onsuccess);
      //     //MIDI.Player.start();
      //
      // }
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
