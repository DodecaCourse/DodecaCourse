<template>
    <div>
        <div v-bind:key="course.id" v-for="(course, num) in courses">
            <CourseItem
              v-bind:course="course"
              :visitedLevels="visitedLevels"
              :completedlevels="completedLevels"
              :user="user"
              :num="num"
              :active="$route.path.startsWith(course.path)"/>
        </div>
    </div>
</template>


<script>
<<<<<<< HEAD
  import CourseItem from "./CourseItem";
  import structure from "../../public/structure.json";
  import api from "../api.js"
  
  export default {
      name: `Courses`,
      mixins: [api],
      components: {
          CourseItem
      },
      props: ['curCourse', 'user'],
      data: function () {
          return {
              structure: {
                  "modules": [],
                  "targets": []
              },
              visitedLevels: [],
              completedLevels: []
          }
      },
      computed: {
          courses: function () {
              return structure["modules"];
          }
      },
      methods: {
        getCompletedCourses: function() {
          var usr;
          this.getUserID(this.user)
            .then(u => usr = u);
          
          if(usr.user_id != null){
            var id = usr.user_id;
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
        if(this.user != "not logged in"){
            this.getCompletedCourses();
        }
        
      }
  }
=======
    import CourseItem from "./CourseItem";
    import structure from "../../public/structure.json";

    export default {
        name: `Courses`,
        components: {
            CourseItem
        },
        props: ['curCourse'],
        computed: {
            courses: function () {
                return structure["modules"];
            }
        },
    }
>>>>>>> 10c8b47a5b7d6d14d29df5a0edd09f704a144d12
</script>

<style scoped>
</style>
