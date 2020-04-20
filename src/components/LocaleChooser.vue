<template>
    <div class="text-center">
        <v-menu close-on-content-click offset-y right transition="slide-y-transition">
            <template v-slot:activator="{ on }">
                <v-btn icon style="float: right" v-on="on" app>
                    <v-icon>mdi-translate</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item
                        v-for="(loc, index) in locales"
                        :key="index"
                        @click="changeLocaleTo(loc.id)"
                >
                    <v-list-item-title>{{ loc.name }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<script>
    export default {
        name: "LocaleChooser",
        data: function() {
            return {
                locales: [
                    {name: "Deutsch", id: "de"},
                    {name: "English", id: "en"},
                ],
                closeOnContentClick: true,
            }
        },
        methods: {
            changeLocaleTo: function(id) {
                if (this.$i18n.locale !== id) {
                    this.$i18n.locale = id;
                }
            }
        }
    }

</script>

<style scoped>

</style>