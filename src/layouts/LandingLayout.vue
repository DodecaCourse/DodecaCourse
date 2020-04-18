<template>
    <div>

        <v-content>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-content>

        <v-footer app>
      <span>&copy;2020 <router-link to="/impressum.html" class="pr-1">Impressum & Datenschutz</router-link>
                  </span>
        </v-footer>
    </div>
</template>

<script>
    export default {
        name: "LandingLayout"
    }
</script>

<style scoped>

</style>