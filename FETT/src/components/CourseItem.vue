<template>
    <div class="course-item" v-bind:class="{'is-complete':course.completed}">
        <p>
            <input type="checkbox" v-on:change="changeCheck"/>
            <span>{{course.title}}</span>
            <!--<button class="expand">
                Expand
            </button>-->
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

    .is-complete span{
        color: #545454;
        text-decoration: line-through;
    }

    .expand {
        alignment: right;
    }
</style>
