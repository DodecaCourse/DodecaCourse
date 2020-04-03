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
          <div v-for="degree in this.degrees" v-bind:key="degree">
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
        { name: "Major/Ionian", numeral: "I" },
        { name: "Dorian", numeral: "II" },
        { name: "Phrygian", numeral: "III" },
        { name: "Lydian", numeral: "IV" },
        { name: "Mixolydian", numeral: "V" },
        { name: "Minor/Aeolian", numeral: "VI" },
        { name: "Locrian", numeral: "VII" }
      ],

      degrees: [1, 2, 3, 4, 5, 6, 7]
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
    }
  }
};
</script>

<style scoped></style>