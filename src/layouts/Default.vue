<template>
    <div>
        <v-navigation-drawer v-model="drawer" app clipped>
            <v-layout align-center justify-space-between column fill-height>
                <v-list dense width="100%">
                    <v-list-item v-if="this.userProp != null" to="/home" link>
                        <v-list-item-action>
                            <v-img class="ear-action" src="/img/ear_mask.svg" height="35px" width="10px"></v-img>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Your Ear</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item to="/" link>
                        <v-list-item-action>
                            <v-icon>mdi-book-music</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title>Introduction</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <Modules :cur-Module="curModule"/>
                </v-list>
                <div class="justify-end v-footer" style="text-align: center"
                     :class="$vuetify.theme.dark ? 'theme--dark' : 'theme--light'">
                    <span>Structure & Content based on <a href="https://eartraininghq.com/">Ear Training HQ</a></span>
                </div>
            </v-layout>
        </v-navigation-drawer>

        <v-app-bar flat app clipped-left solo dense>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
            <v-toolbar-title :class="{'hidden-xs-only': user != null}"><b>Dodeca</b></v-toolbar-title>
            <i class="mx-2 hidden-xs-only">Hearing is Relative!</i>
            <v-spacer></v-spacer>
            <template v-if="!connection">
                <v-chip
                        class="ma-2"
                        text-color="white"
                        color="red"
                >
                    Disconnected
                    <v-icon right>mdi-server-network-off</v-icon>
                </v-chip>
            </template>
            <template v-if="connection">
                <template v-if="userProp == null">
                    <v-btn
                            icon
                            title="Login with your keyword"
                            v-on:click="showLoginSnack=!(showLoginSnack || loginBtnDisabled)"
                    >
                        <v-icon>mdi-login</v-icon>

                    </v-btn>
                    <v-btn icon title="Get your keyword"
                           v-on:click="showRegisterSnack=!(showRegisterSnack || loginBtnDisabled)"
                    >
                        <v-icon>mdi-account-plus</v-icon>
                    </v-btn>
                </template>
                <template v-else>
                    <span>Logged in as <b>{{userProp.user_keyword}}</b></span>
                    <v-btn icon>
                        <v-icon v-on:click="onLogout">mdi-logout</v-icon>
                    </v-btn>
                </template>

            </template>
            <!-- <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn> -->
            <v-btn v-on:click="$vuetify.theme.dark = !$vuetify.theme.dark" icon title="Toggle Light/Dark">
                <v-icon>mdi-invert-colors</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
            <v-container fluid>
                <v-banner app
                          elevation="0"
                          id="player_banner"
                          v-show="!(this.$refs.teacher !== undefined && this.$refs.teacher.hidden)">
                    <Teacher ref="teacher"/>
                </v-banner>
                <router-view></router-view>

            </v-container>
            <v-container fluid>
                <h2 v-if="!connection" class="ma-2">
                    <v-icon>mdi-alert</v-icon>
                    Warning:<br> You are not connected to the server.<br> Your progress will not be saved!<br> Please
                    contact an admin.
                </h2>
            </v-container>
            <LoginSnack :show="showLoginSnack"
                        :on-close="function () {showLoginSnack = false}"/>
            <RegisterSnack :show="showRegisterSnack"
                           :on-close="function () {showRegisterSnack = false}"/>

        </v-content>

        <v-footer app>
      <span>&copy;2020 <router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>
                  </span>
        </v-footer>
    </div>
</template>

<script>
    import Modules from "../components/Modules";
    import Teacher from "../components/Teacher";
    import LoginSnack from "../components/LoginSnack";
    import RegisterSnack from "../components/RegisterSnack";

    export default {
        name: "Default",
        components: {RegisterSnack, LoginSnack, Teacher, Modules}
    }
</script>

<style scoped>

</style>