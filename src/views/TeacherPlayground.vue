<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Spiral Test</p>
            <AASpiral></AASpiral>
        </v-flex>
    </v-layout>
</template>


<script>
    import AASpiral from "../components/AASpiral";
    export default {
        name: "TeacherPlayground",
        components: {AASpiral}
    }
</script>

<style scoped>

</style>