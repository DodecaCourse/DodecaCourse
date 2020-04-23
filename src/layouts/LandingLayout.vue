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
  <div class="bg">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "LandingLayout"
};
</script>

<style scoped>
    .bg {
        /* The image used */
        background-image: url("/img/sky_notes_warm.jpeg");

        /* Full height */
        height: 100vh;
        width: 100vw;

        /* Center and scale the image nicely */
        background-position: 60% center;
        background-repeat: no-repeat;
        background-size: cover;
        background-attachment: fixed;
        background-color: #f9dcbc;
    }
    @media screen and (max-device-height: 580px) {
        .bg {
            background-position: 90% center;
        }
    }
</style>
