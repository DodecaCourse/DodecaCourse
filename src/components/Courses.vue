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

        data: function () {
            return {
                courses: [
                    {
                        id: 0,
                        title: "Recognising the Tonic",
                        completed: false,
                        path: "/tonicinternalization"
                    },
                    {
                        id: 1,
                        title: "Individual notes",
                        completed: false,
                        path: "/internalization"
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

<style scoped>
</style>
