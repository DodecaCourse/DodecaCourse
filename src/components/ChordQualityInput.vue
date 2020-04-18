<template>
  <div class="chord-quality">
    <v-btn
      v-for="c in chordTypes"
      v-show="c.enabled"
      :key="c.display"
      class="mr-1 my-1"
      :class="'normal-btn ' + c.addClass"
      :color="c.enabled ? 'primary' : 'secondary'"
      :disabled="!c.enabled"
      :elevation="1"
      small
      @click="submitBtn(c)"
    >
      {{ c.display }}
    </v-btn>
  </div>
</template>

<script>
// import { Note } from "@tonaljs/tonal";
export default {
  name: "ChordQualityInput",

  props: {
    submitSolution: {
      type: Function,
      required: true,
    },
    enabledQualities: {
      type: Array,
      required: true,
    }
  },

  data: function() {
    return {
      chordTypes: [
        { name: "maj", display: "Major", enabled: true, addClass: ""},
        { name: "min", display: "Minor", enabled: true, addClass: ""},
        { name: "dim", display: "Dim", enabled: true, addClass: ""},
        { name: "aug", display: "Aug", enabled: true, addClass: ""},
        { name: "maj7", display: "Maj 7th", enabled: true, addClass: ""},
        { name: "min7", display: "Min 7th", enabled: true, addClass: ""},
        { name: "dom7", display: "Dom 7th", enabled: true, addClass: ""},
        { name: "dim7", display: "Dim 7th", enabled: true, addClass: ""},
        { name: "min7b5", display: "Min 7b5", enabled: true, addClass: ""},
      ],
    };
  },

  computed: {},

  watch: {
    enabledQualities: function (newVal) {
      for (let l=0; l<this.chordTypes.length; l++) {
        this.chordTypes[l].enabled = newVal.indexOf(this.chordTypes[l].name) > -1;
      }
    }
  },

  mounted: function () {
    for (let l=0; l<this.chordTypes.length; l++) {
      this.chordTypes[l].enabled = this.enabledQualities.indexOf(this.chordTypes[l].name) > -1;
    }
  },

  methods: {
    //triggers when the indexth btn is clicked
    submitBtn: function(quality) {
      const [correct, solution] = this.submitSolution(quality.name);
      const self = this;
      const correctionTime = 500;
      if (correct) {
        quality.addClass = "correct-background";
        setTimeout(function () {
          quality.addClass = "";
        }, correctionTime);
      } else {
        quality.addClass = "incorrect-background";
        setTimeout(function () {
          quality.addClass = "";
        }, correctionTime);
        for (let i=0; i<solution.length; i++) {
          const c = i;
          if (i === 0) {
            this.getChordType(solution[c]).addClass = "correct-background";
          } else {
            setTimeout(function() {
              self.getChordType(solution[c]).addClass = "correct-background";
            }, correctionTime * i + 10 * (i-1));
          }
          setTimeout(function () {
            self.getChordType(solution[c]).addClass = "";
          }, correctionTime * (i + 1) + 10 + i);
        }
      }
    },
    getChordType: function (name) {
      for (let i=0; i<this.chordTypes.length; i++) {
        if (name === this.chordTypes[i].name) return this.chordTypes[i];
      }
      console.warn("not found:", name);
    },
  }
};
</script>

<style scoped lang="sass">
    //standard template for the btns
    .normal-btn
        transition: background-color 0.35s linear
    .normal-btn:not(.v-btn--text):not(.v-btn--outlined):focus::before
        opacity: 0

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

    button.correct-background
        background-color: #7cd2b6 !important

    button.incorrect-background
        background-color: #d28681 !important
</style>
