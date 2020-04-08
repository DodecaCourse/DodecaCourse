<template>

    <!--<v-menu offset-y open-on-hover>

        <v-btn slot="activator" color="primary" v-on="{ on }">hey</v-btn>
        <v-list>
            <v-list-tile
                    v-for="(loc,index) in locales"
                    :key="index"
                    @click="">
                <v-list-item-title>
                    {{loc.name}}
                </v-list-item-title>
            </v-list-tile>
        </v-list>
    </v-menu>-->
    <div class="text-center">
        <v-menu close-on-content-click offset-y right transition="slide-y-transition">
            <template v-slot:activator="{ on }">
                <v-btn
                        style="float: right"
                        v-on="on"
                >
                    <v-icon>mdiTranslate</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item
                        v-for="(loc, index) in locales"
                        :key="index"
                >
                    <v-list-item-title @click="foo">{{ loc.name }}</v-list-item-title>
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
                items: [
                    { title: 'Click Me' },
                    { title: 'Click Me' },
                    { title: 'Click Me' },
                    { title: 'Click Me 2' },
                ],
                closeOnContentClick: true,
            }
        },
        methods: {
            foo: function() {
                if (this.$i18n.locale === "en") {
                    this.$i18n.locale = "de";
                } else {
                    this.$i18n.locale = "en";
                }
            }
        }
    }

</script>

<style scoped>

</style>