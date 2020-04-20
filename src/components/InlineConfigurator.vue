<!--
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz, Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
-->
<template>
  <v-card
    class="d-flex flex-wrap px-1 align-center justify-center"
    elevation="2"
  >
    <b class="mx-1"><slot />:</b>
    <DegreeCirclePictogram
      v-show="enabledDegrees !== undefined"
      :enabled-degrees="enabledDegrees"
    />
    <div>
      <v-btn
        v-for="(lvl, i) in levels"
        v-show="levels > 1"
        :key="i + 1"
        :class="{
          'finished': takes[progId] !== undefined &&
            takes[progId][i+1] !== undefined && takes[progId][i+1].completed,
          'mx-1': i === 0,
          'mr-1': i > 0,
          'dark': $vuetify.theme.dark
        }"
        :color="level === i + 1 ? 'primary' : 'secondary'"
        fab
        x-small
        depressed
        class="level"
        @click="level = i + 1"
      >
        {{ i + 1 }}
      </v-btn>
    </div>
    <div>
      <v-btn
        v-if="!hidePractice"
        class="ma-1"
        color="primary"
        small
        elevation="1"
        @click="onPractice"
      >
        Practice
      </v-btn>
      <v-btn
        v-if="!hideTest"
        class="ma-1"
        color="ternary"
        small
        elevation="1"
        @click="onTest"
      >
        Test
      </v-btn>
      <v-btn
        v-if="!hideTest && user != null"
        title="Mark as completed"
        icon
        :style="completed ? 'color: green' : ''"
        @click="completed = !completed"
      >
        <v-icon>{{ completed ? 'mdi-check-circle' : 'mdi-check-circle-outline' }}</v-icon>
      </v-btn>
    </div>
  </v-card>
</template>

<script>
import DegreeCirclePictogram from "./DegreeCirclePictogram";
import api from "../api";

const INTERNALIZATION = 0;
const RECOGNITION_SINGLE = 1;
const RECOGNITION_INTERVAL = 2;
const TARGET_TONE = 3;
const CHORD_QUALITY = 4;
const CHORD_INTERNALIZATION = 5;
const CHORD_RECOGNITION = 6;

export default {
  name: "InlineConfigurator",
  components: {DegreeCirclePictogram},
  mixins: [api],
  props: {
    tType: {
      type: String,
      required: true
    },
    config: {
      type: Object,
      required: true
    },
    progId: {
      type: Number,
      required: true,
    },
    hideTest: {
      type: Boolean,
    },
    hidePractice: {
      type: Boolean,
    },
    scale: {
      type: String,
      default: "ionian"
    },
  },
  data: function () {
    return {
      level: 1,
    };
  },
  computed: {
    target: function () {
      for (let i=0;i<this.targets.length;i++)
        if (this.targets[i].id === this.progId) return this.targets[i];
      return undefined;
    },
    type: function () {
      // defaults to INTERNALIZATION
      if (this.tType === "internalization") return INTERNALIZATION;
      else if (this.tType === "recognition-single") return RECOGNITION_SINGLE;
      else if (this.tType === "recognition-interval") return RECOGNITION_INTERVAL;
      else if (this.tType === "target-tone") return TARGET_TONE;
      else if (this.tType === "chord-quality") return CHORD_QUALITY;
      else if (this.tType === "chord-internalization") return CHORD_INTERNALIZATION;
      else if (this.tType === "chord-recognition") return CHORD_RECOGNITION;
      else return INTERNALIZATION;
    },
    levels: function () {
      return this.target.levels;
    },
    enabledDegrees: function () {
      if (this.type === INTERNALIZATION) {
        return [this.config.degree];
      } else if (this.type === RECOGNITION_SINGLE) {
        return this.config.degrees;
      } else if (this.type === RECOGNITION_INTERVAL) {
        return this.config.degrees;
      } else {
        return this.config.degrees || [0, 2, 4, 5, 7, 9, 11];
      }
    },
    completed: {
      get: function () {
        return this.takes[this.progId] !== undefined &&
                        this.takes[this.progId][this.level] !== undefined &&
                        this.takes[this.progId][this.level].completed;
      },
      set: function (completed) {
        this.setCompleted(this.level, completed);
      }
    },
  },
  watch: {
    takes: function (newval, oldval) {
      if (newval != null) {
        if (Object.keys(oldval).length === 0 && oldval.constructor === Object)
          this.setLevelByTakes();
      }
    },
  },
  created: function () {
    this.setLevelByTakes();
  },
  methods: {
    onPractice: function () {
      this.$teacher.setConfigurator(this);
      if (this.type === INTERNALIZATION) {
        this.$teacher.setupInternalization(this.config.degree, true, this.level, this.scale);
      } else if (this.type === RECOGNITION_SINGLE) {
        this.$teacher.setupRecognitionSingle(this.config.degrees, true, this.level, this.scale);
      } else if (this.type === RECOGNITION_INTERVAL) {
        this.$teacher.setupRecognitionInterval(this.config.degrees, this.config.intervals,
          true, this.level, this.scale);
      } else if (this.type === TARGET_TONE) {
        this.$teacher.setupTargetTone(this.config.chordTypes, true, this.level, this.scale);
      } else if (this.type === CHORD_QUALITY) {
        this.$teacher.setupChordQuality(this.config.chordTypes, true, this.level, this.scale);
      } else if (this.type === CHORD_INTERNALIZATION) {
        this.$teacher.setupChordInternalization(this.config.diatonic, this.config.degrees, this.config.count, true, this.level, this.scale);
      } else if (this.type === CHORD_RECOGNITION) {
        this.$teacher.setupChordRecognition(this.config.diatonics, this.config.degrees, this.config.count, true, this.level, this.scale);
      }
    },
    onTest: function () {
      this.$teacher.setConfigurator(this);
      if (this.type === INTERNALIZATION) {
        this.$teacher.setupInternalizationTest(this.config.degree, true, this.level, this.scale);
      } else if (this.type === RECOGNITION_SINGLE) {
        this.$teacher.setupRecognitionSingleTest(this.config.degrees, true, this.level, this.scale);
      } else if (this.type === RECOGNITION_INTERVAL) {
        this.$teacher.setupRecognitionIntervalTest(this.config.degrees, this.config.intervals,
          true, this.level, this.scale);
      } else if (this.type === TARGET_TONE) {
        this.$teacher.setupTargetToneTest(this.config.chordTypes, true, this.level, this.scale);
      } else if (this.type === CHORD_QUALITY) {
        this.$teacher.setupChordQualityTest(this.config.chordTypes, true, this.level, this.scale);
      } else if (this.type === CHORD_INTERNALIZATION) {
        console.error("No chord internalization test available");
      } else if (this.type === CHORD_RECOGNITION) {
        this.$teacher.setupChordRecognitionTest(this.config.diatonics, this.config.degrees, this.config.count,true, this.level, this.scale);
      }
    },
    setCompleted: function (level, completed) {
      if (this.takes[this.progId] === undefined) {
        this.takes[this.progId] = {};
      }
      if (this.takes[this.progId][level] === undefined) {
        this.takes[this.progId][level] = {
          completed: false
        };
      }
      this.takes[this.progId][level].completed = completed;
      // update backend
      const self = this;
      if (this.takes[this.progId][level].completed) {
        this.completeTarget(this.progId, level)
          .then(self.updateTakes);
      } else {
        this.unsetCompleteTarget(this.progId, level)
          .then(self.updateTakes);
      }
    },
    setLevelByTakes: function () {
      for (let i = 0; i < this.levels; i++) {
        if (this.takes[this.progId] !== undefined &&
                        this.takes[this.progId][i + 1] !== undefined &&
                        this.takes[this.progId][i + 1].completed) {
          if (this.levels >= i + 2) {
            this.level = i + 2;
          } else {
            this.level = i + 1;
          }
        }
      }
    }
  }
};
</script>

<style lang="sass" scoped>
    .level:not(.v-btn--text):not(.v-btn--outlined):focus::before
        opacity: 0

    .level.finished
        box-shadow: 0 0 9px #00a802 !important
    .level.finished.dark
        box-shadow: 0 0 9px #00ff03 !important
</style>
