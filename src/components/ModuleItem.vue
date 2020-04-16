<template>

  <v-list-group
    :value="active"
  >
    <template v-slot:activator>
    
      <v-list-item-action
        v-if="display_check && !(empty_modules.some(m => m === module.id))"
      >
        <v-icon>
          {{ completed_modules.some(m => m === module.id) ?
             "mdi-checkbox-marked-outline" : "mdi-checkbox-blank-outline" }}
        </v-icon>
      </v-list-item-action>
      <v-list-item-content>
        <v-list-item-title>
          <b>{{ num + 1 }}.</b> {{module.title}}
        </v-list-item-title>
      </v-list-item-content>
    </template>
    <v-list-item
      :key="chapter.id"
      v-for="chapter in module.chapters"
      :to="module.path + chapter.path"
    >
      <v-list-item-title>{{ chapter.title }}</v-list-item-title>
      
      <v-icon
        v-if="user != null && display_check"
      >
        {{ completed_chapters.some(chapter => chapter === chapter.id) ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}
      </v-icon>
    </v-list-item>
  </v-list-group>

</template>

<script>

import api from "../api.js"

export default {
  name: 'ModuleItem',
  mixins: [api],
  props: [
    'module',
    'active',
    'num',
    'completed_chapters',
    'empty_chapters',
    'completed_modules',
    'empty_modules',
    'display_check'
  ]
}

</script>

<style scoped>
</style>
