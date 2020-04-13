<template>

  <v-container fluid class="cards">
    {{usr}}
    <h2>You are not logged in!</h2>
    <h3>Login or generate a new username to save your progress! <i>TODO: Styling</i></h3>
    <v-row dense>
      <v-col>
        <v-card>
          <v-card-title>Register</v-card-title>
          <v-card-subtitle>Generate a new random username</v-card-subtitle>
          <v-card-text>
            You'll need to save that username somewhere in order to restore your progress. You can allow us to set cookies, so you don't
            need to keep track if you are not deleting your cookies. Alternatively, you can copy a link or create a bookmark
            ending on "
            <b>?usr={{user}}</b>", that directly logs you in and puts you back to where you stopped. We will not save any personal
            data(e.g. names). By checking the below checkmark you allow us to save cookies on your system.
            <v-card-actions>

              <v-btn v-on:click="generate">
                <v-icon>mdi-dice-3</v-icon>
                Generate
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-card-subtitle>Login with an existing username</v-card-subtitle>
          <v-card-text>
            <v-text-field label="Username" append-icon="mdi-account" outlined/>
            <v-card-actions>
              <v-btn>
                <v-icon>mdi-login</v-icon>
                Login
              </v-btn>
              <v-btn>
                Forgot username?
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

  import api from "../api.js"

  export default {
    name: 'LoginPanel',
    mixins: [api],
    props: [
      'connected',
      'usr'],
    data: () => ({
        usr: 'none'
    }),
    methods: {
      generate: function() {
        this.generateUserName()
      },
      updateNavBarUsername:function(){
        this.$parent.updateUser();
      }
    },
    
    created: function() {
      this.getCurrentUser()
        .then(usr => this.usr = usr);
      
    }
    
  }

</script>

<style scoped>

  .cards {
    width: 80%;
  }

</style>