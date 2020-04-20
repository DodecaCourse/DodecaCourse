<template>

    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1 class="hidden-xs-only"> {{$t('m1.the-tonic.100h1')}} </h1>
            <h2> {{$t('m1.the-tonic.200h2')}} </h2>
            <p> {{$t('m1.the-tonic.300p')}} </p>
            <p> {{$t('m1.the-tonic.400p')}} </p>
            <p> {{$t('m1.the-tonic.500p')}} </p>
            <p> {{$t('m1.the-tonic.600p')}} </p>
            <p> {{$t('m1.the-tonic.700p')}} </p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/tonic-internalization/exercise"> {{$t('m1.the-tonic.800v-btn')}} </v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
export default {
  name: "TonicInternalizationMethod",
  mounted: function () {
    if (!this.$teacher.playing) {
      this.$teacher.setupInternalization(0, false);
    }
  }
};
</script>

<style>
</style>