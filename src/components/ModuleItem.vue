<template>

  <v-list-group
    :value="active"
  >
    <template v-slot:activator>
    
      <v-list-item-action
        v-if="display_check "
      >
        <v-icon v-if="!(empty_modules.some(m => m === module.id))">
          {{ completed_modules.some(m => m === module.id) ?
             "mdi-checkbox-marked-outline" : "mdi-checkbox-blank-outline" }}
        </v-icon>
        
        <v-icon v-else>
          <!-- also looks good without any icons -->
          mdi-chevron-right
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
      
      <v-list-item-action
        v-if="display_check && !empty_chapters.some(c => c === chapter.id)"
      >
        <v-icon>
          {{ completed_chapters.some(c => c === chapter.id) ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}
        </v-icon>
        
      </v-list-item-action>
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
  ],
  beforeDestroy: function()  {
    var logoff_id = null;
    console.log(this.$route.path);
    this.module.chapters.forEach(chapter => {
      
      console.log(this.module.path + chapter.path);
      if (this.$route.path.startsWith(this.module.path + chapter.path)) {
        logoff_id = chapter.id;
      }
    });
    
    if(logoff_id != null){
      alert(this.logoff_id);
      // Problem: user is not defined anymore on beforeDetroy
      // issue an extra updateCurrentUser()?
      // this.updateCurrentUser(); doesnt Work
      // maybe run this inside App.vue?
      this.setLogoffChapter(logoff_id);
    }
    
  }
}

</script>

<style scoped>
</style>
