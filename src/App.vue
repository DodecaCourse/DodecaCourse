<template>
    <v-app id="inspire">
        <v-navigation-drawer
                v-model="drawer"
                app
                clipped
        >
            <v-list dense>
                <v-list-item to="/" link>
                    <v-list-item-action>
                        <v-icon>mdi-view-dashboard</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Introduction</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <Courses :cur-course="curCourse" />
                <v-list-item to="/teacher-playground" link>
                    <v-list-item-action>
                        <v-icon>mdi-animation-play</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Playground</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                app
                clipped-left
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title>FETT</v-toolbar-title>
        </v-app-bar>

        <v-content>
            <v-container fluid>
                <v-banner app elevation="0" id="player_banner">
                    <Teacher ref="teacher"/>
                </v-banner>
            <router-view>
            </router-view>
            </v-container>
        </v-content>

        <v-footer app>
            <span><router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>
                &copy; 2020, Structure & Content based on <a href="https://eartraininghq.com/">Ear Training HQ</a></span>
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

<style>
    .article {
        max-width: 43em!important;
    }
    #player_banner .v-banner__text {
        width: 100%
    }
    #player_banner .v-banner__wrapper {
        padding-bottom: 0;
        padding-top: 0;
    }
</style>
