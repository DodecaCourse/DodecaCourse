<template>

  <div class="course-item" v-bind:class="{'is-complete':course.completed}">
    <p>
      <b class="course-number">
        {{course.id+1}}
      </b>
      <a :href="course.path"><span>{{course.title}}</span></a>
      <input type="checkbox" v-on:change="changeCheck"/>
    </p>
  </div>

</template>

<script>

export default {
  name: 'CourseItem',
  props: ['course'],
  methods: {
    changeCheck: function() {
      this.course.completed = !this.course.completed
    }
  }
}

</script>

<style scoped>

.course-item {
  background: #f4f4f4;
  padding: 10px;
  border-bottom: 1px #ccc dotted;
}

.course-number {
  margin-right: 10px;
  /*
  background-color: #00948d;
  color: white;
  height: 100%;
  width: 30px;
  Muss mich wieder in CSS einlesen ;(
  Oder wollen wir sowas wie Bootstrap benutzen?
  Oder vuetify für vue?*/
}

.is-complete span{
  color: #545454;
  text-decoration: line-through;
}

span {
  margin-right: 10px;
}

.expand {
  alignment: right;
}

</style>
