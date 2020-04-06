<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>1. Recognising the Tonic</h1>
            <h2>Overview</h2>
            <p>In this module
                we’ll lay the foundation for fast, effective ear training. You’ll:</p>
            <ul>
                <li>discover the
                    note that acts as the focal point of this entire
                    approach to ear training (and the focal point of all effective ear
                    training approaches) - called the tonic.
                </li>
                <li>begin training your ears by memorising the sound of the tonic so you
                    are able to identify it in music.
                </li>
            </ul>
            <h2>Method</h2>
            <ol>
                <li>
                    <p>Read through the lesson on the tonic to find out what the tonic is
                        and why it’s at the centre of an effective ear training approach.</p>
                </li>
                <li><p>Read the exercise explanations for internalisation exercises</p>
                </li>
                <li><p>Start with
                    the tonic internalisation exercise.</p>
                </li>
                <li><p>Repeat until
                    you feel ready to attempt the tonic internalisation test.</p>
                </li>
                <li><p>Attempt the
                    tonic internalisation test.</p>
                </li>
                <li><p>If you pass the test, continue on to module 2. If you do not, refer to the
                    troubleshooting section</p>
                </li>
            </ol>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/tonic-internalization/tonic">Next Chapter</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        name: "TonicInternalizationOverview",
        mounted: function () {
            if (!this.$teacher.playing) {
                this.$teacher.setupInternalization("1P", false)
            }
        }
    }
</script>

<style scoped>

</style>