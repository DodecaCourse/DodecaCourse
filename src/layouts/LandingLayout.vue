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
