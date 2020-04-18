<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1 class="hidden-xs-only">1. Recognising the Tonic</h1>
            <h2>Test</h2>
            <p>
                The tonic internalisation test gives you a way to easily tell when
                you have successfully internalised the sound of the tonic so you can
                move onto module 2.</p>
            <p>Just like the
                internalisation exercise, the tonic internalisation test is made up
                of a sequence that is repeated throughout the exercise. This time
                it's an 8 bar sequence:</p>
            <p>
                <v-img contain :class="{'invert-img': $vuetify.theme.dark}"
                       max-height="10.5ch"
                       max-width="83.5vw" src="/img/m1_c_major_tonic_intern_test.svg"
                       title="The first 8 bars of the tonic internalisation test"/>
            </p>
            <p>The tonic
                internalisation test can be broken down into 3 sections:</p>
            <p><b>Bars 1-2:</b>
                Establish one note as the tonic</p>
            <p>Just like in the
                internalisation exercise, a note is established as the tonic using
                the <i>I - IV - V - I</i> progression.</p>
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
                The 8 bar sequence is repeated in a new randomly chosen key.
                The diagram below shows an example of the first 24 bars of the tonic
                internalisation test:</p>
            <p>
                <v-img contain :class="{'invert-img': $vuetify.theme.dark}"
                       max-height="55ch"
                       max-width="83.5vw" src="/img/m1_tonic_intern_test_24bars.svg"
                       title="The first 24 bars of the tonic internalisation test"/>
            </p>
            <h3>How to use the tonic internalisation test</h3>
            <p>
                Start the player by hitting »Test« below to listen to the internalisation test while you read the instructions.
            </p>
            <p>
                <InlineConfigurator :prog-id="1001" t-type="internalization"
                                    :config="{degree: 0}">
                    Tonic Internalisation
                </InlineConfigurator>
            </p>
            <ol>
                <li><p><b>Listen to the
                    <i>I - IV - V - I</i> Progression:</b> Like with the internalisation exercises (and
                    all other exercises in the Dodeca course) just listen to the <i>I - IV - V - I</i>
                    progression while it outlines the key.</p>
                </li>
                <li><p><b>Listen for
                    the sound of the tonic and hear it clearly in your head:</b> wait until
                    the <i>I - IV - V - I</i> progression has been played and you hear the tonic
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
                    tonic internalisation exercise moves randomly through the keys.</p>
                </li>
            </ol>
            <p>Restart the test, do 12 keys and see how you go.</p>
            <p>If you sang the
                tonic correctly in 10, 11 or all 12 keys, congratulations, you've
                passed the first module! You've taken an
                incredibly important step on the road to relative pitch and more
                creativity and confidence with music.
            </p>
            <p>If you didn't,
                there's no need to worry. It takes most students at least a
                few attempts to pass this test. Simply go back to the
                <router-link to="/tonic-internalization/exercise">internalisation exercise</router-link>
                to solidify your ability to recognise the sound of the tonic
                and retry after a few more practice sessions. Make sure you check the
                troubleshooting section if you have any specific problems.</p>
            <p>
                <b>Want to save your progress as you make your way through the Dodeca Course?</b>
            </p>
            <p>
                Generate a username by hitting <v-icon>mdi-account-plus</v-icon> in the top right corner.
                It's free and no personal information is required.
            </p>
            <v-btn style="float: right" color="secondary" class="mx-3"
                   to="/individual-notes/overview">Next module</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "TonicInternalizationTest",
        components: {InlineConfigurator},
        mounted: function () {
            if (!this.$teacher.playing) {
                this.$teacher.setupInternalization(0, false)
            }
        }
    }
</script>

<style scoped>

</style>