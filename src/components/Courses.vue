<template>
    <div>
        <div v-bind:key="course.id" v-for="course in courses">
            <CourseItem v-bind:course="course" :active="course.id === curCourse"/>
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
                                completed: true,
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
                                title: 'Internalisation Method',
                                completed: false,
                                path: '/internalisation-method'
                            },
                            {
                                id: 2,
                                title: 'Internalisation Test',
                                completed: false,
                                path: '/internalisation-test'
                            },
                            {
                                id: 3,
                                title: 'Recognition Method',
                                completed: false,
                                path: '/recognition-method'
                            },
                            {
                                id: 4,
                                title: 'Recognition Test',
                                completed: false,
                                path: '/recognition-test'
                            }
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
