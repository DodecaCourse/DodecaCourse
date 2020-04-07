<template>

  <v-list-group
    :value="active"
  >
    <template v-slot:activator>
    <v-list-item-action>
      <v-icon>{{ course.completed ? "mdi-checkbox-marked-outline" : "mdi-checkbox-blank-outline"}}</v-icon>
    </v-list-item-action>
    <v-list-item-content>
      <v-list-item-title>{{ num + 1}}. {{course.title}}</v-list-item-title>
    </v-list-item-content>
    </template>
    <v-list-item :key="chapter.id" v-for="chapter in course.chapters" :to="course.path + chapter.path">
      <v-list-item-title>{{ chapter.title }}</v-list-item-title>
      <v-icon>{{ chapter.completed ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}</v-icon>
    </v-list-item>
  </v-list-group>

</template>

<script>

export default {
  name: 'CourseItem',
  props: ['course', 'active', 'num'],
  methods: {
    changeCheck: function() {
      this.course.completed = !this.course.completed
    }
  }
}

</script>

<style scoped>
</style>
