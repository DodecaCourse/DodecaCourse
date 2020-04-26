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
      <h1 class="hidden-xs-only">
        1. Recognising the Tonic
      </h1>
      <h2>Tonic Internalisation Exercise</h2>
      <p>
        The tonic internalisation exercise makes it as easy as possible for
        you to 'internalise' (memorise) the sound of the tonic.
      </p>
      <p>
        It does this by
        clearly playing the tonic repeatedly. With this repeated exposure you
        will quickly start to remember the sound of the tonic.
      </p>
      <p>
        The exercise is
        made up of a 10 bar sequence, which is repeated throughout the
        exercise. Hit »Practice« below to listen to this 10 bar sequence.
        (If you wonder about the icon, you can already take a quick look at
        the <router-link to="/individual-notes/scale-degrees">
          scale degrees
        </router-link>
        chapter in Module 2)
      </p>
      <p>
        <InlineConfigurator
          :prog-id="1001"
          t-type="internalization"
          :config="{degree: 0}"
          hide-test
        >
          Tonic Internalisation
        </InlineConfigurator>
      </p>
      <p>
        The diagram below
        shows this 10 bar sequence, taken from the tonic internalisation
        exercise.
      </p>
      <v-img
        contain
        :class="{'invert-img': $vuetify.theme.dark}"
        max-height="10.5ch"
        max-width="83.5vw"
        src="/img/m1_c_major_tonic_intern_10bars.svg"
        title="10 Bar Sequence from Tonic Internalisation Exercise"
      />
      <p>
        The
        sequence is split up into two sections, as follows:
      </p>
      <div
        class="v-stepper explanation-stepper v-stepper--is-booted v-stepper--vertical"
        :class="$vuetify.theme.dark ? 'theme--dark' : 'theme--light'"
      >
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">1</span>
          <div class="v-stepper__label">
            <span>Bars 1-2: Establish one note as the tonic</span>
          </div>
        </div>
        <div class="v-stepper__content">
          <div
            class="v-stepper__wrapper"
            style="height: auto;"
          >
            <v-card>
              <v-card-text>
                In the first two bars, a short chord progression is played (called a
                <i>I - IV - V</i> progression). This chord progression clearly establishes a
                single note as the tonic. It's impossible to internalise the sound of
                the tonic if it isn't clearly present, so you'll become very familiar
                with it as you progress through the modules as it's used at
                the beginning of a lot of exercises!
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">2</span>
          <div class="v-stepper__label">
            Bars 3-10: The tonic is played repeatedly
          </div>
        </div>
        <div class="v-stepper__content">
          <div
            class="v-stepper__wrapper"
            style="height: auto;"
          >
            <v-card>
              <v-card-text>
                In the 8 bars that follow, the tonic is played in each bar and the tonic
                chord is played in every second bar.
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">3</span>
          <div class="v-stepper__label">
            The Sequence Repeats
          </div>
        </div>
        <div class="v-stepper__content">
          <div
            class="v-stepper__wrapper"
            style="height: auto;"
          >
            <v-card>
              <v-card-text>
                After the 10 bar sequence, the entire sequence is repeated in a new randomly chosen key.
                The diagram below shows the first 30 bars of the tonic
                internalisation exercise, and in it you can see that in bar 11, a new
                key is outlined, this time A major.
              </v-card-text>
            </v-card>
          </div>
        </div>
      </div>
      <br>
      <v-img
        contain
        :class="{'invert-img': $vuetify.theme.dark}"
        max-height="27ch"
        max-width="83.5vw"
        src="/img/m1_tonic_intern_30bars.svg"
        title="First 30 Bars of Tonic Internalisation Exercise"
      />
      <p>
        If you haven't done so yet, hit »Practice« above to start the player and
        listen to the exercise while you
        read the instructions. The exercise is repetitive (by design!) so
        take your time to listen to it and read the instructions to make sure
        you have a clear understanding of how to use the exercise.
      </p>
      <p>
        <v-stepper
          v-model="curStep"
          vertical
          class="explanation-stepper"
        >
          <v-stepper-step
            :complete="curStep > 1"
            step="1"
          >
            <span>Listen to the <i>I - IV - V</i> progression</span>
          </v-stepper-step>
          <v-stepper-content step="1">
            <v-card>
              <v-card-text>
                Simply listening to the <i>I - IV - V</i>
                progression will make it clear to your ear which note is the tonic
                (even if you can't identify which note it is yet). So just sit back
                and listen.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="primary"
                  @click.native="curStep = 2"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="curStep > 2"
            step="2"
          >
            Focus your
            attention on the tonic
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-card>
              <v-card-text>
                For the following 8 bars, listen closely to
                the tonic that is played as the highest note. Listen to it's stable
                sound.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="curStep=1"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="curStep = 3"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="curStep > 3"
            step="3"
          >
            Sing the tonic
          </v-stepper-step>
          <v-stepper-content step="3">
            <v-card>
              <v-card-text>
                Alongside listening to the sound of the tonic, singing it
                will help you to really hear and internalise it's stable sound.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="curStep=2"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="curStep = 4"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="curStep>4"
            step="4"
          >
            Repeat
          </v-stepper-step>
          <v-stepper-content step="4">
            <v-card>
              <v-card-text>
                When the <i>I - IV - V</i> progression is played in a new key, listen to the
                progression as you did the first time. This will establish a new
                note as the tonic and then you can repeat listening to/singing the
                new tonic.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="curStep=3"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="curStep = 5"
                >
                  Finish
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <div v-if="curStep>4">
            <v-btn
              fab
              color="secondary"
              elevation="1"
              small
              style="float: right; margin-top: -3ch; margin-bottom: -3ch"
              class="mr-7"
              @click.native="curStep=1"
            >
              <v-icon>mdi-restart</v-icon>
            </v-btn>
          </div>
        </v-stepper>
      </p>
      <p>
        Practice with this
        exercise until you start to feel confident that you are internalising
        the sound of the tonic, or for 3 days (whichever comes first). Then
        try the tonic internalisation test.
      </p>
      <p>
        That's it! It
        sounds deceptively simple but you'll be surprised at how effective
        this technique is.
      </p>
      <p>
        And
        because of it's deceptive simplicity, many musicians try to
        complicate things. So here are a few things to avoid:
      </p>
      <h3><b>What not to do with the tonic internalisation exercise</b></h3>
      <ol>
        <li>
          <p>
            <b>DO NOT keep track of the notes/keys:</b> the aim of this exercise is to
            be able to hear a piece of music and identify (and sing) which note
            is the tonic. But we aren't trying to say whether that note is a C
            or an F# (that would be the realm of perfect pitch). Simply listen
            and sing, with no regard for what the actual notes/keys are.
          </p>
        </li>
        <li>
          <p>
            <b>DO NOT try to
              work out the tonic during the <i>I - IV - V</i> progression:</b> it takes a few
            moments for our ears to clearly identify a new tonic. We use the I -
            IV - V progression to make it clear, so wait until after the
            progression to start actively listening for the tonic. Trying to do
            it earlier simply makes things more confusing and challenging, with
            no extra benefit.
          </p>
        </li>
      </ol>
      <p><b>Finished?</b></p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/tonic-internalization/test"
      >
        Try the test
      </v-btn>
      <p>
        <br>
      </p><h4>
        <b>TROUBLESHOOTING</b>
      </h4>
      <b>“I’m struggling to sing in tune”</b>
      <p>
        If you’re
        finding it difficult to sing in tune you may be worried that the described
        method won’t work for you.
      </p>
      <p>
        Fortunately, we
        have you covered!
      </p>
      <p>
        While many people
        believe that you can’t fix bad pitch, we know that you can and
        we’ll prove it to you:
      </p>
      <p>
        Just go and check out <a href="https://www.successfulsinging.com/singing-guides/singing-in-tune/">
          this introduction to singing in tune</a>.
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
        <b>“Sometimes the
          tonic is too high/low for my voice”</b>
      </p>
      <p>
        If the tonic is
        played outside your range you can sing it an octave higher or lower
        than it is sounded.
      </p>
      <p>
        Transposing it by
        an octave gives you all the benefits of singing it in the octave that
        you hear it in, with the added benefit of improving your ability to
        identify high/low passages in music.
      </p>
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
  data: function () {
    return {
      curStep: 1,
    };
  },
  mounted: function () {
    if (!this.$teacher.playing) {
      this.$teacher.setupInternalization(0, false);
    }
  }
};
</script>

<style>
</style>