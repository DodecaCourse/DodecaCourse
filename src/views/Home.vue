<template>
  <div id="app">
    <Courses v-bind:courses="courses"/>
  </div>
</template>

<script>
  /* global MIDI */
  // Imports
  import Courses from "../components/Courses";

  export default {
    name: 'Home',
    components: {
      Courses,
    },
    data: function () {
      return {
        courses: [
          {
            id: 0,
            title: "Tonics",
            completed: false
          },
          {
            id: 1,
            title: "Individual notes",
            completed: false
          },
          {
            id: 2,
            title: "Melodies",
            completed: false
          },
          {
            id: 3,
            title: "Chords",
            completed: false
          }

        ]
      }
    }
  }


  window.onload = function () {
    MIDI.loadPlugin({
      soundfontUrl: "https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/",
      instrument: "acoustic_grand_piano",
      onprogress: function (state, progress) {
        console.log(state, progress);
      },
      onsuccess: function () {
        var delay = 0; // play one note every quarter second
        var note = 66; // the MIDI note
        var velocity = 127; // how hard the note hits
        // play the note
        MIDI.setVolume(0, 127);
        MIDI.noteOn(0, note, velocity, delay);
        MIDI.noteOff(0, note, delay + 0.75);
        MIDI.noteOn(0, note + 7, velocity, delay + 0.75);
        MIDI.noteOff(0, note + 7, delay + 2 * 0.75);
      }
    });
  };
</script>


