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
          <b>{{ num + 1 }}.</b> {{ $t("m"+module.id.toString()+".title") }}
        </v-list-item-title>
      </v-list-item-content>
    </template>

    <ChapterItem
      v-for="chapter in module.chapters"
      :key="chapter.id"
      :to-string="module.path + chapter.path"
      :module="module"
      :chapter="chapter"
      :progress="getChapterProgress(chapter)"
      :display-check="displayCheck"
      :completed="completedChapters.some(c => c === chapter.id)"
      :empty="emptyChapters.some(c => c === chapter.id)"
    />
  </v-list-group>
</template>

<script>

import api from "../api.js";
import ChapterItem from "./ChapterItem.vue";

export default {
  name: "ModuleItem",
  components: {
    ChapterItem
  },
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
  },
  methods: {
    getChapterProgress: function(chapter){
      var total = 0;
      var compd = 0;
      this.targets.forEach(target => {
        if(target.chapter_id === chapter.id){
          total += target.levels;
          var take = this.takes[target.id];
          if(take != null) {
            for(var i=target.levels; i>=0; i--){
              if(take[i] != null){
                if(take[i].completed === true) {
                  compd+=i;
                  break;
                }
              }
            }
          }
        }
      });

      return {
        total: total,
        completed: compd
      };
    }
  }
};

</script>
