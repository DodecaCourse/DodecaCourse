<template>
  <div id="app">
    <Courses v-bind:courses="courses"/>
  </div>
</template>

<script>
  // Imports
  import Courses from "../components/Courses";

  export default {
    name: 'Home',
    components: {
      Courses,
    },
    data: function () {
      return {
        courses: [
          {
            id: 0,
            title: "Internalization",
            completed: false,
            path: "/internalization"
          },
          {
            id: 1,
            title: "Individual notes",
            completed: false,
            path: "/notes"
          },
          {
            id: 2,
            title: "Melodies",
            completed: false,
            path: "/melodies"
          },
          {
            id: 3,
            title: "Chords",
            completed: false,
            path: "/chords"
          }

        ]
      }
    }
  }
</script>
