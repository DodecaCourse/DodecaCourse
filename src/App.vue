<template>
  <v-app id="inspire">
    <template v-if="layout === 'landing-layout'">
      <LandingLayout />
    </template>
    <template v-else>
      <v-navigation-drawer
        v-model="drawer"
        app
        clipped
      >
        <v-layout
          align-center
          justify-space-between
          column
          fill-height
        >
          <v-list
            dense
            width="100%"
          >
            <v-list-item
              v-if="userProp != null"
              to="/home"
              link
            >
              <v-list-item-action>
                <v-img
                  class="ear-action"
                  src="/img/ear_mask.svg"
                  height="35px"
                  width="10px"
                />
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Your Ear</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item
              to="/intro"
              link
            >
              <v-list-item-action>
                <v-icon>mdi-book-music</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Introduction</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <Modules :cur-module="curModule" />
          </v-list>
          <div
            class="justify-end v-footer"
            style="text-align: center"
            :class="$vuetify.theme.dark ? 'theme--dark' : 'theme--light'"
          >
            <span>Structure & Content based on <a
              href="https://eartraininghq.com/"
            >Ear Training HQ</a></span>
          </div>
        </v-layout>
      </v-navigation-drawer>

      <v-app-bar
        flat
        app
        clipped-left
        solo
        dense
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        <v-toolbar-title :class="{'hidden-xs-only': user != null}">
          <b>Dodeca</b>
        </v-toolbar-title>
        <i class="mx-2 hidden-xs-only">Hearing is Relative!</i>
        <v-spacer />
        <template v-if="!connection">
          <v-chip
            class="ma-2"
            text-color="white"
            color="red"
          >
            Disconnected
            <v-icon right>
              mdi-server-network-off
            </v-icon>
          </v-chip>
        </template>
        <template v-if="connection">
          <template v-if="userProp == null">
            <v-btn
              icon
              title="Login with your keyword"
              @click="showLoginSnack=!(showLoginSnack || loginBtnDisabled)"
            >
              <v-icon>mdi-login</v-icon>
            </v-btn>
            <v-btn
              icon
              title="Get your keyword"
              @click="showRegisterSnack=!(showRegisterSnack || loginBtnDisabled)"
            >
              <v-icon>mdi-account-plus</v-icon>
            </v-btn>
          </template>
          <template v-else>
            <span>Logged in as <b>{{ userProp.user_keyword }}</b></span>
            <v-btn
              icon
              title="Logout"
            >
              <v-icon @click="onLogout">
                mdi-logout
              </v-icon>
            </v-btn>
          </template>
        </template>
        <!-- <v-btn icon>
                  <v-icon>mdi-heart</v-icon>
                </v-btn> -->
        <v-btn
          icon
          title="Toggle Light/Dark"
          @click="$vuetify.theme.dark = !$vuetify.theme.dark"
        >
          <v-icon>mdi-invert-colors</v-icon>
        </v-btn>
      </v-app-bar>

      <v-content>
        <v-container fluid>
          <v-banner
            v-show="!(this.$refs.teacher !== undefined && this.$refs.teacher.hidden)"
            id="player_banner"
            app
            elevation="0"
          >
            <Teacher ref="teacher" />
          </v-banner>
          <router-view />
        </v-container>
        <!--
                <v-container fluid>
                    <h2 v-if="!connection" class="ma-2">
                        <v-icon>mdi-alert</v-icon>
                        Warning:<br> You are not connected to the server.<br> Your progress will not be saved!<br>
                        Please
                        contact an admin.
                    </h2>
                </v-container>
                -->

        <LoginSnack
          :show="showLoginSnack"
          :on-close="function () {showLoginSnack = false}"
        />
        <RegisterSnack
          :show="showRegisterSnack"
          :on-close="function () {showRegisterSnack = false}"
        />
      </v-content>
      <v-footer app>
        <span>
          &copy;2020 <a
            href="/impressum.html"
            class="pr-1"
          >Impressum & Datenschutz</a>
        </span>
      </v-footer>
    </template>
  </v-app>
</template>

<script>
import LandingLayout from "./layouts/LandingLayout";
const default_layout = "default";

import Modules from "./components/Modules";
import Teacher from "./components/Teacher";
import LoginSnack from "./components/LoginSnack";
import api from "./api.js";
import RegisterSnack from "./components/RegisterSnack";

export default {
  name: "Dodeca",
  components: {
    LandingLayout,
    RegisterSnack,
    Teacher,
    Modules,
    LoginSnack,
  },
  mixins: [api],
  data: () => ({
    drawer: null,
    curModule: 0,
    showLoginSnack: false,
    showRegisterSnack: false,
    loginBtnDisabled: false, // workaround against login popping up on logout
    userProp: null,
    takesProp: {}
  }),
  computed: {
    layout: function () {
      return (this.$route.meta.layout || default_layout) + "-layout";
    }
  },
  watch: {
    userProp: function (val) {
      if (val != null) {
        this.loginBtnDisabled = true;
        this.updateTakes();
      } else {
        this.takes = {};
      }
    },
    $route: function () {
      if (this.userProp != null) {
        var logoff_id = null;
        // console.log(this.$route.path);
        this.modules.forEach(module => {
          module.chapters.forEach(chapter => {
            // console.log(module.path + chapter.path);
            if (this.$route.path.startsWith(module.path + chapter.path)) {
              logoff_id = chapter.id;
            }
          });
        });
        if (logoff_id != null) {
          //alert(logoff_id);
          // Problem: user is not defined anymore on beforeDetroy
          // issue an extra updateCurrentUser()?
          // this.updateCurrentUser(); doesnt Work
          // maybe run this inside App.vue?
          // (was inside ModuleItem before)

          // Problem: The view function did not return a valid response.
          // The function either returned None or ended without a return statement.
          // Meaning that the flask app cant build a response to a destroyed
          // application
          // Tried removing return statements

          // For now, trying with a watch on route!
          // (was inside beforeDestroy before)
          this.userProp.logoff_chapter = logoff_id;
          this.setLogoffChapter(logoff_id);
        }
      }
    }
  },
  created: function () {
    this.updateCurrentUser();
  },
  methods: {
    onLogout: function () {
      const self = this;
      setTimeout(function () {
        self.loginBtnDisabled = false;
      });
      this.logout();
    }
  },
};

</script>

<style lang="sass">

    @import '../node_modules/typeface-roboto/index.css'

    .article
        max-width: 43em !important

    #player_banner .v-banner__text
        width: 100%

    #player_banner .v-banner__wrapper
        padding-bottom: 0
        padding-top: 0

    .theme--dark
        .v-banner__wrapper
            background-color: #121212

        .v-banner__wrapper .v-sheet
            background-color: #121212

        .ear-action
            filter: invert(100%)

    .ear-action
        filter: invert(30%)

    .v-list-item--active .theme--light
        .ear-action
            filter: invert(0%) !important

    .invert-img .v-image__image
        filter: invert(100%)

    .v-list
        padding: 0px
</style>
