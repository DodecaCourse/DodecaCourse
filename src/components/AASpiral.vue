<template>
  <v-container>
    <v-row align="start">
      <v-col align="center" cols="3">
        <v-chip
          ><b>Root: {{ getRoot() }}, Octave: {{ this.octave }}</b></v-chip
        >
      </v-col>

      <v-col align="center">
        <v-select :items="bases" v-model="root" label="Base note" dense />
      </v-col>

      <v-col>
        <v-card>
          <select v-model="rootMod" multiple>
            <option value="b">b (flat)</option>
            <option value="">(natural)</option>
            <option value="#"># (sharp)</option>
          </select>
        </v-card>
      </v-col>

      <v-col align="start">
        <v-card>
          Octave:
          <v-btn
            color="primary"
            rounded
            x-small
            fab
            elevation="1"
            v-on:click="octave++"
            ><b>+</b></v-btn
          ><v-btn
            color="primary"
            rounded
            x-small
            fab
            elevation="1"
            v-on:click="octave--"
            ><b>-</b></v-btn
          >
        </v-card>
      </v-col>
    </v-row>

    <v-row align="start">
      <v-col align="center" cols="3">
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
            <v-btn
              rounded
              :color="scale == mode.name ? 'primary' : 'secondary'"
              v-on:click="changeMode(mode)"
              dark
              >{{ mode.numeral }}</v-btn
            >
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
              :color="isEnabled(i.halfsteps) ? 'primary' : 'secondary'"
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
import { Note } from "@tonaljs/tonal";
export default {
  name: "AASpiral",

  data: function() {
    return {
      scale: "Major/Ionian",
      root: "C",
      rootMod: "",

      octave: 4,

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
        { halfsteps: 0, name: "1P" },
        { halfsteps: 1, name: "2m" },
        { halfsteps: 2, name: "2M" },
        { halfsteps: 3, name: "3m" },
        { halfsteps: 4, name: "3M" },
        { halfsteps: 5, name: "4P" },
        { halfsteps: 6, name: "4A" },
        { halfsteps: 7, name: "5P" },
        { halfsteps: 8, name: "6m" },
        { halfsteps: 9, name: "6M" },
        { halfsteps: 10, name: "7m" },
        { halfsteps: 11, name: "7M" },
        { halfsteps: 12, name: "8P" }
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
    getRoot: function() {
      return this.root + this.rootMod;
    },

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

    noteBt: function(index) {
      let result = Note.transpose(this.getRoot(), index.name);
      window.alert(result);
    }
  }
};
</script>

<style scoped></style>
