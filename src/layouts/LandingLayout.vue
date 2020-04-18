<template>
    <div class="bg">
        <router-view>
        </router-view>
    </div>
</template>

<script>
    export default {
        name: "LandingLayout"
    }
</script>

<style scoped>
    .bg {
        /* The image used */
        background-image: url("/img/notes.jpeg");

        /* Full height */
        height: 100vh;
        width: 100vw;

        /* Center and scale the image nicely */
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>