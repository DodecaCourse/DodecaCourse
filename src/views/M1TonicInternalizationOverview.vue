<template>
  <v-layout
    align-center
    justify-center
    row
  >
    <v-flex
      class="article"
      xs10
    >
      <h1> {{ $t('m1.overview.100h1') }} </h1>
      <h2> {{ $t('m1.overview.200h2') }} </h2>
      <p> {{ $t('m1.overview.300p') }} </p>
      <ul>
        <li> {{ $t('m1.overview.400ul.500li') }} </li>
        <li> {{ $t('m1.overview.400ul.600li') }} </li>
      </ul>
      <h2> {{ $t('m1.overview.700h2') }} </h2>
      <ol>
        <li>
          <p> {{ $t('m1.overview.800ol.900li.1000p') }} </p>
        </li>
        <li>
          <p> {{ $t('m1.overview.800ol.1100li.1200p') }} </p>
        </li>
        <li>
          <p> {{ $t('m1.overview.800ol.1300li.1400p') }} </p>
        </li>
        <li>
          <p> {{ $t('m1.overview.800ol.1500li.1600p') }} </p>
        </li>
        <li>
          <p> {{ $t('m1.overview.800ol.1700li.1800p') }} </p>
        </li>
        <li>
          <p> {{ $t('m1.overview.800ol.1900li.2000p') }} </p>
        </li>
      </ol>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/tonic-internalization/tonic"
      >
        {{ $t('m1.overview.2100v-btn') }}
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "TonicInternalizationOverview",
  mounted: function () {
    if (!this.$teacher.playing) {
      this.$teacher.setupInternalization(0, false);
    }
  }
};
</script>

<style scoped>

</style>