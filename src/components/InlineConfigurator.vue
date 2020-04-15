<template>
    <v-card class="d-flex flex-wrap px-1 align-center justify-center" elevation="2"
        >
        <b class="mx-1"><slot></slot>:</b>
        <DegreeCirclePictogram v-show="enabledDegrees !== undefined" :enabled-degrees="enabledDegrees">
        </DegreeCirclePictogram>
        <div>
        <v-btn v-show="levels > 1" v-for="(lvl, i) in this.levels" :key="i + 1"
               @click="level = i + 1"
               :class="{
                   'finished': takes[progId] !== undefined &&
                   takes[progId][i+1] !== undefined && takes[progId][i+1].completed,
                   'mx-1': i === 0,
                   'mr-1': i < 0
               }"
               :color="level === i + 1 ? 'primary' : 'secondary'"
               fab x-small depressed
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
            <v-btn v-if="!hideTest && user != null"
                   title="Mark as completed"
                   @click="toggleCompleted" icon :style="completed ? 'color: green' : ''">
                <v-icon>{{completed ? 'mdi-check-circle' : 'mdi-check-circle-outline'}}</v-icon>
            </v-btn>
        </div>
    </v-card>
</template>

<script>
    import structure from "../../public/structure.json"
    import DegreeCirclePictogram from "./DegreeCirclePictogram";
    import api from "../api";

    const INTERNALIZATION = 0;
    const RECOGNITION_SINGLE = 1;
    const RECOGNITION_INTERVAL = 2;
    const TARGET_TONE = 3;
    const CHORD_QUALITY = 4;
    const CHORD_INTERNALIZATION = 5;
    const CHORD_RECOGNITION = 6;

    export default {
        name: "InlineConfigurator",
        components: {DegreeCirclePictogram},
        mixins: [api],
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
                required: true,
            },
            hideTest: {
                type: Boolean,
            },
            hidePractice: {
                type: Boolean,
            },
            scale: {
                type: String
            },
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
                else if (this.tType === "chord-internalization") return CHORD_INTERNALIZATION;
                else if (this.tType === "chord-recognition") return CHORD_RECOGNITION;
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
            },
            completed: function () {
                return this.takes[this.progId] !== undefined &&
                    this.takes[this.progId][this.level] !== undefined &&
                    this.takes[this.progId][this.level].completed
            },
        },
        methods: {
            onPractice: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalization(this.config.degree, true, this.level, this.scale);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingle(this.config.degrees, true, this.level, this.scale);
                } else if (this.type === RECOGNITION_INTERVAL) {
                    this.$teacher.setupRecognitionInterval(this.config.degrees, this.config.intervals,
                        true, this.level, this.scale)
                } else if (this.type === TARGET_TONE) {
                    this.$teacher.setupTargetTone(this.config.chordTypes, true, this.level, this.scale)
                } else if (this.type === CHORD_QUALITY) {
                    this.$teacher.setupChordQuality(this.config.chordTypes, true, this.level, this.scale)
                } else if (this.type === CHORD_INTERNALIZATION) {
                    this.$teacher.setupChordInternalization(this.config.diatonic, this.config.degrees, this.config.count, true, this.level, this.scale)
                } else if (this.type === CHORD_RECOGNITION) {
                    this.$teacher.setupChordRecognition(this.config.diatonics, this.config.degrees, this.config.count, true, this.level, this.scale)
                }
            },
            onTest: function () {
                if (this.type === INTERNALIZATION) {
                    this.$teacher.setupInternalizationTest(this.config.degree, true, this.level, this.scale);
                } else if (this.type === RECOGNITION_SINGLE) {
                    this.$teacher.setupRecognitionSingleTest(this.config.degrees, true, this.level, this.scale);
                } else if (this.type === RECOGNITION_INTERVAL) {
                    this.$teacher.setupRecognitionIntervalTest(this.config.degrees, this.config.intervals,
                        true, this.level, this.scale)
                } else if (this.type === TARGET_TONE) {
                    this.$teacher.setupTargetToneTest(this.config.chordTypes, true, this.level, this.scale)
                } else if (this.type === CHORD_QUALITY) {
                    this.$teacher.setupChordQualityTest(this.config.chordTypes, true, this.level, this.scale)
                } else if (this.type === CHORD_INTERNALIZATION) {
                    console.error("No chord internalization test available");
                } else if (this.type === CHORD_RECOGNITION) {
                    this.$teacher.setupChordRecognitionTest(this.config.diatonics, this.config.degrees, this.config.count,true, this.level, this.scale)
                }
            },
            toggleCompleted: function () {
                // change local version first
                if (this.takes[this.progId] === undefined) {
                    this.takes[this.progId] = {}
                }
                if (this.takes[this.progId][this.level] === undefined) {
                    console.log("undefined",this.takes[this.progId][this.level]);
                    this.takes[this.progId][this.level] = {
                        completed: false
                    };
                }
                this.takes[this.progId][this.level].completed = !this.takes[this.progId][this.level].completed;
                // update backend
                console.log(this.takes, this.takes[this.progId][this.level].completed);
                if (this.takes[this.progId][this.level].completed) {
                    this.completeTarget(this.progId, this.level)
                        .then(res => console.log("result:", res));
                } else {
                    this.unsetCompleteTarget(this.progId, this.level)
                        .then(res => console.log("result:", res));
                }
                this.getTakes()
                    .then(res => console.log("result:", res));
                this.updateTakes();
            },
        },
        create: function () {
            if (this.user != null)
                this.updateTakes();
            console.log(this.takes);
        },
    }
</script>

<style lang="sass" scoped>
    .level:not(.v-btn--text):not(.v-btn--outlined):focus::before
        opacity: 0

    .level.finished
        box-shadow: 0 0 8px #00a802 !important
</style>