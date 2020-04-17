<template>
    <div>
        <v-container fluid class="cards">
            <v-snackbar
                    v-model="showSelf"
                    vertical
                    :timeout="0"
                    color="info"
            >
                <h3>Login or generate a new username to save your progress!</h3>
                <template v-if="user == null">
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
                                autofocus
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
                                <b>?usr={{user}}</b>", that directly logs you in and puts you back to where you stopped.
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
                </template>
                <template v-else>
                    <v-card>
                        <v-card-text>
                        <p>Success! You are now logged in as <b>{{user.user_keyword}}</b>.
                            Your custom url: /?{{user.user_keyword}}<span></span></p>

                        <p>You can now continue your learning journey! Have fun and remember your
                            username! </p>
                        </v-card-text>
                    </v-card>
                </template>
                <v-btn
                        text
                        @click="onClose"
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
          },
          onClose: {
              type: Function,
              required: true
          }
        },
        data: () => ({
            txtfld: '',
            login_enabled: false,
        }),
        computed: {
            showSelf: {
                get: function () {
                    return this.show;
                },
                set: function () {
                    // updates snackbar state -> ignore
                }
            },
        },
        methods: {
          generate: function() {
            this.generateUser()
              .then(u => {
                //console.log(u);
                this.setCurrentUser(u)
                  .then(res => {
                    console.log("Result:", res);
                  });
              });
          },
          loginUser: function() {
            this.setCurrentUser(this.txtfld)
              .then(res => {
                console.log("Result", res);
              });
          },
          updateEnableLogin: function() {
            console.log(this.txtfld.length);
            if(this.txtfld.length === 4){
              this.getUserID(this.txtfld.trim())
                .then(data => {
                  this.founduser = data;
                  console.log(data);
                  this.login_enabled = !(this.founduser == null);
                });
            } else {
              this.login_enabled = false;
            }
          },
        },
    }

</script>
