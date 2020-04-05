<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>2. Recognising Individual Notes</h1>
            <h2>Tests</h2>
            <v-banner app elevation="0" id="player" sticky>
                <Teacher t-type="internalization-test"/>
            </v-banner>
            <p>
                Each scale degree has an internalisation test that goes alongside
                it's internalisation exercise.</p>
            <p>The
                internalisation test for each scale degree is just like the
                internalisation test for the tonic from the first module. A I - IV -V
                progression is played for the first two bars, followed by a pause,
                and finally the target scale degree is played before the sequence is
                repeated in a new key.</p>
            <p>You can see the
                first 8 bars from the internalisation test for the second scale
                degree below.</p>
            <p>
                <v-img contain max-height="9.5ch" max-width="90vw" src="/img/m2_c_major_re_intern_test.svg"
                title="First 8 bars from the internalisation test for the second scale degree"/>
            </p>
            <h3>How to use the individual note internalisation tests</h3>
            <p>
                In the internalisation tests in this module we'll add the additional
                step of singing the tonic, just as we did with the internalisation
                exercises.</p>
            <p>This creates two
                'difficulty levels' with the internalisation tests.</p>
            <h4>1. Sing the tonic</h4>
            <p>In this first
                'difficulty level', you'll sing the tonic before you attempt to sing
                the target scale degree. So you will:</p>
            <ol>
                <li><p><b>Listen to the
                    I - IV - V Progression:</b> Like with the internalisation exercises (and
                    all other exercises in the course) just listen to the I - IV - V
                    progression while it outlines the key.</p></li>
                <li><p><b>Listen for
                    the sound of the target scale degree and hear it clearly in your
                    head:</b> wait until the I - IV - V progression has been played and you
                    hear the tonic chord played again, then identify which note is the
                    tonic and hear it internally.</p></li>
                <li><p><b>Sing the
                    tonic:</b> sing the note you hear as the tonic in your head just as you
                    did in the tonic internalisation exercise.</p></li>
                <li><p><b>Try to hear
                    the sound of the target scale degree clearly in your head:</b> after
                    you've sung the tonic, try to hear the sound of the target scale
                    degree as clearly in your head as you can. You are repeating the
                    movement from the tonic to the target scale degree you've been
                    singing in the internalisation exercise so listen for that sound.</p></li>
                <li><p><b>Sing the
                    target scale degree:</b> if you can hear the target scale degree
                    internally, sing it. Then hold it or repeat it for the next few
                    second.</p></li>
                <li><p><b>Check that
                    you have sung the target scale degree correctly:</b> Listen to the
                    target scale degree when it is played to see if it's the same note
                    as the one you're singing.</p></li>
                <li><p><b>Repeat:</b> The
                    internalisation tests move through all 12 keys, so repeat this
                    process in each of them to see how well you've internalised the
                    sound of each scale degree.</p></li>
            </ol>
            <p>Once you can get
                10 out of 12 keys right at the first difficult level, you're ready to
                move onto the second one.</p>
            <h4>2. Don't sing the tonic</h4>
            <ol>
                <li><p><b>Listen to the
                    I - IV - V Progression:</b> Like with the internalisation exercises (and
                    all other exercises in the course) just listen to the I - IV - V
                    progression while it outlines the key.</p></li>
                <li><p><b>Listen for
                    the sound of the tonic and hear it clearly in your head:</b> wait until
                    the I - IV - V progression has been played and you hear the tonic
                    chord played again, then identify which note is the tonic and hear
                    it internally.</p></li>
                <li><p><b>Try to hear
                    the sound of the target scale degree clearly in your head:</b> once you
                    can hear the tonic clearly in your head, listen for the sound of the
                    target scale degree. You are listening for the same relationship,
                    but you simply haven't sung the tonic.</p></li>
                <li><p><b>Sing the
                    target scale degree:</b> if you can hear the target scale degree
                    internally, sing it. Then hold it or repeat it for the next few
                    second.</p></li>
                <li><p><b>Check that
                    you have sung the target scale degree correctly:</b> Listen to the
                    target scale degree when it is played to see if it's the same note
                    as the one you're singing.</p></li>
                <li><p><b>Repeat:</b> The
                    internalisation exercises move through all 12 keys, so repeat this
                    process in each of them to see how well you've internalised the
                    sound of each scale degree.</p></li>
            </ol>
            <p>Once you can pass
                an internalisation test (sing the target scale degree correctly 10
                out of 12 times), move onto the next internalisation exercise.
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2" to="/individual-notes/internalisation-method">Continue internalising</v-btn>
            <p><br />
                <p>
                Repeat
                this until you've passed the first 4 internalisation tests. Then
                you're read to add the recognition exercises to your practice
                routine.</p>
            <v-btn style="float: right" color="secondary" class="ma-2" to="/individual-notes/recognition-method">Start recognition</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import Teacher from "../components/Teacher";
    export default {
        name: "IndividualNotesTest",
        components: {Teacher}
    }
</script>

<style scoped>

</style>