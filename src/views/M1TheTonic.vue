<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>1. Recognising the Tonic</h1>
            <h2>The tonic</h2>
            <p>
                The tonic is the central note of a piece of music. It sounds the most
                stable and at rest. The tonic is generally played at the end of a
                piece of music to give it a sense of resolution and acts as the
                reference point for the key of a piece of music: the tonic of a piece
                in the key of A major is A.</p>
            <p>The tonic is the
                essential starting point for ear training because of that stable
                sound it has. With a little practice we can learn to identify the
                tonic when we hear it in music and then we can use it as a reference
                point to identify every other note and chord we hear.</p>
            <p>Once you’re able
                to identify the tonic you can start learning to identify other notes
                and chords based on the interval that separates them from the tonic.
                But we’ll get to that in the next module.</p>
            <p>First we need to
                be able to confidently identify which note is the tonic. And that’s
                precisely the goal of this first module.</p>
            <p>We’ll
                do that with an exercise called an internalisation exercise.</p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/tonic-internalization/exercise">Next Chapter</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        name: "TonicInternalizationMethod",
        mounted: function () {
            if (!this.$teacher.playing) {
                this.$teacher.setupInternalization(0, false)
            }
        }
    }
</script>

<style>
</style>