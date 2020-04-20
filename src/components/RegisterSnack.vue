<!--
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz, Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
-->
<template>
  <div>
    <v-container
      fluid
      class="cards"
    >
      <v-snackbar
        v-model="showSelf"
        vertical
        :timeout="0"
        color="info"
      >
        <v-card>
          <template v-if="user == null">
            <v-card-text>
              <h3 class="mb-1">
                Generate your personal username
              </h3>
              to save your progress and to continue right where you left off.
              By clicking »Generate« below, you allow us to set a cookie to store
              that you're logged in with this username.
              <v-card-actions>
                <v-btn @click="generate">
                  <v-icon>mdi-dice-3</v-icon>
                  Generate
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
            </v-card-text>
          </template>
          <template v-else>
            <v-card-text>
              <h3 class="mb-1">
                Success!
              </h3>
              You are now logged in as <b>{{ user.user_keyword }}</b>. Write down your username or bookmark your custom URL:<br>
              <a :href="'https://dodeca.wavel.de/home?usr=' + user.user_keyword">
                https://dodeca.wavel.de/home?usr={{ user.user_keyword }}
              </a><br>
              To log in for your next session, use your custom URL or the login button above
              to enter your username.
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                primary
                class="mx-5"
                @click="onClose"
              >
                I Understood
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
  name: "RegisterSnack",
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
  },
};

</script>
