<template>
    <div>
        <div v-bind:key="course.id" v-for="(course, num) in courses">
            <CourseItem
              v-bind:course="course"
              :visitedLevels="visitedLevels"
              :completedLevels="completedLevels"
              :user="user"
              :num="num"
              :active="$route.path.startsWith(course.path)"/>
        </div>
    </div>
</template>


<script>
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/backend-merge
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
            const self = this;
            this.getChapters(id)
              .then(l => lvls = l);
            lvls.forEach( lvl => {
              self.visitedLevels = self.visitedLevels + lvl.level_id;
              if(lvl.completed){
                self.completedLevels = self.completedLevels + lvl.level_id;
              }
            });
            console.log(this.visitedLevels);
            console.log(this.completedLevels);
          }
          
        }
      
      },
      created: function() {
        if(this.user != "not logged in"){
            this.getCompletedCourses();
        }
        
      }
  }
<<<<<<< HEAD
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
=======
>>>>>>> origin/backend-merge
</script>

<style scoped>
</style>
