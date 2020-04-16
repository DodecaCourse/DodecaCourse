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
                <Modules :cur-Module="curModule"/>
                <v-list-item to="/dev/servertest" link>
                    <v-list-item-action>
                        <v-icon>mdi-bash</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Backend</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
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
                solo
                dense
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title><b>Dodeca</b></v-toolbar-title>
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
                  v-on:click="showAccountSnack=!(showAccountSnack || loginBtnDisabled)"
                >
                  <v-icon>mdi-login</v-icon>
                  
                </v-btn>
              </template>
              <template v-else>
                <span>Logged in as <b>{{userProp.user_keyword}}</b></span>
                <v-btn icon>
                  <v-icon v-on:click="onLogout">mdi-logout</v-icon>
                </v-btn>
              </template>
              
            </template>
            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
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
                <router-view></router-view>
                
            </v-container>
            <v-container fluid>
              <h2 v-if="!connection" class="ma-2">
                <v-icon>mdi-alert</v-icon> Warning:<br>
                You are not connected to the server.<br>
                Your progress will not be saved!<br>
                Please contact an admin.
              </h2>
            </v-container>
            <AccountSnack
              :show="showAccountSnack"
              :on-close="function () {showAccountSnack = false}"
            />
            
        </v-content>

        <v-footer app>
            <span>&copy;2020 <router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>
                </span>
        </v-footer>
    </v-app>
</template>

<script>
    import Modules from "./components/Modules";
    import Teacher from "./components/Teacher";
    import AccountSnack from "./components/AccountSnack";
    import api from "./api.js"
    
    export default {
      name: "FETT",
      mixins: [
        api
      ],
      components: {
        Teacher,
        Modules,
        AccountSnack
      },
      props: {
          source: String,
      },
      data: () => ({
          drawer: null,
          curModule: 0,
          showAccountSnack: false,
          loginBtnDisabled: false, // workaround against login popping up on logout
          userProp: null,
          takesProp: {},
      }),
      methods: {
          onLogout: function () {
            const self = this;
            setTimeout(function () {
                self.loginBtnDisabled = false;
            });
            this.logout();
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
          }
      },
      created: function() {
          this.updateCurrentUser();
      }
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

      
  .theme--dark
    .v-banner__wrapper
      background-color: #121212
    .v-banner__wrapper .v-sheet
      background-color: #121212

  .invert-img .v-image__image
    filter: invert(100%)
</style>
