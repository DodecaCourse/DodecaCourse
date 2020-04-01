<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>1. Recognising the Tonic</h1>
            <h2>Test</h2>
            <v-banner app elevation="0" id="player" sticky>
                <Teacher fixed-degree="1P" t-type="internalization-test"/>
            </v-banner>
            <p>
                The tonic internalisation test gives you a way to easily tell when
                you have successfully internalised the sound of the tonic so you can
                move onto module 2.</p>
            <p>Just like the
                internalisation exercise, the tonic internalisation test is made up
                of a sequence that is repeated throughout the exercise. This time
                it's an 8 bar sequence:</p>
            <p>
                <v-img contain
                       max-height="18ch"
                       max-width="90vw" src="/img/m1_test8barsequence.png" title="The first 8 bars of the tonic internalisation test"/>
            </p>
            <p>The tonic
                internalisation test can be broken down into 3 sections:</p>
            <p><b>Bars 1-2:</b>
                Establish one note as the tonic</p>
            <p>Just like in the
                internalisation exercise, a note is established as the tonic using
                the I - IV - V progression.</p>
            <p><b>Bars 3-6:</b> Pause</p>
            <p>During the
                following 4 bars, there is a pause. This is where the testing takes
                place. You'll find out how in the next section.</p>
            <p><b>Bars 7-8:</b> The
                tonic is played</p>
            <p>In the final 2
                bars of the sequence, the tonic is played. It is repeated in three
                octaves, so that it will match your register, regardless of your
                range.</p>
            <p><b>Sequence Repeats:</b>
                The 8 bar sequence is repeated in a new key. Like in the
                internalisation exercises, the key centre moves up by a perfect 4th
                each time: the fourth scale degree of the old key is the tonic of the
                new one. The diagram below shows the first 24 bars of the tonic
                internalisation test:</p>
            <p>
                <v-img contain
                       max-height="54ch"
                       max-width="90vw" src="/img/m1_test24barsequence.png" title="The first 24 bars of the tonic internalisation test"/>
            </p>
            <p><br/>
            </p>
            <h3>How to use the tonic internalisation test</h3>
            <p>
                Download and listen to listen to the tonic internalisation test
                while you read the instructions.</p>

            <ol>
                <li><p><b>Listen to the
                    I - IV - V Progression:</b> Like with the internalisation exercises (and
                    all other exercises in the course) just listen to the I - IV - V
                    progression while it outlines the key.</p>
                </li>
                <li><p><b>Listen for
                    the sound of the tonic and hear it clearly in your head:</b> wait until
                    the I - IV - V progression has been played and you hear the tonic
                    chord played again, then see if you can hear internally which note
                    is the tonic. Try to hear it as clearly as you can in your head.</p>
                </li>
                <li><p><b>Sing the
                    tonic:</b> Sing the note you hear as the tonic in your head. If you
                    can't hold it for the entire duration of the pause, stop and take a
                    breath, then sing it again until you hear the tonic played.</p>
                </li>
                <li><p><b>Check that
                    you have sung the target scale degree correctly:</b> Listen to the tonic
                    when it is played to see if it's the same note as the one you're
                    singing.</p>
                </li>
                <li><p><b>Repeat:</b> The
                    tonic internalisation exercise moves through all 12 keys, so repeat
                    this process in each of them to see how well you've internalised the
                    sound of the tonic.</p>
                </li>
            </ol>
            <p>Try the entire
                test, and see how you go.</p>
            <p>If you sang the
                tonic correctly in 10, 11 or all 12 keys congratulations, you've
                passed the first module of 80/20 Ear Training! You've taken an
                incredibly important step on the road to relative pitch and more
                creativity and confidence with music.</p>
            <p>If you didn't,
                there's no need to worry. It takes most of our students at least a
                few attempts to pass this test. Simply go back to the internalisation
                exercise to solidify your ability to recognise the sound of the tonic
                and retry after a few more practice sessions. Make sure you check the
                troubleshooting section if you have any specific problems.</p>
        </v-flex>
    </v-layout>
</template>

<script>
    import Teacher from "../components/Teacher";
    export default {
        name: "TonicInternalizationTest",
        components: {Teacher}
    }
</script>

<style scoped>

</style>