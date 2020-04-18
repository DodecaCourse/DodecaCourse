<template>
  <div class="div-circle">
    <v-btn
      v-for="btn in buttons"
      :key="btn.index"
      :class="'normal-btn normal-btn--' + (btn.index + 1) + ' ' + btn.addClass"
      :disabled="!btn.enabled || !loaded"
      medium
      fab
      :elevation="btn.index === 0 ? 5 : 2"
      :color="btn.enabled ? 'primary' : 'secondary'"
      @click="onClick(btn)"
    >
      {{ labels[btn.index] }}
    </v-btn>
    <div id="inner-content">
      <slot name="content" />
    </div>
  </div>
</template>

<script>
/* global MIDI */
export default {
  name: "LandingCircle",

  props: {
    enabledButtons: {
      type: Array,
      required: true,
    },
    labels: {
      type: Array,
      required: true,
    },
  },

  data: function() {
    return {
      loaded: false,
      buttons: [
        { index: 0, enabled: false, addClass: ""},
        { index: 1, enabled: false, addClass: ""},
        { index: 2, enabled: false, addClass: ""},
        { index: 3, enabled: false, addClass: ""},
        { index: 4, enabled: false, addClass: ""},
        { index: 5, enabled: false, addClass: ""},
        { index: 6, enabled: false, addClass: ""},
        { index: 7, enabled: false, addClass: ""},
        { index: 8, enabled: false, addClass: ""},
        { index: 9, enabled: false, addClass: ""},
        { index: 10, enabled: false, addClass: ""},
        { index: 11, enabled: false, addClass: ""}
      ],
    };
  },

  watch: {
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
  created: function initAudio() {
    // Initialize MIDI
    if (typeof MIDI !== "undefined") {
      this.loadMIDI();
    } else {
      window.onload = this.loadMIDI;
    }
  },

  methods: {
    //triggers when the indexth button is clicked
    onClick: function(button) {
      console.log(button);
      if (this.loaded) {
        MIDI.noteOn(0, 60 + button.index, 127, 0);
        MIDI.noteOff(0, 60 + button.index, 0.5);
      }
    },
    loadMIDI: function () {
      const self = this;
      MIDI.loadPlugin({
        soundfontUrl: "/soundfont/",
        instrument: "acoustic_grand_piano",
        onprogress: function (state, progress) {
          if(self.debug) console.log(state, progress);
        },
        onsuccess: function () {
          self.loaded = true;
        }
      });
    }
  },
};
</script>

<style scoped lang="sass">
    @use "sass:math"
    @use "sass:list"

    //parameters for the DegreeCircles' position and size
    $radius: 109
    $btnrad: 56 / 2
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
      left: $btnrad * 1.8px
      bottom: $btnrad * 2px
      right: $btnrad * 1.8px
      top: $btnrad * 2px
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
      bottom: $btnrad * 2px
      right: $btnrad * 1.8px
      top: $btnrad * 2px
      text-align: center

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
  width: 2px * $radius + 2px * $btnrad
  height: 2px * $radius + 2px * $btnrad
</style>
