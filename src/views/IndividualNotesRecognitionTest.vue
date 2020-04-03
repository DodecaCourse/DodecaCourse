<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1>2. Recognising Individual Notes</h1>
            <h2>Recognition Tests</h2>
            <Teacher t-type="recognition" :preselect="['1P', '2M', '3M', '4P', '5P', '6M', '7M']"/>
            <p>There are 10
                recognition tests for each scale. The first 5 are at a slower tempo,
                the final 5 are at a faster tempo. Focus on the slower tempo until
                you can complete an exercise with less than 5 mistakes. Then move
                onto the faster tempo exercises.</p>
        </v-flex>
    </v-layout>
</template>

<script>
    import Teacher from "../components/Teacher";
    export default {
        name: "IndividualNotesTest",
        components: {Teacher}
    }
</script>

<style scoped>

</style>