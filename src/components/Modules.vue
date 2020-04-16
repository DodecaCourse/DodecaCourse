<template>
  <div>
    {{completed_chapters}}, {{completed_modules}}<br>
    {{empty_chapters}}, {{empty_modules}}
    <div v-bind:key="module.id" v-for="(module, num) in modules">
        <ModuleItem
          v-bind:module="module"
          :completed_chapters="completed_chapters"
          :empty_chapters="empty_chapters"
          :completed_modules="completed_modules"
          :empty_modules="empty_modules"
          :num="num"
          :display_check="display_check"
          :active="$route.path.startsWith(module.path)"/>
    </div>
  </div>
</template>


<script>
  import ModuleItem from "./ModuleItem";
  import structure from "../../public/structure.json";
  import api from "../api.js"
  
  export default {
      name: `Modules`,
      mixins: [api],
      components: {
          ModuleItem
      },
      props: ['curCourse'],
      data: function () {
          return {
              structure: {
                  "modules": [],
                  "chapters": [],
                  "targets": []
              },
              display_check: false,
              completed_chapters: [],
              empty_chapters: [],
              completed_modules: [],
              empty_modules: []
              
          }
      },
      computed: {
          modules: function () {
              return structure["modules"];
          }
      },
      methods: {
        updateCompleted: function() {
          
          // this.structure.targets.forEach(target => {
          //   var take = this.takes[target.id];
          //   console.log(take);
          //   this.structure.chapters.forEach(chapter => {
          //     console.log(chapter);
          //   });
          // });
        }
      
      },
      watch: {
        user: function () {
          if(this.user != null){
            this.display_check = true;
            this.updateCompleted();
          } else {
            this.display_check = false;
          }
        },
        takes: function() {
          this.updateCompleted();
        }
        
      }
  }
</script>

<style scoped>
</style>
