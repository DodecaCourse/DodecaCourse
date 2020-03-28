<template>
    <p>Player</p>
</template>

<script>
    /* global MIDI */
    export default {
        name: "InternalizationPlayer",
        created: function () {
            MIDI.loadPlugin({
                soundfontUrl: "https://gleitz.github.io/midi-js-soundfonts/FluidR3_GM/",
                instrument: "acoustic_grand_piano",
                onprogress: function (state, progress) {
                    console.log(state, progress);
                },
                onsuccess: function () {
                    var delay = 0; // play one note every quarter second
                    var note = 66; // the MIDI note
                    var velocity = 127; // how hard the note hits
                    // play the note
                    MIDI.setVolume(0, 127);
                    MIDI.noteOn(0, note, velocity, delay);
                    MIDI.noteOff(0, note, delay + 0.75);
                    MIDI.noteOn(0, note + 7, velocity, delay + 0.75);
                    MIDI.noteOff(0, note + 7, delay + 2 * 0.75);
                }
            });
        }
    }
</script>

<style scoped>

</style>