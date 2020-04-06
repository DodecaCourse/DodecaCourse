<template>
    <div>
        <div v-bind:key="course.id" v-for="course in courses">
            <CourseItem v-bind:course="course" :active="$route.path.startsWith(course.path)"/>
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
        props: ['curCourse'],

        data: function () {
            return {
                courses: [
                    {
                        id: 0,
                        title: "Recognising the Tonic",
                        completed: false,
                        path: "/tonic-internalization",
                        chapters: [
                            {
                                id: 0,
                                title: 'Overview',
                                completed: false,
                                path: '/overview'
                            },
                            {
                                id: 1,
                                title: 'The Tonic',
                                completed: false,
                                path: '/tonic'
                            },
                            {
                                id: 2,
                                title: 'Exercise',
                                completed: false,
                                path: '/exercise'
                            },
                            {
                                id: 3,
                                title: 'Test',
                                completed: false,
                                path: '/test'
                            }
                        ]
                    },
                    {
                        id: 1,
                        title: "Recognising Individual Notes",
                        completed: false,
                        path: "/individual-notes",
                        chapters: [
                            {
                                id: 0,
                                title: 'Overview',
                                completed: false,
                                path: '/overview'
                            },
                            {
                                id: 1,
                                title: 'Scale Degrees',
                                completed: false,
                                path: '/scale-degrees'
                            },
                            {
                                id: 2,
                                title: 'Internalisation',
                                completed: false,
                                path: '/internalisation'
                            },
                            {
                                id: 4,
                                title: 'Recognition',
                                completed: false,
                                path: '/recognition'
                            },
                        ]
                    },
                    {
                        id: 2,
                        title: "Recognising Melodies",
                        completed: false,
                        path: "/recognising-melodies",
                        chapters: [
                            {
                                id: 0,
                                title: 'Overview',
                                completed: false,
                                path: '/overview'
                            },
                            {
                                id: 1,
                                title: 'Recognition Exercises',
                                completed: false,
                                path: '/recognition-exercises'
                            }
                        ]
                    },
                    {
                        id: 3,
                        title: "Chords",
                        completed: false,
                        path: "/chords",
                        chapters: [
                            {
                                id: 0,
                                title: 'Overview',
                                completed: false,
                                path: '/overview'
                            },
                            {
                                id: 1,
                                title: 'Method',
                                completed: false,
                                path: '/method'
                            },
                            {
                                id: 2,
                                title: 'Test',
                                completed: false,
                                path: '/test'
                            }
                        ]
                    }

                ]
            }
        }
    }
</script>

<style scoped>
</style>
