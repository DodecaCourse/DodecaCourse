<template>
  <div class="div-circle">
    <div
      id="background-circle"
      :class="backgroundClass"
      :style="'backgroundColor: ' + backgroundColor"
    />
    <v-btn
      v-for="btn in buttons"
      :key="btn.index"
      :class="'normal-btn normal-btn--' + (btn.index + 1) + ' ' + btn.addClass"
      :disabled="!btn.enabled"
      x-small
      fab
      :elevation="btn.index === 0 ? 5 : 2"
      :color="btn.enabled ? 'primary' : 'secondary'"
      @click="onClick(btn)"
    >
      {{ labels[btn.index] }}
    </v-btn>
    <div id="progress-content">
      <slot name="progress" />
    </div>
    <div id="inner-content">
      <slot name="playbtn" />
    </div>
    <div
      id="inner-text"
      :style="'color: ' + $vuetify.theme.currentTheme.primary"
    >
      <slot name="text" />
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
    enabledButtons: {
      type: Array,
      required: true,
    },
    labels: {
      type: Array,
      required: true,
    }
    // tType: {
    //   type: String,
    //   required: false,
    //   default:
    // }
  },

  data: function() {
    return {
      //standard mode and root, rootMod is for handling a flat and a sharp note, so
      //they can be chosen separately from the base note
      mode: "Major/Ionian",
      root: "C",
      rootMod: "",

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

      buttons: [
        { index: 0, enabled: true, addClass: ""},
        { index: 1, enabled: true, addClass: ""},
        { index: 2, enabled: true, addClass: ""},
        { index: 3, enabled: true, addClass: ""},
        { index: 4, enabled: true, addClass: ""},
        { index: 5, enabled: true, addClass: ""},
        { index: 6, enabled: true, addClass: ""},
        { index: 7, enabled: true, addClass: ""},
        { index: 8, enabled: true, addClass: ""},
        { index: 9, enabled: true, addClass: ""},
        { index: 10, enabled: true, addClass: ""},
        { index: 11, enabled: true, addClass: ""}
      ],

      //base notes, like the white tiles to get the root system running
      bases: ["C", "D", "E", "F", "G", "A", "B"],

      backgroundClass: "",
      backgroundColor: "green",
      backgroundTimeout: undefined,

      // contains enabled buttons of mode
      modeEnabled: [],
      useMode: false,
    };
  },

  watch: {
    modeEnabled: function (newVal) {
      if (this.useMode) {
        for (let l=0; l<this.buttons.length; l++) {
          this.buttons[l].enabled = newVal.indexOf(this.buttons[l].index) > -1;
        }
      }
    },
    enabledButtons: function (newVal) {
      for (let l=0; l<this.buttons.length; l++) {
        this.buttons[l].enabled = newVal.indexOf(this.buttons[l].index) > -1;
      }
    }
  },

  mounted: function () {
    for (let l=0; l<this.buttons.length; l++) {
      this.buttons[l].enabled = this.enabledButtons.indexOf(this.buttons[l].index) > -1;
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
        newEnabled.push(this.buttons[i].index);
        if (i === mode.halfsteps.first || i === mode.halfsteps.second) {
          i++;
        } else {
          i = i + 2;
        }
      }
      this.modeEnabled = newEnabled;
    },

    //triggers when the indexth button is clicked
    onClick: function(button) {
      const [correct, solution] = this.submitSolution(button.index);
      const self = this;
      const correctionTime = 500;
      if (correct) {
        this.backgroundColor = "lightgreen";
      } else {
        this.backgroundColor = "lightcoral";
        for (let i=0; i<solution.length; i++) {
          const c = i;
          if (i === 0) {
            this.buttons[solution[c]].addClass = "correct-background";
          } else {
            setTimeout(function() {
              self.buttons[solution[c]].addClass = "correct-background";
            }, correctionTime * i + 10 * (i-1));
          }
          setTimeout(function () {
            self.buttons[solution[c]].addClass = "";
          }, correctionTime * (i + 1) + 10 + i);
        }
      }
      if (this.backgroundTimeout !== undefined) {
        clearTimeout(this.backgroundTimeout);
      }
      // fade-in-out could still be set on fast clicks -> reset and timeout
      this.backgroundClass = "";
      setTimeout(function () {self.backgroundClass = "fade-in-out";}, 50);
      this.backgroundTimeout = setTimeout(function () {self.backgroundClass = "";}, 700);
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
  transition: background-color 0.35s linear
.normal-btn:not(.v-btn--text):not(.v-btn--outlined):focus::before
  opacity: 0

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
      opacity: 0.4
    100%
      opacity: 0

  .correct-background
    background-color: #7cd2b6 !important
</style>
