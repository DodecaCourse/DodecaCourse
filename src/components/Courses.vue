<template>
    <div>
        <div v-bind:key="course.id" v-for="(course, num) in courses">
            <CourseItem v-bind:course="course" :num="num" :active="$route.path.startsWith(course.path)"/>
        </div>
    </div>
</template>


<script>
  import CourseItem from "./CourseItem";
  import structure from "../../public/structure.json";

  export default {
      name: `Courses`,
      components: {
          CourseItem
      },
      props: ['curCourse'],
      data: function () {
          return {
              structure: {
                  "modules": [],
                  "targets": []
              }
          }
      },
      computed: {
          courses: function () {
              return structure["modules"];
          }
      },
  }
</script>

<style scoped>
</style>
