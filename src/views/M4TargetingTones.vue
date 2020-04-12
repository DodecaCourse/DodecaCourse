<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>4. Recognising Chords</h1>
            <h2>Targeting Tones</h2>
            <h3>Exercises</h3>
            <p>
                The targeting tones exercises make it easy to learn how to zero in on the sound of the root note of any
                chord.
            </p>
            <p>
                You'll find a targeting tones exercise for each triad as well as the most common 7th chords - maj 7, min
                7 and dom 7. In a targeting tones exercise you will hear a chord played for a bar, then the root note of
                that chord played on its own for a bar. This is repeated for 8 bars before the process is repeated in a
                new key.
            </p>
            <p>
                By alternating between the complete chord and the root note you'll quickly develop a level of
                familiarity with the sound of the root note of any chord among the other notes.
            </p>
            <p>
                Below you can see the first 24 bars of the major triad targeting tones exercise.
            </p>
            <p>
                <v-img  contain max-height="25ch" max-width="83.5vw"
                        src="/img/m4_targeting_tones_exercise.svg"
                       title="24 bars of the major triad targeting tones exercise"/>
            </p>
            <h3>How to use the targeting tones exercises</h3>
            <p>
                The approach for the targeting tones exercises is simple:
            </p>
            <ol>
                <li><p>
                    When you hear the target note on its own, listen closely to the sound of that individual note.
                </p></li>
                <li><p>
                    When you hear the full combination of notes played again, listen for that note’s individual sound.
                </p></li>
                <li><p>
                    Sing the root note of the chord occasionally throughout the exercise to help you focus on its sound.
                </p></li>
            </ol>
            <p>
                As you listen closely and sing the root note of each chord type you'll start to develop a familiarity
                with the sound of the root note in any chord.
            </p>
            <p>
                After spending a session or two on each targeting tones exercise, attempt the corresponding targeting
                tones test to see if you are indeed able to find the root note when you hear that chord played
            </p>
            <h3>Tests</h3>
            <p>
                Just as there was an internalisation test for each internalisation exercise in the first two modules,
                there is a targeting tones test for each targeting tones exercise.
            </p>
            <p>
                The targeting tones tests function similarly to the internalisation tests as well.
            </p>
            <p>
                You'll hear a chord played, then a pause for a few seconds, then the root note of the chord will be
                played. This is repeated in 12 keys.
            </p>
            <p>
                You can see the first 16 bars of the major triad targeting tones test below:
            </p>
            <p>
                <v-img contain max-height="17ch" max-width="83.5vw"
                        src="/img/m4_targeting_tones_test.svg"
                     title="The first 16 bars of the major triad targeting tones test"/>
            </p>
            <h3>How to use the targeting tones tests</h3>
            <p>
                The targeting tones tests work in much the same way as the internalisation tests from module 1 and 2:
            </p>
            <ol>
                <li><p>
                    When you hear the chord played, listen for the sound of the chord's root note.
                </p></li>
                <li><p>
                    During the pause, sing the root note.
                </p></li>
                <li><p>
                    Hold the root note and listen to see if you've sung it correctly.
                </p></li>
            </ol>
            <p>
                When you can sing 10 out of 12 root notes correctly, move onto the targeting tones exercise for the next chord.
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['maj']}"
                                    :prog-id="5001"
                                    t-type="target-tone">
                    Major
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['min']}"
                                    :prog-id="5002"
                                    t-type="target-tone">
                    Minor
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['maj7']}"
                                    :prog-id="5003"
                                    t-type="target-tone">
                    Major 7th
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['min7']}"
                                    :prog-id="5004"
                                    t-type="target-tone">
                    Minor 7th
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['dom7']}"
                                    :prog-id="5005"
                                    t-type="target-tone">
                    Dominant 7th
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['dim7']}"
                                    :prog-id="5006"
                                    t-type="target-tone">
                    Diminished 7th
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator :config="{degrees: [0, 2, 4, 5, 7, 9, 11], chordTypes: ['min7b5']}"
                                    :prog-id="5007"
                                    t-type="target-tone">
                    Minor 7b5
                </InlineConfigurator>
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/chords/chord-quality-recognition">Next Chapter
            </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "M4TargetingTones",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>