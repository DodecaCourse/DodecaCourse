<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>4. Recognising Chords</h1>
            <h2>Diatonic Chords Internalisation</h2>
            <p>
                There is an internalisation exercise for each diatonic triad.
            </p>
            <p>
                The exercises are similar to the internalisation exercises for individual scale degrees. In these
                however, the tonic chord alternates with the target chord in each bar. The target chord is played in two
                separate octaves - the octave above the tonic chord and the octave below.
            </p>
            <p>
                The diagram below shows the internalisation exercise for the ii chord (the chord built on the second scale degree).
            </p>
            <p>
                <v-img  contain max-height="25ch" max-width="83.5vw"
                        src="/img/m4_chord_internalisation_ii.svg"
                        title="Internalisation exercise for the ii chord"/>
            </p>
            <h3>How to use the diatonic chords internalisation exercises</h3>
            <p>
                Follow the steps below for each internalisation exercise:
            </p>
            <ol>
                <li><p>
                    Listen to the <i>I - IV - V</i> chord progression
                </p></li>
                <li><p>
                    Listen to the sound of the movement from the tonic chord to the target chord in each bar
                </p></li>
                <li><p>
                    Sing the root note of the tonic and the target chord (the root note is always the bass note in these exercises)
                </p></li>
            </ol>
            <p>
                Repeat this in each key throughout the exercise.
            </p>
            <p>
                If you find it difficult to accurately sing the root/bass notes of the chords, continue practicing with the targeting tones exercises.
            </p>
            <p>
                Practice with each internalisation exercise for 1-2 sessions, then progress onto the diatonic chords recognition exercises. Return to these internalisation exercises if you find a chord difficult in the recognition exercises.
            </p>
            <h3>Diatonic Triads</h3>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 2, count: 3}"
                        :prog-id="7001" t-type="chord-internalization" hide-test>
                    ii Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 4, count: 3}"
                        :prog-id="7002" t-type="chord-internalization" hide-test>
                    iii Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 5, count: 3}"
                        :prog-id="7003" t-type="chord-internalization" hide-test>
                    IV Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 7, count: 3}"
                        :prog-id="7004" t-type="chord-internalization" hide-test>
                    V Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 9, count: 3}"
                        :prog-id="7005" t-type="chord-internalization" hide-test>
                    vi Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 11, count: 3}"
                        :prog-id="7006" t-type="chord-internalization" hide-test>
                    vii Internalisation
                </InlineConfigurator>
            </p>
            <h3>Diatonic 7th Chords</h3>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 2, count: 4}"
                        :prog-id="7007" t-type="chord-internalization" hide-test>
                    ii7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 4, count: 4}"
                        :prog-id="7008" t-type="chord-internalization" hide-test>
                    iii7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 5, count: 4}"
                        :prog-id="7009" t-type="chord-internalization" hide-test>
                    IVmaj7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 7, count: 4}"
                        :prog-id="7010" t-type="chord-internalization" hide-test>
                    V7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 9, count: 4}"
                        :prog-id="7011" t-type="chord-internalization" hide-test>
                    vi7 Internalisation
                </InlineConfigurator>
            </p>
            <p>
                <InlineConfigurator
                        :config="{degrees: [0, 2, 4, 5, 7, 9, 11], diatonic: 11, count: 4}"
                        :prog-id="7012" t-type="chord-internalization" hide-test>
                    vii7b5 Internalisation
                </InlineConfigurator>
            </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/chords/diatonic-chord-recognition">Next Chapter
            </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "M4DiatonicChordsInternalization",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>