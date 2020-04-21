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
  <v-list-item
    :to="toString"
    :style="{ 'background-image': createBackgroundString() }"
  >
    <v-list-item-title>
      {{ chapter.title }}
      <v-list-item-subtitle
        v-if="displayCheck && !empty"
      >
        {{ progress.completed }} / {{ progress.total }}
      </v-list-item-subtitle>
    </v-list-item-title>

    <v-list-item-action
      v-if="displayCheck && !empty"
    >
      <v-icon>
        {{ completed ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline" }}
      </v-icon>
    </v-list-item-action>
  </v-list-item>
</template>
<script>

import api from "../api.js";

export default {
  name: "ChapterItem",
  mixins: [api],
  inject: ["theme"],
  props: {
    "toString": {
      type: String,
      required: true
    },
    "chapter": {
      type: Object,
      required: true
    },
    "progress": {
      type: Object,
      default: function() {
        return {
          total: 0,
          completed: 0
        };
      }
    },
    "displayCheck": {
      type: Boolean,
      default: false
    },
    "empty": {
      type: Boolean,
      default: false
    },
    "completed": {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
      empty_color_light: "#FFFFFF",
      filled_color_light: "rgb(194, 212, 252)",
      empty_color_dark: "#363636",
      filled_color_dark: "#2B81D6"
    };
  },
  methods: {
    createBackgroundString: function() {
      if(!this.empty) {
        const ratio = this.progress.completed/this.progress.total;
        const lower = (ratio*100).toFixed(1);
        const upper = (ratio*100 +0.1).toFixed(1);
        var filled_color = null;
        var empty_color = null;
        if(this.theme.isDark){
          filled_color = this.filled_color_dark;
          empty_color = this.empty_color_dark;
        } else {
          filled_color = this.filled_color_light;
          empty_color = this.empty_color_light;
        }
        return `linear-gradient(90deg, ${filled_color} ${lower}%, ${empty_color} ${upper}%)`;
      }
    }
  }
};

</script>

<style scoped>
.theme--dark .v-list .v-list-item--active {
  color: rgb(194, 212, 252);
}



</style>
