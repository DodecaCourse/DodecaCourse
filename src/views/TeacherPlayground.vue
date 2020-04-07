<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <p>Tonic Internalisation Exercise & Test</p>
            <p>
                <InlineConfigurator :prog-id="1001" t-type="internalization"
                                    :config="{degree: '1P'}">
                    Tonic Internalisation
                </InlineConfigurator>
            </p>
            <p>Individual Note Internalisation & Test</p>
            <p>
                <InlineConfigurator :prog-id="2001" t-type="internalization"
                                    :config="{degree: '2M'}">
                    »Re« Internalisation
                </InlineConfigurator>
            </p>
            <p>Individual Note Recognition</p>
            <p>
                <InlineConfigurator :prog-id="3002" t-type="recognition-single"
                                    :config="{degrees: ['1P', '2M', '3M', '4P', '5P', '6M', '7M']}">
                    Major Scale Recognition
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