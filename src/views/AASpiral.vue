<template>
  <v-container>
    <v-row align="start">
      <v-col align="center" md="sm">
        <v-chip> <b>Mode:</b></v-chip>
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
          <div v-for="degree in this.numberOfButtons" v-bind:key="degree">
            <v-btn
              color="blue"
              small
              fab
              elevation="1"
              v-on:click="noteBt(degree)"
              >{{ degree }}</v-btn
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
      root: "C",

      octave: 0,

      modes: [
        {
          name: "Major/Ionian",
          numeral: "I",
          halfsteps: { first: 3, second: 7 }
        },
        { name: "Dorian", numeral: "II", halfsteps: { first: 2, second: 6 } },
        {
          name: "Phrygian",
          numeral: "III",
          halfsteps: { first: 1, second: 5 }
        },
        { name: "Lydian", numeral: "IV", halfsteps: { first: 4, second: 7 } },
        {
          name: "Mixolydian",
          numeral: "V",
          halfsteps: { first: 3, second: 6 }
        },
        {
          name: "Minor/Aeolian",
          numeral: "VI",
          halfsteps: { first: 2, second: 5 }
        },
        { name: "Locrian", numeral: "VII", halfsteps: { first: 1, second: 4 } }
      ],

      numberOfButtons: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],

      notes: ["C", "D", "E", "F", "G", "A", "B"],

      enabled: [true, false, true, false, true, true, false, true, false, true, false, true]
    };
  },

  watch: {},

  methods: {
    playDegree: function(scale, root, degree, octave) {
      const note = degree + 7 * octave;
      window.alert(root + " " + scale + " " + note);
    },

    noteBt: function(deg) {
      this.playDegree(this.scale, this.root, deg, this.octave);
    },

    changeMode: function(mode) {
      this.scale = mode.name;
    },

    flattenNote: function (note) {
      return note + "b";
    },

    sharpenNote: function (note) {
      return note + "#";
    }
  }
};
</script>

<style scoped></style>
