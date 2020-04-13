<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>5. Minor Keys</h1>
            <h2>Scale Degrees</h2>
            <h3>Internalisation</h3>
            <p>
                <InlineConfigurator :prog-id="9001" t-type="internalization"
                                    :config="{degree: 0}" scale="aeolian">
                    »Do« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="9003" t-type="internalization"
                                    :config="{degree: 3}" scale="aeolian">
                    »Me« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="9004" t-type="internalization"
                                    :config="{degree: 5}" scale="aeolian">
                    »Fa« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="9005" t-type="internalization"
                                    :config="{degree: 7}" scale="aeolian">
                    »So« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="9007" t-type="internalization"
                                    :config="{degree: 10}" scale="aeolian">
                    »Te« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                Having internalised the minor pentatonic scale, you can already play many
                pop songs by ear. You can already continue to the pentatonic
                <router-link to="/individual-notes/recognition">recognition
                    exercises</router-link>, while also doing the internalisation exercises of the two missing
                scale degrees, »Re« and »Le«.
            <p>
                <InlineConfigurator :prog-id="9002" t-type="internalization"
                                    :config="{degree: 2}" scale="aeolian">
                    »Re« Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="9006" t-type="internalization"
                                    :config="{degree: 8}" scale="aeolian">
                    »Le« Internalisation
                </InlineConfigurator>
            </p>
            <h3>Recognition</h3>
            <p>
                <InlineConfigurator :prog-id="10001" t-type="recognition-single"
                                    :config="{degrees: [0, 3, 5, 7, 10]}" scale="aeolian">
                    Minor Pentatonic Recognition
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :prog-id="10002" t-type="recognition-single"
                                    :config="{degrees: [0, 2, 3, 5, 7, 8, 10]}" scale="aeolian">
                    Minor Scale Recognition
                </InlineConfigurator>
            </p>
            <h2>Two Note Melodies</h2>

            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10], intervals: [1, 2, 3, 4]}" :prog-id="11001"
                                    t-type="recognition-interval" scale="aeolian">
                    2nds & 3rds
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10], intervals: [5, 6, 7]}" :prog-id="11002"
                                    t-type="recognition-interval" scale="aeolian">
                    4ths & 5ths
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10], intervals: [8, 9, 12]}" :prog-id="11003"
                                    t-type="recognition-interval" scale="aeolian">
                    6ths & 8ves
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10], intervals: [1,2,3,4,5,6,7,8,9,12]}"
                                    :prog-id="11004"
                                    t-type="recognition-interval" scale="aeolian">
                    Melodic Intervals
                </InlineConfigurator>
            </p>
            <h2>Chords</h2>
            <h3>Internalisation</h3>

            <h4>Diatonic Triads</h4>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 2, count: 3}"
                        :prog-id="12001" t-type="chord-internalization" hide-test scale="aeolian">
                    ii° Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 3, count: 3}"
                        :prog-id="12002" t-type="chord-internalization" hide-test scale="aeolian">
                    III Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 5, count: 3}"
                        :prog-id="12003" t-type="chord-internalization" hide-test scale="aeolian">
                    iv Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 7, count: 3}"
                        :prog-id="12004" t-type="chord-internalization" hide-test scale="aeolian">
                    v Internalisation
                </InlineConfigurator>
            </p>
            <p>
                The dominant often isn't played as a diatonic chord of the natural minor scale,
                but as a diatonic chord of the harmonic minor scale, which includes a raised
                7th, the major third of the V chord:
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 11], diatonic: 7, count: 3}"
                        :prog-id="12005" t-type="chord-internalization" hide-test scale="aeolian">
                    V Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 8, count: 3}"
                        :prog-id="12006" t-type="chord-internalization" hide-test scale="aeolian">
                    VI Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 10, count: 3}"
                        :prog-id="12007" t-type="chord-internalization" hide-test scale="aeolian">
                    VII Internalisation
                </InlineConfigurator>
            </p>

            <h4>Diatonic 7th Chords</h4>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 2, count: 4}"
                        :prog-id="12008" t-type="chord-internalization" hide-test scale="aeolian">
                    ii7b5 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 3, count: 4}"
                        :prog-id="12009" t-type="chord-internalization" hide-test scale="aeolian">
                    IIImaj7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 5, count: 4}"
                        :prog-id="12010" t-type="chord-internalization" hide-test scale="aeolian">
                    iv7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 7, count: 4}"
                        :prog-id="12011" t-type="chord-internalization" hide-test scale="aeolian">
                    v7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 11], diatonic: 7, count: 4}"
                        :prog-id="12012" t-type="chord-internalization" hide-test scale="aeolian">
                    V7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 8, count: 4}"
                        :prog-id="12013" t-type="chord-internalization" hide-test scale="aeolian">
                    VImaj7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 3, 5, 7, 8, 10], diatonic: 10, count: 4}"
                        :prog-id="12014" t-type="chord-internalization" hide-test scale="aeolian">
                    VII7 Internalisation
                </InlineConfigurator>
            </p>
            <h3>Recognition</h3>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10],
                diatonics: [0, 2, 3, 5, 7, 8, 10], count: 3}"
                                    :prog-id="8001"
                                    t-type="chord-recognition" scale="aeolian">
                    Diatonic Triads
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 3, 5, 7, 8, 10],
                diatonics: [0, 2, 3, 5, 7, 8, 10], count: 4}"
                                    :prog-id="8002"
                                    t-type="chord-recognition" scale="aeolian">
                    Diatonic 7th Chords
                </InlineConfigurator>
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/next/practice">What's next?
            </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "M5MinorKeyExercisesTests",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>