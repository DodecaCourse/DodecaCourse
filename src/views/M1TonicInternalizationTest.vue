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
      <h2>Test</h2>
      <p>
        The tonic internalisation test gives you a way to easily tell when
        you have successfully internalised the sound of the tonic so you can
        move onto module 2.
      </p>
      <p>
        Just like the
        internalisation exercise, the tonic internalisation test is made up
        of a sequence that is repeated throughout the exercise. This time
        it's an 8 bar sequence:
      </p>
      <p>
        <v-img
          contain
          :class="{'invert-img': $vuetify.theme.dark}"
          max-height="10.5ch"
          max-width="83.5vw"
          src="/img/m1_c_major_tonic_intern_test.svg"
          title="The first 8 bars of the tonic internalisation test"
        />
      </p>
      <p>
        The tonic
        internalisation test can be broken down into 3 sections:
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
                Just like in the
                internalisation exercise, a note is established as the tonic using
                the <i>I - IV - V - I</i> progression.
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">2</span>
          <div class="v-stepper__label">
            Bars 3-6: Pause
          </div>
        </div>
        <div class="v-stepper__content">
          <div
            class="v-stepper__wrapper"
            style="height: auto;"
          >
            <v-card>
              <v-card-text>
                During the
                following 4 bars, there is a pause. This is where the testing takes
                place. You'll find out how in the next section.
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">3</span>
          <div class="v-stepper__label">
            Bars 7-8: The tonic is played
          </div>
        </div>
        <div class="v-stepper__content">
          <div
            class="v-stepper__wrapper"
            style="height: auto;"
          >
            <v-card>
              <v-card-text>
                In the final 2
                bars of the sequence, the tonic is played. It is repeated in three
                octaves, so that it will match your register, regardless of your
                range.
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="v-stepper__step v-stepper__step--active">
          <span class="v-stepper__step__step primary">4</span>
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
                The 8 bar sequence is repeated in a new randomly chosen key.
                The diagram below shows an example of the first 24 bars of the tonic
                internalisation test:
              </v-card-text>
            </v-card>
          </div>
        </div>
      </div>
      <br>
      <p>
        <v-img
          contain
          :class="{'invert-img': $vuetify.theme.dark}"
          max-height="55ch"
          max-width="83.5vw"
          src="/img/m1_tonic_intern_test_24bars.svg"
          title="The first 24 bars of the tonic internalisation test"
        />
      </p>
      <h3>How to use the tonic internalisation test</h3>
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
            <span>Listen to the <i>I - IV - V - I</i> progression</span>
          </v-stepper-step>
          <v-stepper-content step="1">
            <v-card>
              <v-card-text>
                Like with the internalisation exercises (and
                all other exercises in the Dodeca course) just listen to the <i>I - IV - V - I</i>
                progression while it outlines the key.
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
            Listen for the sound of the tonic and hear it clearly in your head
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-card>
              <v-card-text>
                Wait until
                the <i>I - IV - V - I</i> progression has been played and you hear the tonic
                chord played again, then see if you can hear internally which note
                is the tonic. Try to hear it as clearly as you can in your head.
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
                Sing the note you hear as the tonic in your head. If you
                can't hold it for the entire duration of the pause, stop and take a
                breath, then sing it again until you hear the tonic played.
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
            Check that you have sung the target scale degree correctly
          </v-stepper-step>
          <v-stepper-content step="4">
            <v-card>
              <v-card-text>
                If the microphone is activated (toggle it using the
                <v-icon>mdi-microphone</v-icon> button), you can capture your singing and it will tell you if you've sung correctly
                (keep in mind that the software might not be 100% accurate. It's important you hold the note until the end).
                If not, listen to the tonic when it is played to see if it's the same note as the one you're
                singing.
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
          <v-stepper-content step="5">
            <v-card>
              <v-card-text>
                The tonic internalisation exercise moves randomly through the keys.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="curStep=4"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="curStep = 6"
                >
                  Finish
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <div v-if="curStep>5">
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
        <InlineConfigurator
          :prog-id="1001"
          t-type="internalization"
          :config="{degree: 0}"
        >
          Tonic Internalisation
        </InlineConfigurator>
      </p>
      <p>
        If you sang the
        tonic correctly in 10, 11 or all 12 keys, congratulations, you've
        passed the first module! You've taken an
        incredibly important step on the road to relative pitch and more
        creativity and confidence with music.
      </p>
      <p>
        If you didn't,
        there's no need to worry. It takes most students at least a
        few attempts to pass this test. Simply go back to the
        <router-link to="/tonic-internalization/exercise">
          internalisation exercise
        </router-link>
        to solidify your ability to recognise the sound of the tonic
        and retry after a few more practice sessions. Make sure you check the
        troubleshooting section if you have any specific problems.
      </p>
      <p>
        <b>Want to save your progress as you make your way through the Dodeca Course?</b>
      </p>
      <p>
        Generate a username by hitting <v-icon>mdi-account-plus</v-icon> in the top right corner.
        It's free and no personal information is required.
      </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="mx-3"
        to="/individual-notes/overview"
      >
        Next module
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import InlineConfigurator from "../components/InlineConfigurator";
export default {
  name: "TonicInternalizationTest",
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

<style scoped>

</style>