<template>
  <!-- below is the code which generates an easy to use interface for changing root note and mode by hand
       if you want to use it you will have to cut and paste the div containing the circle into the 
       marked area in the v-container-->
  <!--
  <v-container>

    below is the code which generates an easy to use interface for changing root note and mode by hand

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
            <option value="b"><b>&flat;</b> (flat)</option>
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
          <b>Mode: {{ this.mode }}</b></v-chip
        >
      </v-col>

      <v-col>
        <v-card
          class="d-inline-flex px-1 align-start justify-center"
          elevation="5"
          width="100%"
        >
          <div v-for="(modus) in this.modes" v-bind:key="modus">
            <v-btn
              rounded
              :color="mode == modus.name ? 'primary' : 'secondary'"
              v-on:click="changeMode(modus)"
              dark
              >{{ modus.numeral }}</v-btn
            >
          </div>
        </v-card>
      </v-col>
    </v-row>


    <v-row>
      <v-col>

          INSERT DIV FOR CIRCLE HERE

      </v-col>
    </v-row>
  </v-container>
-->
  <div class="div-circle">
    <div ref="background" id="background-circle" />
    <v-btn
      v-for="i in this.degrees"
      v-bind:key="i.display"
      :class="'normal-btn normal-btn--' + (i.degree + 1)"
      :color="i.enabled ? 'primary' : 'secondary'"
      :disabled="!i.enabled"
      x-small
      fab
      :elevation="i.degree === 0 ? 5 : 2"
      v-on:click="noteBt(i)"
      :ripple="i.degree === solution ? {class: 'green--text' } : { class: 'red--text' }"
      >{{ i.display }}</v-btn>
    <div id="progress-content">
      <slot name="progress"></slot>
    </div>
    <div id="inner-content">
      <slot name="playbtn"></slot>
    </div>
    <div id="inner-text" :style="'color: ' + $vuetify.theme.currentTheme.primary">
      <slot name="text"></slot>
    </div>
  </div>
</template>

<script>
// import { Note } from "@tonaljs/tonal";
export default {
  name: "DegreeCircle",

  props: {
    submitSolution: {
      type: Function,
      required: true,
    },
    solution: {
      type: Number,
      required: true,
    },
    enabledDegrees: {
      type: Array,
      required: true,
    }
  },

  data: function() {
    return {
      //standard mode and root, rootMod is for handling a flat and a sharp note, so
      //they can be chosen separately from the base note
      mode: "Major/Ionian",
      root: "C",
      rootMod: "",

      //button which was clicked last, 1P by default
      lastClicked: 0,

      //var to save on which octave the tone is
      octave: 4,

      //database for modes, saves their names and where their respective halfsteps lie
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

      //database for the intervals/degrees, "name" chosen to fit TonalJS, display is the name of
      //Solfege and shown on btns
      degrees: [
        { degree: 0, name: "1P", display: "Do", enabled: true },
        { degree: 1, name: "2m", display: "Ra", enabled: true },
        { degree: 2, name: "2M", display: "Re", enabled: true },
        { degree: 3, name: "3m", display: "Ma", enabled: true },
        { degree: 4, name: "3M", display: "Mi", enabled: true },
        { degree: 5, name: "4P", display: "Fa", enabled: true },
        { degree: 6, name: "4A", display: "Fi", enabled: true },
        { degree: 7, name: "5P", display: "So", enabled: true },
        { degree: 8, name: "6m", display: "Le", enabled: true },
        { degree: 9, name: "6M", display: "La", enabled: true },
        { degree: 10, name: "7m", display: "Ta", enabled: true },
        { degree: 11, name: "7M", display: "Ti", enabled: true }
      ],

      //base notes, like the white tiles to get the root system running
      bases: ["C", "D", "E", "F", "G", "A", "B"],

      // contains enabled degrees of mode
      modeEnabled: [],
      useMode: false,
    };
  },

  computed: {},

  watch: {
    modeEnabled: function (newVal) {
      if (this.useMode) {
        for (let l=0; l<this.degrees.length; l++) {
          this.degrees[l].enabled = newVal.indexOf(this.degrees[l].degree) > -1
        }
      }
    },
    enabledDegrees: function (newVal) {
      for (let l=0; l<this.degrees.length; l++) {
        this.degrees[l].enabled = newVal.indexOf(this.degrees[l].degree) > -1
      }
    }
  },

  methods: {
    //returns full root note
    getRoot: function() {
      return this.root + this.rootMod;
    },

    //for changing the mode
    //is unused when mode interface is unused
    changeMode: function(mode) {
      this.mode = mode.name;
      this.setEnabledMode(mode);
    },

    //handles the enabled buttons according to the new mode using the mode's halfsteps
    setEnabledMode: function(mode) {
      let newEnabled = [];
      let i = 0;
      while (i < this.enabled.length) {
        newEnabled.push(this.degrees[i].degree);
        if (i === mode.halfsteps.first || i === mode.halfsteps.second) {
          i++;
        } else {
          i = i + 2;
        }
      }
      this.modeEnabled = newEnabled;
    },

    //triggers when the indexth btn is clicked
    noteBt: function(index) {
      //index ist vom typ "interval" -> Solfege Bez.: index.display
      //                                Intervallname: index.name (also zB 3m, wie TonalsJS es auch benutzt)
      //
      //wenn man die Eingabe des Users speichern will sollte das dann denke ich hier passieren, ich habe auch
      //schonmal eine Variable "lastClicked" (s.o.) erstellt, weiß nicht ob die hilfreich ist aber die könnte
      //man ja dann hier ändern oder so
      // let result = Note.transpose(this.getRoot(), index.name);
      console.log(this.$refs.background);
      this.$refs.background.style.backgroundColor = this.solution === index.degree ?"green" : "red";
      this.$refs.background.className = "fade-in-out";
      const self = this;
      setTimeout(function () {self.$refs.background.className = ""}, 700);
      this.submitSolution(index.degree);
    }
  }
};
</script>

<style scoped lang="sass">
    @use "sass:math"
    @use "sass:list"

    //parameters for the DegreeCircles' position and size
    $radius: 62
    $btnrad: 32
    $centerX: $radius
    $centerY: $radius

    $backgroundMargin: 5

    //math values for computing the respective positions of the btns
    $sin: 0, 0.5, 0.866, 1, 0.866, 0.5, 0, -0.5, -0.866, -1, -0.866, -0.5
    $cos: 1, 0.866, 0.5, 0, -0.5, -0.866, -1, -0.866, -0.5, 0, 0.5, 0.866

    //because I was stupid
    $indices: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

    //instanciates each individual btn with its position
    @each $i in $indices
      .normal-btn--#{$i}
        left: math.floor(nth($sin, $i) * $radius + $centerX) * 1px
        top: math.floor(-1 * nth($cos, $i) * $radius + $centerY) * 1px

    #inner-content
      position: absolute
      left: math.floor(nth($sin, 12) * $radius + $centerX) * 1.3px
      top: math.floor(-1 * nth($cos, 11) * $radius + $centerY) * 1.3px
      width: $radius * 1.2px
      height: $radius * 1.2px
      display: flex

    #inner-content *
      justify-self: center
      align-self: center
      margin-left: auto
      margin-right: auto

    #progress-content
      position: absolute
      left: $btnrad * 1px + 1px
      top: $btnrad * 1px + 1px

    #inner-text
      position: absolute
      left: $btnrad * 1.8px
      bottom: $btnrad * 1px
      right: $btnrad * 1.8px
      top: $btnrad * 3px
      text-align: center

    #background-circle
      position: absolute
      left: $btnrad * 1px + 1px * $backgroundMargin
      top: $btnrad * 1px + 1px * $backgroundMargin
      width: 2px * $radius - 1px * $btnrad - 2px * $backgroundMargin
      height: 2px * $radius - 1px * $btnrad - 2px * $backgroundMargin
      border-radius: 1px * $radius - 0.5px * $btnrad  - 1px * $backgroundMargin
      background-color: green
      opacity: 0

 //standard template for the btns
.normal-btn
  text-transform: none !important
  position: absolute

  //class which contains the DegreeCircle
.div-circle
  position: relative
  width: 2px * $radius + 1px * $btnrad
  height: 2px * $radius + 1px * $btnrad

  .red--text
    color: lightcoral

  .green--text
    color: lightgreen

  .fade-in-out
    opacity: 1
    animation-name: fadeInOutOpacity
    animation-iteration-count: 1
    animation-timing-function: ease-in-out
    animation-duration: 0.7s

  @keyframes fadeInOutOpacity
    0%
      opacity: 0
    50%
      opacity: 0.2
    100%
      opacity: 0
</style>
