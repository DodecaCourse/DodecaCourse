<template>
    <v-card class="d-flex flex-wrap px-1 align-center justify-center" elevation="2"
        >
        <b class="mx-1"><slot></slot>:</b>
        <DegreeCirclePictogram v-show="enabledDegrees !== undefined" :enabled-degrees="enabledDegrees">
        </DegreeCirclePictogram>
        <div>
        <v-btn v-show="levels > 1" :class="i === 0 ? 'mx-1' : 'mr-1'" v-for="(lvl, i) in this.levels" :key="i + 1"
               @click="level = i + 1" :color="level === i + 1 ? 'primary' : 'secondary'" fab x-small depressed
        class="level">
            {{i + 1}}
        </v-btn>
        </div>
        <div>
        <v-btn v-if="!hidePractice" class="ma-1" color="primary" small elevation="1" v-on:click="onPractice">
            Practice
        </v-btn>
        <v-btn v-if="!hideTest" class="ma-1" color="ternary" small elevation="1" v-on:click="onTest">
            Test
        </v-btn>
        </div>
    </v-card>
</template>

<script>
    import structure from "../../public/structure.json"
    import DegreeCirclePictogram from "./DegreeCirclePictogram";

    const INTERNALIZATION = 0;
    const RECOGNITION_SINGLE = 1;
    const RECOGNITION_INTERVAL = 2;
    const TARGET_TONE = 3;
    const CHORD_QUALITY = 4;

    export default {
        name: "InlineConfigurator",
        components: {DegreeCirclePictogram},
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
                else if (this.tType === "recognition-interval") return RECOGNITION_INTERVAL;
                else if (this.tType === "target-tone") return TARGET_TONE;
                else if (this.tType === "chord-quality") return CHORD_QUALITY;
                else return INTERNALIZATION;
            },
            levels: function () {
                return this.target.levels;
            },
            enabledDegrees: function () {
                if (this.type === INTERNALIZATION) {
                    return [this.config.degree]
                } else if (this.type === RECOGNITION_SINGLE) {
                    return this.config.degrees;
                } else if (this.type === RECOGNITION_INTERVAL) {
                    return this.config.degrees;
                } else {
                    return this.config.degrees || [0, 2, 4, 5, 7, 9, 11];
                }
            }
        },
        methods: {
            onPractice: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalization(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingle(this.config.degrees, true, this.level);
                } else if (this.type === RECOGNITION_INTERVAL) {
                    this.$teacher.setupRecognitionInterval(this.config.degrees, this.config.intervals,
                        true, this.level)
                } else if (this.type === TARGET_TONE) {
                    this.$teacher.setupTargetTone(this.config.chordTypes, true, this.level)
                } else if (this.type === CHORD_QUALITY) {
                    this.$teacher.setupChordQuality(this.config.chordTypes, true, this.level)
                }
            },
            onTest: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalizationTest(this.config.degree, true);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingleTest(this.config.degrees, true, this.level);
                } else if (this.type === RECOGNITION_INTERVAL) {
                    this.$teacher.setupRecognitionIntervalTest(this.config.degrees, this.config.intervals,
                        true, this.level)
                } else if (this.type === TARGET_TONE) {
                    this.$teacher.setupTargetToneTest(this.config.chordTypes, true, this.level)
                } else if (this.type === CHORD_QUALITY) {
                    this.$teacher.setupChordQualityTest(this.config.chordTypes, true, this.level)
                }
            }
        }
    }
</script>

<style lang="sass" scoped>
    .level:not(.v-btn--text):not(.v-btn--outlined):focus::before
        opacity: 0
</style>