<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>4. Recognising Chords</h1>
            <h2>Diatonic Chords Recognition</h2>
            <h3>Exercises</h3>
            <p>
                By now I'm sure you're feeling very familiar with the format of the recognition exercises.
            </p>
            <p>
                In the recognition exercises for diatonic chords you'll hear the I - IV - V progression at the beginning
                of the exercise, then you'll hear random diatonic chords played.
            </p>
            <p>
                You'll find 3 sets of recognition exercises. One that focuses on triads, one that focuses on seventh
                chords and one that includes both.
            </p>
            <h3>How to use the Diatonic Chords Recognition Exercises</h3>
            <p>
                Follow the steps below for these recognition exercises:
            </p>
            <ol>
                <li><p>
                    Listen to the I - IV - V Progression
                </p></li>
                <li><p>
                    Listen to the chord played next
                </p></li>
                <li><p>
                    <b>[OPTIONAL]</b> Sing the root note of the chord
                </p></li>
                <li><p>
                    Try to recognise the root note's scale degree and the quality of the chord
                </p></li>
                <li><p>
                    Check that you've identified it correctly
                </p></li>
            </ol>
            <p>
                Repeat steps 2- 5 throughout the exercise.
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
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11],
                diatonics: [2, 4, 5, 7, 9, 11], count: 3}"
                                    :prog-id="8001"
                                    t-type="chord-recognition">
                    Diatonic Triads
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11],
                diatonics: [2, 4, 5, 7, 9, 11], count: 4}"
                                    :prog-id="8002"
                                    t-type="chord-recognition">
                    Diatonic 7th Chords
                </InlineConfigurator>
            </p>
            <v-btn style="float: right" color="secondary" class="mx-3"
                   to="/minor/overview">Next module</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "M4DiatonicChordsRecognition",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>