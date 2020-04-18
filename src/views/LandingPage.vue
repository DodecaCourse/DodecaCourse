<template>
    <v-layout
            column
            align-center
            justify-center
            fill-height
    >
            <v-layout
                    column
                    align-center
                    justify-center
                    class="main flex-grow-0">
            <LandingCircle :enabled-buttons="[0,2,4,5,7,9,11]"
                           :labels="['Do', 'Ra', 'Re', 'Me', 'Mi', 'Fa', 'Fi', 'So', 'Le', 'La', 'Te', 'Ti']">
                <template v-slot:content>
                    <div>
                    <h1 class="text-center"><b>Dodeca</b></h1>
                    <span class="text-center">Hearing is Relative</span></div>
                </template>
            </LandingCircle>

                <h3 class="text-center mt-4" v-if="$vuetify.breakpoint.height > 415">Functional Ear Training Course - Free & Online</h3>
            <v-btn
                    :class="{'mt-12': $vuetify.breakpoint.height > 500}"
                    color="primary"
                    dark
                    large
                    href="/intro"
            >
                Get Started
            </v-btn>
            </v-layout>
        <div class="sp-footer white--text">
                <span>&copy;2020 <router-link to="/impressum.html">Impressum & Datenschutz</router-link></span>
        </div>
    </v-layout>
</template>

<script>
    import LandingCircle from "../components/LandingCircle";
    export default {
        name: "LandingPage",
        components: {LandingCircle},
    }
</script>

<style scoped lang="sass">
    .main
        max-width: 90vw
        margin-bottom: 4ch

    .sp-footer
        background-color: rgba(0,0,0, 0.25)
        width: 100%
        padding: 0.4ch
        text-align: center
        position: absolute
        bottom: 0
</style>
