<template>
    <div>
        <div v-bind:key="course.id" v-for="course in courses">
            <CourseItem v-bind:course="course"/>
        </div>
    </div>
</template>


<script>
    import CourseItem from "./CourseItem";

    export default {
        name: `Courses`,
        components: {
            CourseItem
        },
        props: ["courses"]
    }
</script>

<style scoped>
</style>