<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>5. Minor Keys</h1>
            <h2>Solfège in Minor Keys</h2>
            <p>In minor keys, you can choose from two sets of
                <a href="https://en.wikipedia.org/wiki/Solf%C3%A8ge#Minor">solfège syllables</a>.</p>
            <p>
                La-based minor uses the same syllables as the major scale, but
                starts on »La« as the first scale degree. That works because each minor
                scale can be derived from a major scale, beginning on the sixth degree.
                This approach makes transposing to the
                <a href="https://en.wikipedia.org/wiki/Relative_key">relative key</a>,
                the corresponding major with the same key signature, really easy, but
                makes it difficult to transpose to other keys.
            </p>
            <p>
                Do-based minor starts on »Do« and uses the syllables »Me« for the lowered third,
                »Le« for the lowered sixth and »Te« for the lowered seventh. Using this approach,
                it is easy to change between
                <a href="https://en.wikipedia.org/wiki/Parallel_key">parallel keys</a>, where
                the tonic stays the same but the keys changes. It's also easier to apply it
                to other scales, which you will probably encounter during your musical journey.
                Therefore, we will be using Do-based minor in this section of the course.
            </p>
            <p>
                If you need the possibility to use La-based minor, just drop me a note, it
                will be possible to add this as an option.
            </p>
            <p>
                Now you're prepared to get started with the exercises:
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                       to="/minor/ex-tests">Next Chapter
            </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        name: "M5SolfegeMinor"
    }
</script>

<style scoped>

</style>