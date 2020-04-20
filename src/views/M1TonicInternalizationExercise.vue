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
      <h1 class="hidden-xs-only">
        {{ $t("m1.intern-ex.100h1") }}
      </h1>
      <h2> {{ $t("m1.intern-ex.200h2") }} </h2>
      <p> {{ $t("m1.intern-ex.300p") }} </p>
      <p> {{ $t("m1.intern-ex.400p") }} </p>
      <p>
        {{ $t("m1.intern-ex.500p.501") }}
        <router-link to="/individual-notes/scale-degrees">
          {{ $t("m1.intern-ex.500p.600router-link") }}
        </router-link>
        {{ $t("m1.intern-ex.500p.700") }}
      </p>
      <p>
        <InlineConfigurator
          :prog-id="1001"
          t-type="internalization"
          :config="{degree: 0}"
          hide-test
        >
          {{ $t("m1.intern-ex.800p.900ic") }}
        </InlineConfigurator>
      </p>
      <p> {{ $t("m1.intern-ex.1000p") }} </p>
      <v-img
        contain
        :class="{'invert-img': $vuetify.theme.dark}"
        max-height="10.5ch"
        max-width="83.5vw"
        src="/img/m1_c_major_tonic_intern_10bars.svg"
        title="10 Bar Sequence from Tonic Internalisation Exercise"
      />
      <p> {{ $t("m1.intern-ex.1200p") }} </p>
      <h4>
        <b> {{ $t("m1.intern-ex.1300h4.1400b") }} </b>
      </h4>
      <p> {{ $t("m1.intern-ex.1500p") }} </p>
      <h4>
        <b> {{ $t("m1.intern-ex.1600h4.1700b") }} </b>
      </h4>
      <p> {{ $t("m1.intern-ex.1800p") }} </p>
      <h4>
        <b> {{ $t("m1.intern-ex.1900h4.2000b") }} </b>
      </h4>
      <p> {{ $t("m1.intern-ex.2100p") }} </p>
      <v-img
        contain
        :class="{'invert-img': $vuetify.theme.dark}"
        max-height="27ch"
        max-width="83.5vw"
        src="/img/m1_tonic_intern_30bars.svg"
        title="First 30 Bars of Tonic Internalisation Exercise"
      />
      <p> {{ $t("m1.intern-ex.2300p") }} </p>
      <ol>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.2400ol.2500li.2600p.2700b.2701") }}
              <i> {{ $t("m1.intern-ex.2400ol.2500li.2600p.2700b.2800i") }} </i>
              {{ $t("m1.intern-ex.2400ol.2500li.2600p.2700b.2900") }} </b>
            {{ $t("m1.intern-ex.2400ol.2500li.2600p.2901") }}
            <i> {{ $t("m1.intern-ex.2400ol.2500li.2600p.3000i") }} </i>
            {{ $t("m1.intern-ex.2400ol.2500li.2600p.3100") }}
          </p>
        </li>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.2400ol.3200li.3300p.3400b") }} </b>
            {{ $t("m1.intern-ex.2400ol.3200li.3300p.3500") }}
          </p>
        </li>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.2400ol.3600li.3700p.3800b") }} </b>
            {{ $t("m1.intern-ex.2400ol.3600li.3700p.3900") }}
          </p>
        </li>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.2400ol.4000li.4100p.4200b") }} </b>
            {{ $t("m1.intern-ex.2400ol.4000li.4100p.4201") }}
            <i> {{ $t("m1.intern-ex.2400ol.4000li.4100p.4300i") }} </i>
            {{ $t("m1.intern-ex.2400ol.4000li.4100p.4400") }}
          </p>
        </li>
      </ol>
      <p> {{ $t("m1.intern-ex.4500p") }} </p>
      <p> {{ $t("m1.intern-ex.4600p") }} </p>
      <p> {{ $t("m1.intern-ex.4700p") }} </p>
      <h3>
        <b> {{ $t("m1.intern-ex.4800h3.4900b") }} </b>
      </h3>
      <ol>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.5000ol.5100li.5200p.5300b") }} </b>
            {{ $t("m1.intern-ex.5000ol.5100li.5200p.5400") }}
          </p>
        </li>
        <li>
          <p>
            <b> {{ $t("m1.intern-ex.5000ol.5500li.5600p.5700b.5701") }}
              <i> {{ $t("m1.intern-ex.5000ol.5500li.5600p.5700b.5800i") }} </i>
              {{ $t("m1.intern-ex.5000ol.5500li.5600p.5700b.5900") }} </b>
            {{ $t("m1.intern-ex.5000ol.5500li.5600p.6000") }}
          </p>
        </li>
      </ol>
      <p>
        <b> {{ $t("m1.intern-ex.6100p.6200b") }} </b>
      </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/tonic-internalization/test"
      >
        {{ $t("m1.intern-ex.6300v-btn") }}
      </v-btn>
      <p><br></p>
      <h4>
        <b> {{ $t("m1.intern-ex.6400p.6600h4.6700b") }} </b>
      </h4>
      <b> {{ $t("m1.intern-ex.6400p.6800b") }} </b>
      <p> {{ $t("m1.intern-ex.6400p.6900p") }} </p>
      <p> {{ $t("m1.intern-ex.6400p.7000p") }} </p>
      <p> {{ $t("m1.intern-ex.6400p.7100p") }} </p>
      <p>
        {{ $t("m1.intern-ex.6400p.7200p.7201") }}
        <a href="https://www.successfulsinging.com/singing-guides/singing-in-tune/"> {{ $t("m1.intern-ex.6400p.7200p.7300a") }} </a>
      </p>

      <!--
            <p>So navigate to the
                bonus module “How to Sing in Tune” where you’ll find a simple
                exercise that you can use to improve your pitching within 1-2 weeks.
                Once you’ve spent a week or so on that exercise your singing will
                be at a level where you’re ready to start on the internalisation
                exercises.</p>
            <p><b>“I’m not sure
                whether I’m singing the tonic or a different note”</b></p>
            <p>In the
                internalisation exercise the tonic is always the top note.</p>
            <p>So if you’re
                unsure whether you’re singing the correct note you can use the
                exercises in the bonus module “How to Sing the Top Note of a Chord”
                to improve your ability to hear and sing the top note of a chord.
                That exercise will make it easy for you to know when you’re singing
                the correct note in the internalisation exercise and when you’re
                singing a different note from the chord.</p>
                -->

      <p>
        <b> {{ $t("m1.intern-ex.6400p.7500p.7600b") }} </b>
      </p>
      <p> {{ $t("m1.intern-ex.6400p.7700p") }} </p>
      <p> {{ $t("m1.intern-ex.6400p.7800p") }} </p>
      <!--
            <p>If you find it
                difficult to transpose the notes you hear by an octave, you’ll find
                an exercise to work on it in the bonus module “How to Become a More
                Confident Singer”.</p>
                -->
    </v-flex>
  </v-layout>
</template>

<script>
import InlineConfigurator from "../components/InlineConfigurator";
export default {
  name: "TonicInternalizationMethod",
  components: {InlineConfigurator},
  mounted: function () {
    if (!this.$teacher.playing) {
      this.$teacher.setupInternalization(0, false);
    }
  }
};
</script>

<style>
</style>