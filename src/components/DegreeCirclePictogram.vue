<template>
    <div :title="description">
        <div class="div-circle-pict" @click="function() {
            console.log('Click');
        }">
            <v-btn
                    v-for="i in this.degrees"
                    v-bind:key="i.display"
                    :class="'normal-btn normal-btn--' + (i.degree + 1)"
                    :color="i.enabled ? 'primary' : 'secondary'"
                    :disabled="!i.enabled"
                    x-small
                    fab
                    :elevation="i.degree === 0 ? 15 : 0"
            />
        </div>
        <div id="inner-content">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "DegreeCirclePictogram",

        props: {
            enabledDegrees: {
                type: Array,
                required: true,
            }
        },

        data: function() {
            return {
                //database for the intervals/degrees, "name" chosen to fit TonalJS, display is the name of
                //Solfege and shown on btns
                degrees: [
                    { degree: 0, name: "1P", display: "Do", enabled: true },
                    { degree: 1, name: "2m", display: "Ra", enabled: true },
                    { degree: 2, name: "2M", display: "Re", enabled: true },
                    { degree: 3, name: "3m", display: "Ma", enabled: true },
                    { degree: 4, name: "3M", display: "Mi", enabled: true },
                    { degree: 5, name: "4P", display: "Fa", enabled: true },
                    { degree: 6, name: "4A", display: "Fi", enabled: true },
                    { degree: 7, name: "5P", display: "So", enabled: true },
                    { degree: 8, name: "6m", display: "Le", enabled: true },
                    { degree: 9, name: "6M", display: "La", enabled: true },
                    { degree: 10, name: "7m", display: "Ta", enabled: true },
                    { degree: 11, name: "7M", display: "Ti", enabled: true }
                ],
            };
        },

        computed: {
            description: function () {
                var ret = "";
                for (let l=0; l<this.degrees.length; l++) {
                    if(this.degrees[l].enabled) {
                        ret += this.degrees[l].display + " "
                    }
                }
                return ret
            }
        },

        watch: {
            enabledDegrees: function (newVal) {
                for (let l=0; l<this.degrees.length; l++) {
                    this.degrees[l].enabled = newVal.indexOf(this.degrees[l].degree) > -1;
                }
            }
        },
        mounted: function () {
            for (let l=0; l<this.degrees.length; l++) {
                this.degrees[l].enabled = this.enabledDegrees.indexOf(this.degrees[l].degree) > -1;
            }
        }
    };
</script>

<style scoped lang="sass">
    @use "sass:math"
    @use "sass:list"

    //parameters for the DegreeCircles' position and size
    $radius: 62
    $btnrad: 32
    $centerX: $radius
    $centerY: $radius
    $scale: 1/4

    //math values for computing the respective positions of the btns
    $sin: 0, 0.5, 0.866, 1, 0.866, 0.5, 0, -0.5, -0.866, -1, -0.866, -0.5
    $cos: 1, 0.866, 0.5, 0, -0.5, -0.866, -1, -0.866, -0.5, 0, 0.5, 0.866

    //because I was stupid
    $indices: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

    //instanciates each individual btn with its position
    @each $i in $indices
        .normal-btn--#{$i}
            left: math.floor(nth($sin, $i) * $radius + $centerX) * 1px
            top: math.floor(-1 * nth($cos, $i) * $radius + $centerY) * 1px


    //standard template for the btns
    .normal-btn
        text-transform: none !important
        position: absolute

    //class which contains the DegreeCircle
    .div-circle-pict
        position: relative
        transform: scale($scale, $scale)
        transform-origin: top left
        width: (2px * $radius + 1px * $btnrad) * $scale
        height: (2px * $radius + 1px * $btnrad) * $scale
        pointer-events: none

    #inner-content
        position: absolute
        left: (math.floor(nth($sin, 12) * $radius + $centerX) * 2px) * $scale
        top: (math.floor(-1 * nth($cos, 11) * $radius + $centerY) * 2px) * $scale
        width: ($radius * 1.2px) * $scale
        height: ($radius * 1.2px) * $scale
        display: table

    #inner-content *
        text-align: center
        display: table-cell
        vertical-align: middle
</style>
