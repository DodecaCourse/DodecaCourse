<template>
  <div id="app">
    <Header/>
    <Courses v-bind:courses="courses"/>
  </div>
</template>

<script>
  // Imports
  import Courses from "./components/Courses";
  import Header from "./components/Header";

  export default {
    name: 'Eartrainer',
    components: {
      Courses,
      Header
    },
    data: function () {
      return {
        courses: [
          {
            id: 0,
            title: "Chords",
            completed: false
          },
          {
            id: 1,
            title: "Pitch",
            completed: true
          },
          {
            id: 2,
            title: "Tempo",
            completed: false
          }

        ]
      }
    }
  }
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }
</style>
