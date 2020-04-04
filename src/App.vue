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
                        <v-icon>mdi-book-music</v-icon>
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
                <v-list-item to="/dev/servertest" link>
                    <v-list-item-action>
                        <v-icon>mdi-bash</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Backend</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                flat
                dark
                app
                clipped-left
                dense
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title>FETT</v-toolbar-title>
            <v-spacer></v-spacer>
            <pre>Logged in as: </pre><b>{{user}}</b>
            <v-btn icon>
              <v-icon>mdi-logout</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <v-btn icon to="/settings">
              <v-icon>mdi-cog</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
            <v-container fluid>
            <router-view></router-view>
            </v-container>
        </v-content>

        <v-footer app>
            <span><router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>, &copy; 2020, Structure & Content based on <a href="https://eartraininghq.com/">Ear Training HQ</a></span>
        </v-footer>
    </v-app>
</template>

<script>
    import Courses from "./components/Courses";
    export default {
        components: {Courses},
        props: {
            source: String,
        },
        data: () => ({
            drawer: null,
            curCourse: 0,
            user: "2Tfv6"
        }),
        created () {
        },
    }
</script>

<style>
    .article {
        max-width: 43em!important;
    }
</style>
