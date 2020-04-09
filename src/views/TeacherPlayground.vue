<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Tonic Internalisation Exercise & Test</p>
            <p>
                <InlineConfigurator :prog-id="1001" t-type="internalization"
                                    :config="{degree: 0}">
                    Tonic Internalisation
                </InlineConfigurator>
            </p>
            <p>Individual Note Internalisation & Test</p>
            <p>
                <InlineConfigurator :prog-id="2001" t-type="internalization"
                                    :config="{degree: 2}">
                    »Re« Internalisation
                </InlineConfigurator>
            </p>
            <p>Individual Note Recognition</p>
            <p>
                <InlineConfigurator :prog-id="3002" t-type="recognition-single"
                                    :config="{degrees: [0, 2, 4, 5, 7, 9, 11]}">
                    Major Scale Recognition
                </InlineConfigurator>
            </p>
            <p>Interval Recognition</p>
            <p>
                <InlineConfigurator :prog-id="4001" t-type="recognition-interval"
                                    :config="{degrees: [0, 2, 4, 5, 7, 9, 11], intervals: [1, 2, 3, 4]}">
                    2nds & 3rds
                </InlineConfigurator>
            </p>
        </v-flex>
    </v-layout>
</template>


<script>
    import InlineConfigurator from "../components/InlineConfigurator";
    export default {
        name: "TeacherPlayground",
        components: {InlineConfigurator}
    }
</script>

<style scoped>

</style>