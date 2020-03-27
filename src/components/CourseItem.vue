<template>
    <div class="course-item" v-bind:class="{'is-complete':course.completed}">
        <p>
            <input type="checkbox" v-on:change="changeCheck"/>
            {{course.title}}
            <button>

            </button>
        </p>
    </div>
</template>

<script>
    export default {
        name: 'CourseItem',
        props: ["course"],
        methods: {
            changeCheck: function () {
                this.course.completed = !this.course.completed;
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

    .is-complete {
        color: #545454;
        text-decoration: line-through;
    }
</style>