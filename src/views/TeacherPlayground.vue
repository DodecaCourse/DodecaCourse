<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Tonic Internalisation</p>
            <Teacher :fixed-degrees="['1P']" t-type="internalization"/>
            <p>Tonic Internalisation Test</p>
            <Teacher :fixed-degrees="['1P']" t-type="internalization-test"/>
            <p>Individual Note Internalisation</p>
            <Teacher t-type="internalization"/>
            <p>Individual Note Internalisation Test</p>
            <Teacher t-type="internalization-test"/>
            <p>Individual Note Recognition</p>
            <Teacher t-type="recognition"/>
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