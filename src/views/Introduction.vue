<!--
This file is part of the "Dodeca Course" and
is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
It is a derivative of Ear Training HQ (https://eartraininghq.com/), used under
Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
-->
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
      <h1> <b> {{ $t('introduction.100h1.101b') }} </b> {{ $t('introduction.100h1.102n') }} </h1>
      <h2> {{ $t('introduction.200h2') }} </h2>
      <p> {{ $t('introduction.300p') }} </p>
      <p> {{ $t('introduction.400p') }} </p>
      <p> {{ $t('introduction.500p') }} </p>
      <h3> {{ $t('introduction.600h3') }} </h3>
      <p> {{ $t('introduction.700p') }} </p>
      <p> {{ $t('introduction.800p') }} </p>
      <p> {{ $t('introduction.900p') }} </p>
      <h3> {{ $t('introduction.1000h3') }} </h3>
      <p> {{ $t('introduction.1100p') }} </p>
      <p> {{ $t('introduction.1200p') }} </p>
      <p> {{ $t('introduction.1300p') }} </p>
      <p> {{ $t('introduction.1400p') }} </p>
      <p> {{ $t('introduction.1500p') }} </p>
      <p> {{ $t('introduction.1600p') }} </p>
      <p> {{ $t('introduction.1700p') }} </p>
      <p> {{ $t('introduction.1800p') }} </p>
      <p> {{ $t('introduction.1900p') }} </p>
      <h3> {{ $t('introduction.2000h3') }} </h3>
      <p> {{ $t('introduction.2100p') }} </p>
      <p> {{ $t('introduction.2200p') }} </p>
      <h3> {{ $t('introduction.2300h3') }} </h3>
      <p> {{ $t('introduction.2400p') }} </p>
      <p> {{ $t('introduction.2500p') }} </p>
      <h3> {{ $t('introduction.2600h3') }} </h3>
      <p> {{ $t('introduction.2700p') }} </p>
      <p> {{ $t('introduction.2800p') }} </p>
      <p> {{ $t('introduction.2900p') }} </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/tonic-internalization/overview"
      >
        {{ $t('introduction.3000v-btn') }}
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "Introduction",
  components: {
  },
};
</script>
