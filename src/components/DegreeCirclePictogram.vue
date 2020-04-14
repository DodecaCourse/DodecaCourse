<template>
    <div :title="description" class="circle-div"
         :style="'width: ' + (2 * rad + 2 * degrad) + 'px; height: ' + (2 * rad + 2 *degrad) + 'px;'">
        <svg class="circle-svg" :style="'width: ' + (2 * rad + 2 * degrad) + 'px; height: ' + (2 * rad + 2 *degrad) + 'px;'">
            <circle v-for="i in this.degrees"
                    v-bind:key="i.degree"
                    class="v-btn elevation-1"
                    :class="{btnEnabled: i.enabled, btnDisabled: !i.enabled}"
                    :cx="Math.sin(2/12 * Math.PI * i.degree) * rad + rad + degrad"
                    :cy="-Math.cos(2/12 * Math.PI * i.degree) * rad + rad + degrad" :r="degrad"
                    :fill="i.enabled ? $vuetify.theme.currentTheme.primary : ($vuetify.theme.dark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.12)')"
                    :style="'background-color: ' + $vuetify.theme.dark ? 'rgba(255,255,255,0.12)' : 'rgba(0,0,0,0.12)'"
            />
        </svg>
        <div id="inner-content"
             :style="'width: ' + (2 * rad - 2 * degrad) + 'px; height: ' + (2 * rad - 2 *degrad) + 'px; left: ' + 2 * degrad + 'px; top: ' + 2 * degrad + 'px;'">
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
                    { degree: 0, display: "Do", enabled: true },
                    { degree: 1, display: "Ra", enabled: true },
                    { degree: 2, display: "Re", enabled: true },
                    { degree: 3, display: "Me", enabled: true },
                    { degree: 4, display: "Mi", enabled: true },
                    { degree: 5, display: "Fa", enabled: true },
                    { degree: 6, display: "Fi", enabled: true },
                    { degree: 7, display: "So", enabled: true },
                    { degree: 8, display: "Le", enabled: true },
                    { degree: 9, display: "La", enabled: true },
                    { degree: 10, display: "Te", enabled: true },
                    { degree: 11, display: "Ti", enabled: true }
                ],
                rad: 16,
                degrad: 4,
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
    //standard template for the btns
    .normal-btn
        text-transform: none !important
        position: absolute


    .circle-div
        position: relative

    .circle-svg
        pointer-events: none

    #inner-content
        position: absolute
        display: table

    #inner-content *
        text-align: center
        display: table-cell
        vertical-align: middle
</style>
