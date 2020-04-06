<template>
    <v-card class="d-inline-flex px-1 align-center justify-center" elevation="2"
        >
        <b class="mx-1 hidden-sm-and-down"><slot></slot>:</b>
        <v-btn class="ma-1" color="primary" small elevation="1" v-on:click="onPractice">
            Practice
        </v-btn>
        <v-btn class="ma-1" color="ternary" small elevation="1" v-on:click="onTest">
            Test
        </v-btn>
    </v-card>
</template>

<script>
    const INTERNALIZATION = 0;
    const RECOGNITION_SINGLE = 1;

    export default {
        name: "InlineConfigurator",
        props: {
            tType: {
                type: String,
                required: true
            },
            config: {
                type: Object,
            },
            progId: {
                type: String,
            }
        },
        computed: {
            type: function () {
                // defaults to INTERNALIZATION
                if (this.tType === "internalization") return INTERNALIZATION;
                else if (this.tType === "recognition-single") return RECOGNITION_SINGLE;
                else return INTERNALIZATION;
            },
        },
        methods: {
            onPractice: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalization(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingle(this.config.degrees, true);
                }
            },
            onTest: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalizationTest(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingleTest(this.config.degrees, true);
                }
            }
        }
    }
</script>

<style scoped>

</style>