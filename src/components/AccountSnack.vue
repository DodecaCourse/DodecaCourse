<template>
    <div>
        <v-container fluid class="cards">
            <v-snackbar
                    v-model="show"
                    vertical
                    :timeout="0"
                    color="info"
            >
                <h3>Login or generate a new username to save your progress!</h3>
                <v-tabs>
                    <v-tab>Login</v-tab>
                    <v-tab>Register</v-tab>
                    <v-tab-item>
                        <v-card>
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
                                <v-btn style="margin-left: auto">
                                  Forgot username?<i>(TODO)</i>
                                </v-btn>
                              </v-card-actions>
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                    <v-tab-item>
                        <v-card>
                            <v-card-subtitle>Generate a new random username</v-card-subtitle>
                            <v-card-text>
                                You'll need to save that username somewhere in order to restore your progress. You can
                                allow us to set cookies, so you don't
                                need to keep track if you are not deleting your cookies. Alternatively, you can copy a
                                link or create a bookmark
                                ending on "
                                <b>?usr={{usr}}</b>", that directly logs you in and puts you back to where you stopped.
                                We will not save any personal
                                data(e.g. names). By checking the below checkmark you allow us to save cookies on your
                                system.
                                <v-card-actions>

                                    <v-btn v-on:click="generate">
                                        <v-icon>mdi-dice-3</v-icon>
                                        Generate
                                    </v-btn>
                                </v-card-actions>
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                </v-tabs>
                <v-btn
                        text
                        @click="show = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </v-container>
    </div>

</template>

<script>

    import api from "../api.js"

    export default {
        name: 'AccountSnack',
        mixins: [api],
        props: {
          connected: {
            Type: Boolean,
          },
          show: {
            type: Boolean,
            required: true
          }
        },
        // computed: {
          // TODO: Hab hier probiert, mit einer computeten show variable
          // den Vue Warn zu umgehen:
          // [Vue warn]: Avoid mutating a prop directly since the value will be
          // overwritten whenever the parent component re-renders. Instead, use
          // a data or computed property based on the prop's value.
          // Prop being mutated: "show"
          // show: {
          //   get: function() {
          //     return this.show_prop;
          //   },
          //   set: function(val) {
          //     this.$parent.show_prop  =val
          //   }
          // }
        // },
        inject: ['updateUser'],
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
            this.show = false;
            this.updateUser();
          }
        },

        created: function () {
          this.getCurrentUser()
            .then(usr => this.usr = usr);

        }

    }

</script>
