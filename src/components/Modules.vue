<template>
    <div>
        <div v-bind:key="course.id" v-for="(course, num) in courses">
            <ModuleItem
              v-bind:course="course"
              :completed_levels="completedLevels"
              :num="num"
              :active="$route.path.startsWith(course.path)"/>
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
                  "targets": []
              },
              
              completed_modules: [],
              completed_chapters: [],
              completed_targets: []
          }
      },
      computed: {
          courses: function () {
              return structure["modules"];
          }
      },
      methods: {
        getCompletedCourses: function() {
        
          if(this.user.user_id != null){
            var id = this.user.user_id;
            var lvls;
            this.getChapters(id)
              .then(l => lvls = l);
            lvls.forEach( lvl => {
              this.visitedLevels = this.visitedLevels + lvl.level_id;
              if(lvl.completed){
                this.completedLevels = this.completedLevels + lvl.level_id;
              }
            });
            console.log(this.visitedLevels);
            
          }
          
        }
      
      },
      created: function() {
        this.updateCurrentUser();
        if(this.user != null){
            this.getCompletedCourses();
        }
        
      }
  }
</script>

<style scoped>
</style>
