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
  <v-layout
    column
    align-center
    justify-center
    fill-height
  >
    <v-layout
      column
      align-center
      justify-center
      class="main flex-grow-0"
    >
      <LandingCircle
        :enabled-buttons="[0,2,4,5,7,9,11]"
        :labels="['Do', 'Ra', 'Re', 'Me', 'Mi', 'Fa', 'Fi', 'So', 'Le', 'La', 'Te', 'Ti']"
      >
        <template #content>
          <div>
            <h1 class="text-center">
              <b>Dodeca</b>
            </h1>
            <span class="text-center">Hearing is Relative</span>
          </div>
        </template>
      </LandingCircle>

      <h3
        v-if="$vuetify.breakpoint.height > 415"
        class="text-center mt-4"
      >
        Functional Ear Training Course - Free & Online
      </h3>
      <v-btn
        :class="{'mt-12': $vuetify.breakpoint.height > 500}"
        color="primary"
        dark
        large
        href="/intro"
      >
        Get Started
      </v-btn>
    </v-layout>
    <div class="sp-footer white--text">
      <span>
        &copy;2020 <a href="/impressum.html">Impressum & Datenschutz</a>
      </span>
    </div>
  </v-layout>
</template>

<script>
import LandingCircle from "../components/LandingCircle";
export default {
  name: "LandingPage",
  components: {LandingCircle},
};
</script>

<style scoped lang="sass">
    .main
        max-width: 90vw
        margin-bottom: 4ch

    .sp-footer
        background-color: rgba(0,0,0, 0.25)
        width: 100%
        padding: 0.4ch
        text-align: center
        position: absolute
        bottom: 0
</style>
