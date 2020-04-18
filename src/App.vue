<template>
  <v-app id="inspire">
    <component :is="layout">

    </component>
  </v-app>

</template>

<script>
  import api from './api.js';
  const default_layout = 'default';
  
  export default {
    name: 'Dodeca',
    mixins: [api],
    components: {},
    props: {
      source: String
    },
    data: () => ({
      drawer: null,
      curModule: 0,
      showLoginSnack: false,
      showRegisterSnack: false,
      loginBtnDisabled: false, // workaround against login popping up on logout
      userProp: null,
      takesProp: {},
    }),
    computed: {
      layout: function () {
        return (this.$route.meta.layout || default_layout) + '-layout'
      }
    },
    methods: {
      onLogout: function() {
        const self = this
        setTimeout(function() {
          self.loginBtnDisabled = false
        })
        this.logout()
      }
    },
    watch: {
      userProp: function(val) {
        if (val != null) {
          this.loginBtnDisabled = true
          this.updateTakes()
        } else {
          this.takes = {}
        }
      },
      $route: function()  {
        if(this.userProp != null){
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
          if(logoff_id != null){
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
    created: function() {
      this.updateCurrentUser()
    },
  }

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
    .ear-action
      filter: invert(100%)
  
  .ear-action
    filter: invert(30%)
  .v-list-item--active
    .ear-action
      filter: invert(0%)!important
  .invert-img .v-image__image
    filter: invert(100%)
  .v-list
    padding: 0px
</style>
