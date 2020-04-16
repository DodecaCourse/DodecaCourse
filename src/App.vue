<template>
    <v-app id="inspire">
        <v-navigation-drawer
                v-model="drawer"
                app
                clipped
        >
            <v-layout align-center justify-space-between column fill-height>
            <v-list dense>
                <v-list-item to="/" link>
                    <v-list-item-action>
                        <v-icon>mdi-book-music</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Introduction</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <Courses :cur-course="curCourse" />
            </v-list>
            <div class="justify-end v-footer" style="text-align: center" :class="$vuetify.theme.dark ? 'theme--dark' : 'theme--light'">
                <span>Structure & Content based on <a href="https://eartraininghq.com/">Ear Training HQ</a></span>
            </div>
            </v-layout>
        </v-navigation-drawer>

        <v-app-bar
                flat
                app
                clipped-left
                dense
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title><b>Dodeca</b></v-toolbar-title>
            <i class="mx-2 hidden-xs-only">Hearing is Relative!</i>
            <v-spacer></v-spacer>
            <v-btn v-on:click="$vuetify.theme.dark = !$vuetify.theme.dark" icon title="Toggle Light/Dark">
                <v-icon>mdi-invert-colors</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
            <v-container fluid>
                <v-banner app elevation="0" id="player_banner"
                          v-show="!(this.$refs.teacher !== undefined && this.$refs.teacher.hidden)">
                    <Teacher ref="teacher"/>
                </v-banner>
            <router-view>
            </router-view>
            </v-container>
        </v-content>

        <v-footer app>
            <span>&copy;2020 <router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>
                </span>
        </v-footer>
    </v-app>
</template>

<script>
    import Courses from "./components/Courses";
    import Teacher from "./components/Teacher";

    export default {
        components: {Teacher, Courses},
        props: {
            source: String,
        },
        data: () => ({
            drawer: null,
            curCourse: 0,
        }),
    };
</script>

<style lang="sass">
    @import '../node_modules/typeface-roboto/index.css'
    .article
        max-width: 43em!important

    #player_banner .v-banner__text
        width: 100%

    #player_banner .v-banner__wrapper
        padding-bottom: 0
        padding-top: 0

    .invert-img .v-image__image
        filter: invert(100%)

</style>
