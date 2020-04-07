<template>
    <v-card class="d-inline-flex px-1 align-center justify-center" elevation="2"
        >
        <b class="mx-1 hidden-sm-and-down"><slot></slot>:</b>
            <v-btn v-show="levels > 1" class="mr-1" v-for="(lvl, i) in this.levels" :key="i + 1"
                   @click="level = i + 1" :color="level === i + 1 ? 'primary' : 'secondary'" fab x-small depressed >
                {{i + 1}}
            </v-btn>
        <v-btn v-if="!hidePractice" class="ma-1" color="primary" small elevation="1" v-on:click="onPractice">
            Practice
        </v-btn>
        <v-btn v-if="!hideTest" class="ma-1" color="ternary" small elevation="1" v-on:click="onTest">
            Test
        </v-btn>
    </v-card>
</template>

<script>
    import structure from "../../public/structure.json"

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
                type: Number,
            },
            hideTest: {
                type: Boolean,
            },
            hidePractice: {
                type: Boolean,
            }
        },
        data: function () {
            return {
                level: 1,
            }
        },
        computed: {
            target: function () {
                for (let i=0;i<structure.targets.length;i++)
                    if (structure.targets[i].id === this.progId) return structure.targets[i];
                return undefined;
            },
            type: function () {
                // defaults to INTERNALIZATION
                if (this.tType === "internalization") return INTERNALIZATION;
                else if (this.tType === "recognition-single") return RECOGNITION_SINGLE;
                else return INTERNALIZATION;
            },
            levels: function () {
                return this.target.levels;
            },
        },
        methods: {
            onPractice: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalization(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingle(this.config.degrees, true, this.level);
                }
            },
            onTest: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalizationTest(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingleTest(this.config.degrees, true, this.level);
                }
            }
        }
    }
</script>

<style scoped>

</style>