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
                        <v-list-item-title>Dashboard</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <Courses />
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
            <v-container
                    class="fill-height"
                    fluid
            >
                <router-view></router-view>
            </v-container>
        </v-content>

        <v-footer app>
            <span>&copy; 2019</span>
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
        }),
        created () {
        },
    }
</script>
