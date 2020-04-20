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
  <v-list-group
    :value="active"
  >
    <template #activator>
      <v-list-item-action
        v-if="displayCheck "
      >
        <v-icon v-if="!(emptyModules.some(m => m === module.id))">
          {{ completedModules.some(m => m === module.id) ?
            "mdi-checkbox-marked-outline" : "mdi-checkbox-blank-outline" }}
        </v-icon>
        
        <v-icon v-else>
          <!-- also looks good without any icons -->
          mdi-chevron-right
        </v-icon>
      </v-list-item-action>
      <v-list-item-content>
        <v-list-item-title>
          <b>{{ num + 1 }}.</b> {{ module.title }}
        </v-list-item-title>
      </v-list-item-content>
    </template>
    <v-list-item
      v-for="chapter in module.chapters"
      :key="chapter.id"
      :to="module.path + chapter.path"
    >
      <v-list-item-title>{{ chapter.title }}</v-list-item-title>
      
      <v-list-item-action
        v-if="displayCheck && !emptyChapters.some(c => c === chapter.id)"
      >
        <v-icon>
          {{ completedChapters.some(c => c === chapter.id) ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline" }}
        </v-icon>
      </v-list-item-action>
    </v-list-item>
  </v-list-group>
</template>

<script>

import api from "../api.js";

export default {
  name: "ModuleItem",
  mixins: [api],
  props: {
    "module": {
      type: Object,
      required: true
    },
    "active": {
      type: Boolean,
      default: false
    },
    "num": {
      type: Number,
      required: true
    },
    "completedChapters": {
      type: Array,
      required: true
    },
    "emptyChapters": {
      type: Array,
      required: true
    },
    "completedModules": {
      type: Array,
      required: true
    },
    "emptyModules": {
      type: Array,
      required: true
    },
    "displayCheck": {
      type: Boolean,
      default: false
    }
  }
};

</script>
