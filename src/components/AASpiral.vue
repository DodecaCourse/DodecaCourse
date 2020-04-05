<template>
  <v-container>
    <v-row align="start">
      <v-col align="center" md="sm">
        <v-chip>
          <b>Mode: {{ this.scale }}</b></v-chip
        >
      </v-col>
      <v-col>
        <v-card
          class="d-inline-flex px-1 align-start justify-center"
          elevation="5"
          width="100%"
        >
          <div v-for="(mode, i) in this.modes" v-bind:key="i">
            <v-btn rounded color="primary" v-on:click="changeMode(mode)" dark>{{
              mode.numeral
            }}</v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card
          class="d-inline-flex px-1 align-center justify-center"
          elevation="5"
          width="100%"
        >
          <div v-for="i in this.intervals" v-bind:key="i">
            <v-btn
              color="blue"
              :disabled="!isEnabled(i.halfsteps)"
              small
              fab
              elevation="1"
              v-on:click="noteBt(i)"
              >{{ i.name }}</v-btn
            >
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AASpiral",

  data: function() {
    return {
      scale: "Major/Ionian",
      root: { base: "C", flattened: false, sharpened: false },

      octave: 0,

      modes: [
        {
          name: "Major/Ionian",
          numeral: "I",
          halfsteps: { first: 4, second: 11 }
        },
        { name: "Dorian", numeral: "II", halfsteps: { first: 2, second: 9 } },
        {
          name: "Phrygian",
          numeral: "III",
          halfsteps: { first: 0, second: 7 }
        },
        { name: "Lydian", numeral: "IV", halfsteps: { first: 6, second: 11 } },
        {
          name: "Mixolydian",
          numeral: "V",
          halfsteps: { first: 4, second: 9 }
        },
        {
          name: "Minor/Aeolian",
          numeral: "VI",
          halfsteps: { first: 2, second: 7 }
        },
        { name: "Locrian", numeral: "VII", halfsteps: { first: 0, second: 5 } }
      ],

      intervals: [
        { halfsteps: 0, name: "P1" },
        { halfsteps: 1, name: "b2" },
        { halfsteps: 2, name: "M2" },
        { halfsteps: 3, name: "b3" },
        { halfsteps: 4, name: "M3" },
        { halfsteps: 5, name: "P4" },
        { halfsteps: 6, name: "A4" },
        { halfsteps: 7, name: "P5" },
        { halfsteps: 8, name: "b6" },
        { halfsteps: 9, name: "M6" },
        { halfsteps: 10, name: "b7" },
        { halfsteps: 11, name: "M7" },
        { halfsteps: 12, name: "P8" }
      ],

      notes: [
        { base: "C", flattened: true, sharpened: false },
        { base: "C", flattened: false, sharpened: false },
        { base: "C", flattened: false, sharpened: true },

        { base: "D", flattened: true, sharpened: false },
        { base: "D", flattened: false, sharpened: false },
        { base: "D", flattened: false, sharpened: true },

        { base: "E", flattened: true, sharpened: false },
        { base: "E", flattened: false, sharpened: false },
        { base: "E", flattened: false, sharpened: true },

        { base: "F", flattened: true, sharpened: false },
        { base: "F", flattened: false, sharpened: false },
        { base: "F", flattened: false, sharpened: true },

        { base: "G", flattened: true, sharpened: false },
        { base: "G", flattened: false, sharpened: false },
        { base: "G", flattened: false, sharpened: true },

        { base: "A", flattened: true, sharpened: false },
        { base: "A", flattened: false, sharpened: false },
        { base: "A", flattened: false, sharpened: true },

        { base: "B", flattened: true, sharpened: false },
        { base: "B", flattened: false, sharpened: false },
        { base: "B", flattened: false, sharpened: true }
      ],

      bases: ["C", "D", "E", "F", "G", "A", "B"],

      enabled: [
        true,
        false,
        true,
        false,
        true,
        true,
        false,
        true,
        false,
        true,
        false,
        true,
        true
      ]
    };
  },

  computed: {},

  watch: {},

  methods: {
    changeMode: function(mode) {
      this.scale = mode.name;
      this.changeEnabled(mode);
    },

    changeEnabled: function(mode) {
      let i;
      for (i = 0; i < this.enabled.length; i++) {
        this.enabled[i] = false;
      }
      i = 0;
      while (i < this.enabled.length) {
        this.enabled[i] = true;
        if (i == mode.halfsteps.first || i == mode.halfsteps.second) {
          i++;
        } else {
          i = i + 2;
        }
      }
    },

    isEnabled: function(i) {
      return this.enabled[i];
    },

    playDegree: function(scale, root, degree, octave) {
      const note = degree + 7 * octave;
      window.alert(root + " " + scale + " " + note);
    },

    noteBt: function(interval) {
      this.playDegree(this.scale, this.root, interval, this.octave);
    },

    addInterval: function(note, interval) {
      if (interval.halfsteps < 5) {
        return 0;
      }
    },

    getNoteString: function(note) {
      if (note.flattened) {
        return note.base + "b";
      } else if (note.sharpened) {
        return note.base + "#";
      }
      return note.base;
    }
  }
};
</script>

<style scoped></style>
