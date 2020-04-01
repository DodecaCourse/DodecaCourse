<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Tonic Internalisation</p>
            <Teacher fixed-degree="1P"/>
            <p>Individual Note Internalisation</p>
            <Teacher/>
        </v-flex>
    </v-layout>
</template>


<script>
    import Teacher from "../components/Teacher";
    export default {
        name: "TeacherPlayground",
        components: {Teacher}
    }
</script>

<style scoped>

</style>