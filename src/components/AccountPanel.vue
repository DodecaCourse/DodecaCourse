<template>
  <v-container v-if="!success" fluid class="panel">
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
            <b>?usr=USERNAME</b>", that directly logs you in and puts you back to where you stopped. We will not save any personal
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
            <v-text-field
              label="Username"
              name="txtfld"
              v-model="txtfld"
              @input="updateEnableLogin"
              append-icon="mdi-account"
              outlined
            />
            <v-card-actions>
              <v-btn v-on:click="loginUser" :disabled="!login_enabled" primary>
                <v-icon>mdi-login</v-icon>
                Login
              </v-btn>
              <v-btn>
                Forgot username?<i>(TODO)</i>
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
    <!-- TODO: Success Info
    <v-container v-if="success" class="panel">
      <h2>Success!</h2>
      <p>You are now logged in as</p>
      <h1><b>{{usr}}</b></h1>
      <p>Your custom url:</p>
      <p>...</p>
      <p>You can now continue your learning journey! Have fun and remember your
        username! </p>
    </v-container>
    -->
</template>

<script>

  import api from "../api.js"

  export default {
    name: 'AccountPanel',
    mixins: [api],
    inject: ['updateUser'],
    props: [
      'connection'
    ],
    data: () => ({
        usr: 'none',
        txtfld: '',
        login_enabled: false
    }),
    methods: {
      generate: function() {
        this.generateUser()
          .then(u => {
            console.log(u);
            this.setCurrentUser(u)
              .then(res => {
                console.log(res);
                // this.updateCurrentUser();
                this.updateParentUsername();
              });
          });
      },
      loginUser: function() {
        this.setCurrentUser(this.txtfld)
          .then(res => {
            console.log(res);
            this.updateParentUsername();
          });
      },
      updateEnableLogin: function() {
        console.log(this.txtfld.length)
        if(this.txtfld.length == 4){
          this.getUserID(this.txtfld.trim())
            .then(data => {
              this.founduser = data;
              if (!(this.founduser.user_id == null)) {
                this.login_enabled = true;
              } else {
                this.login_enabled = false;
              }
            });
        } else {
          this.login_enabled = false;
        }
        
        
      },
      updateParentUsername:function(){
        this.updateUser();
      }
    },
    
    created: function() {
      this.getCurrentUser()
        .then(usr => this.usr = usr);
      
    }
    
  }

</script>

<style scoped>

  .panel {
    width: 80%;
  }

</style>