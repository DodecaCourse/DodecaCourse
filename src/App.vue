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
                <Courses :cur-course="curCourse" :user="user"/>
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
                app
                clipped-left
                solo
                dense
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title><b>FETT</b></v-toolbar-title>
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
              <v-text-field
                class="shrink"
                outlined
                width="10px"
                height="10px"
                dense
              ></v-text-field>
              <v-btn icon>
                <v-icon>mdi-login</v-icon>
              </v-btn>
            
              
              <v-btn icon>
                <v-icon>mdi-account-plus</v-icon>
              </v-btn>
              <pre>Logged in as: </pre><b>{{user}}</b>
              <v-btn icon>
                <v-icon>mdi-logout</v-icon>
              </v-btn>
              
            </template>
            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            <v-btn v-on:click="$vuetify.theme.dark = !$vuetify.theme.dark" icon title="Toggle Light/Dark">
                <v-icon>mdi-invert-colors</v-icon>
            </v-btn>
            <v-btn icon to="/settings">
              <v-icon>mdi-cog</v-icon>
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
            <LoginPanel :connection="connection" :usr="user"/>
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
    import LoginPanel from "./components/LoginPanel"
    import api from "./api.js"
    
    export default {
      name: "FETT",
      mixins: [
        api
      ],
      components: {
        Teacher,
        Courses,
        LoginPanel
      },
      props: {
          source: String,
      },
      data: () => ({
          drawer: null,
          user: 'not logged in',
          curCourse: 0
      }),
      methods: {
        updateUser: function() {
          this.getCurrentUser()
            .then(res => this.user = res);
        }
      },
      created: function() {
        this.updateUser();
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

    .invert-img .v-image__image
        filter: invert(100%)

</style>
