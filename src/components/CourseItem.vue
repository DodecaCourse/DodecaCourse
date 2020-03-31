<template>

  <v-list-group
    :value="active"
  >
    <template v-slot:activator>
    <v-list-item-action>
      <v-icon>{{ course.completed ? "mdi-checkbox-marked-outline" : "mdi-checkbox-blank-outline"}}</v-icon>
    </v-list-item-action>
    <v-list-item-content>
      <v-list-item-title>{{ course.id + 1}}. {{course.title}}</v-list-item-title>
    </v-list-item-content>
    </template>
    <v-list-item :to="course.path + '/overview'">
      <v-list-item-title>Overview</v-list-item-title>
      <v-icon>{{ course.completed ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}</v-icon>
    </v-list-item>
    <v-list-item :to="course.path + '/method'">
      <v-list-item-title>Method</v-list-item-title><v-icon>{{ course.completed ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}</v-icon>
    </v-list-item>
    <v-list-item :to="course.path + '/test'">
      <v-list-item-title>Test</v-list-item-title>
      <v-icon>{{ course.completed ? "mdi-checkbox-marked-circle-outline" : "mdi-checkbox-blank-circle-outline"}}</v-icon>
    </v-list-item>
  </v-list-group>

</template>

<script>

export default {
  name: 'CourseItem',
  props: ['course', 'active'],
  methods: {
    changeCheck: function() {
      this.course.completed = !this.course.completed
    }
  }
}

</script>

<style scoped>
</style>
