<template>
  <div>
    <v-container
      fluid
      class="cards"
    >
      <v-snackbar
        v-model="showSelf"
        multi-line
        :timeout="0"
        color="info"
      >
        <v-card flat>
          <template v-if="user == null">
            <v-card-text>
              <h3 class="mb-1">
                Log in with an existing username
              </h3>
              <v-text-field
                v-model="txtfld"
                label="Username"
                name="txtfld"
                autofocus
                append-icon="mdi-account"
                outlined
                dense
                hide-details
                @input="updateEnableLogin"
              />
              By logging in you agree that we set a cookie to save that you are logged in
              with your username.
            </v-card-text>
            <v-card-actions>
              <v-btn
                :disabled="!login_enabled"
                primary
                @click="loginUser"
              >
                <v-icon>mdi-login</v-icon>
                Login
              </v-btn>
              <v-spacer />
              <v-btn
                primary
                class="mx-5"
                @click="onClose"
              >
                Close
              </v-btn>
            </v-card-actions>
          </template>
          <template v-else>
            <v-card-text>
              <h3 class="mb-1">
                Success!
              </h3>
              You are now logged in as <b>{{ user.user_keyword }}</b>. Your custom url:<br>
              <a :href="'https://dodeca.wavel.de/home?usr=' + user.user_keyword">
                https://dodeca.wavel.de/home?usr={{ user.user_keyword }}
              </a><br>
              You can now continue your learning journey. Have fun and remember your
              username!
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                primary
                class="mx-5"
                @click="onClose"
              >
                Close
              </v-btn>
            </v-card-actions>
          </template>
        </v-card>
      </v-snackbar>
    </v-container>
  </div>
</template>

<script>

import api from "../api.js";

export default {
  name: "LoginSnack",
  mixins: [api],
  props: {
    connected: {
      type: Boolean,
      default: true
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
    txtfld: "",
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
    loginUser: function () {
      this.setCurrentUser(this.txtfld);
    },
    updateEnableLogin: function () {
      // console.log(this.txtfld.length);
      if (this.txtfld.length === 4) {
        this.getUserID(this.txtfld.trim())
          .then(data => {
            this.founduser = data;
            // console.log(data);
            this.login_enabled = !(this.founduser == null);
          });
      } else {
        this.login_enabled = false;
      }
    },
  },
};

</script>
