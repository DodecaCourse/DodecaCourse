<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Tonic Internalisation</p>
            <Teacher t-type="internalization" :preselect="['1P']" fixed/>
            <p>Tonic Internalisation Test</p>
            <Teacher t-type="internalization-test" :preselect="['1P']" fixed/>
            <p>Individual Note Internalisation</p>
            <Teacher t-type="internalization"/>
            <p>Individual Note Internalisation Test</p>
            <Teacher t-type="internalization-test"/>
            <p>Spiral Test</p>
            <AASpiral></AASpiral>
            <p>Individual Note Recognition</p>
            <Teacher t-type="recognition" :preselect="['1P', '2M', '3M', '4P', '5P', '6M', '7M']"/>
        </v-flex>
    </v-layout>
</template>


<script>
    import Teacher from "../components/Teacher";
    import AASpiral from "./AASpiral";
    export default {
        name: "TeacherPlayground",
        components: {AASpiral, Teacher}
    }
</script>

<style scoped>

</style>