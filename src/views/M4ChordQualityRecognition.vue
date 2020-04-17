<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1 class="hidden-xs-only">4. Recognising Chords</h1>
            <h2>Chord Quality Recognition</h2>
            <p>
                The aim of the chord quality recognition exercises is to practice identifying common triads and seventh
                chords.
            </p>
            <p>
                In the chord quality recognition exercises chords are played on their own (there is no <i>I - IV - V</i>
                progression). After a pause of a few seconds you're told what chord you heard.
            </p>
            <h3>Preparing for the chord quality recognition exercises</h3>
            <p>
                All the previous recognition exercises focused on recognising sounds that you had previously
                internalised (the sounds of the scale degrees of the major scale).
            </p>
            <p>
                The aim of the chord quality recognition exercises is no different. The aim is to internalise the sound
                of each chord before you begin.
            </p>
            <p>
                To do this, use the targeting tones exercises for each chord. When you can pass the targeting tones
                tests for all the chords in any given recognition exercise you are ready to begin.
            </p>
            <h3>How to use the chord quality recognition exercises</h3>
            <p>
                Follow the steps below for the chord quality recognition exercises:
            </p>
            <ol>
                <li><p>
                    Listen to the chord as it is played
                </p></li>
                <li><p>
                    Focus your attention on the root note
                </p></li>
                <li><p>
                    <b>(OPTIONAL)</b> Sing the root note
                </p></li>
                <li><p>
                    Identify the quality of the chord
                </p></li>
            </ol>
            <p>
                Repeat this throughout the exercise.
            </p>
            <p>
                Step 3 is (like with other recognition exercises) an optional intermediate step. As you practice with
                these exercises you'll start hearing the root note easily and you won't need to sing it. But to begin
                with, sing it to ensure that you are able to accurately identify which note is the root note.
            </p>
            <p>
                If you are unsure whether you are identifying the root note accurately, return to the targeting tones
                exercises to focus on this.
            </p>
            <p>You pass the test if you complete it with 3 or less mistakes.</p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['maj', 'min', 'dim']}"
                                    :prog-id="6001"
                                    t-type="chord-quality">
                    Maj, Min & Dim Triads
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['maj7', 'min7', 'dom7']}"
                                    :prog-id="6002"
                                    t-type="chord-quality">
                    Maj 7th, Min 7th & Dom 7th
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['dim7', 'min7b5']}"
                                    :prog-id="6003"
                                    t-type="chord-quality">
                    Dim 7th & Min7b5
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11],
                chordTypes: ['maj', 'min', 'dim', 'maj7', 'min7', 'dom7', 'dim7', 'min7b5']}"
                                    :prog-id="6004"
                                    t-type="chord-quality">
                    Triads & 7th Chords
                </InlineConfigurator>
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/chords/diatonic-chord-internalisation">Next Chapter
            </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";

    export default {
        name: "M4ChordQualityRecognition",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>