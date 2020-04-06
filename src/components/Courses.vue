<template>
    <div>
        <div v-bind:key="course.id" v-for="(course, num) in courses">
            <CourseItem v-bind:course="course" :num="num" :active="$route.path.startsWith(course.path)"/>
        </div>
    </div>
</template>


<script>
    import CourseItem from "./CourseItem";
    import Vue from "vue";

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
                return this.structure["modules"];
            }
        },
        beforeCreate: function () {
            fetch("/structure.json")
                .then(r => r.json())
                .then(json => {
                    Vue.prototype.$structureJSON = json;
                    this.structure = json;
                });
        }
    }
</script>

<style scoped>
</style>
