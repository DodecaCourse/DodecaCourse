<template>
    <div>
        <v-text-field v-model="input" placeholder="Input" />
        <v-btn @click="onSubmit">Submit</v-btn>
        <p>{{answer}}</p>
    </div>
</template>

<script>
    export default {
        name: "BasicInput",
        props: {
            submitSolution: {
                type: Function,
                required: true,
            },
            answer: {
                type: String,
                required: true,
            }
        },
        data: function() {
            return {
                input: '',
            }
        },
        methods: {
            onSubmit: function () {
                this.submitSolution(this.input);
            }
        }
    }
</script>

<style scoped>

</style>