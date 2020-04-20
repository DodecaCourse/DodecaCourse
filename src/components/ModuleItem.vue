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
    <v-list-item
      v-for="chapter in module.chapters"
      :key="chapter.id"
      :to="module.path + chapter.path"
    >
      <v-list-item-title> {{ $t("m"+module.id.toString()+".chapters."+chapter.id.toString()) }} </v-list-item-title>
      
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
