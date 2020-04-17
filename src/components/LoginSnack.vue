<template>
    <div>
        <v-container fluid class="cards">
            <v-snackbar
                    v-model="showSelf"
                    multi-line
                    :timeout="0"
                    color="info"
            >
                <v-card flat>
                <template v-if="user == null">
                    <v-card-text>
                        <h3>Log in with an existing username</h3>
                              <v-text-field
                                label="Username"
                                name="txtfld"
                                autofocus
                                v-model="txtfld"
                                @input="updateEnableLogin"
                                append-icon="mdi-account"
                                outlined
                                dense
                                hide-details
                              />
                        By logging in you agree that we set a cookie to save that you are logged in
                        with your username.
                    </v-card-text>
                  <v-card-actions>
                      <v-btn v-on:click="loginUser" :disabled="!login_enabled" primary>
                          <v-icon>mdi-login</v-icon>
                          Login
                      </v-btn>
                      <v-btn
                              @click="onClose"
                              primary
                              class="mx-5"
                      >
                          Close
                      </v-btn>
                  </v-card-actions>
                </template>
                <template v-else>
                        <v-card-text>
                            <h3>Log in to continue where you left off!</h3>
                                Success! You are now logged in as <b>{{user.user_keyword}}</b>. Your custom url:
                                <v-text-field
                                    readonly
                                    solo
                                    dense
                                    hide-details
                                    :value="'https://dodeca.wavel.de/home?usr=' + user.user_keyword"
                                ></v-text-field>
                            You can now continue your learning journey. Have fun and remember your
                                username!
                        </v-card-text>
                        <v-card-actions>
                            <v-btn
                                    @click="onClose"
                                    primary
                                    class="mx-5"
                            >
                                Close
                            </v-btn>
                        </v-card-actions>
                </template></v-card>
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
            generate: function () {
                this.generateUser()
                    .then(u => {
                        //console.log(u);
                        this.setCurrentUser(u)
                            .then(res => {
                                console.log("Result:", res);
                            });
                    });
            },
            loginUser: function () {
                this.setCurrentUser(this.txtfld)
                    .then(res => {
                        console.log("Result", res);
                    });
            },
            updateEnableLogin: function () {
                console.log(this.txtfld.length);
                if (this.txtfld.length === 4) {
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
