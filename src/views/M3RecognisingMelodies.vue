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
        3. Recognising Melodies
      </h1>
      <h2>2 Note Melody Recognition</h2>
      <p>
        These exercises are just like the internalisation exercise from the
        first module. The 2 note melody recognition exercises are just like
        the individual note recognition exercises from the previous module.
      </p>
      <p>
        A
        <i>I - IV - V - I</i> progression is played at the start to establish one note
        as the tonic, and then the exercise begins. Instead of hearing one
        note at a time, two are played - one straight after the other - then
        there is a pause where you can enter the scale degrees you heard.
      </p>
      <h3>How the exercises are organised</h3>
      <p>
        You'll see below that there are several 2 Note Melody
        Recognition Exercises: 2nds &amp; 3rds , 4ths &amp; 5ths, 6ths &amp; 8ves and
        melodic intervals. The first 3 groups contain melodies of specific
        intervals: in the 2nds &amp; 3rds exercises for example there is
        always either a 2nd or 3rd between the two notes of the melody. The
        final group contains all the intervals from the previous exercises.
      </p>
      <p>
        In each group you'll find 5 levels with varying speed, so start at level one
        and advance to the higher levels as you acquire speed in recognition.
      </p>
      <h3>How to use the 2 Note Melody Recognition Exercises?</h3>
      <p>
        The approach for these recognition exercises is identical to the
        approach for the individual note recognition exercises from the
        previous module:
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
            <span>Listen to the <i>I - IV - V - I</i> progression</span>
          </v-stepper-step>
          <v-stepper-content step="1">
            <v-card>
              <v-card-text>
                Simply listening to the <i>I - IV - V - I</i>
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
            <span>Listen to the 2 note melody played after the <i>I - IV - V - I</i> progression</span>
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-card>
              <v-card-text>
                Listen to the 2 notes and
                listen for the way that they each sound and resonate in
                relation to the tonic chord/pedal.
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
            [OPTIONAL] Sing the melody
          </v-stepper-step>
          <v-stepper-content step="3">
            <v-card>
              <v-card-text>
                Singing the notes helps to hear the way that they relate
                to the tonic and often helps to make them easier to identify. Sing
                and hold each note for a little longer than you hear them if
                necessary.
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
            Try to recognise the notes' scale degrees
          </v-stepper-step>
          <v-stepper-content step="4">
            <v-card>
              <v-card-text>
                if you think you've identified the notes' scale degrees,
                sing the melody with the corresponding solfège syllables.
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
            step="5"
          >
            Check that you've identified it correctly
          </v-stepper-step>
          <v-stepper-content step="5">
            <v-card>
              <v-card-text>
                Enter them by clicking the corresponding buttons on
                the circle to check if you identified them correctly.
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
        Repeat
        steps 2-5 throughout the exercise.
      </p>
      <h3>How to choose which exercises to focus on</h3>
      <p>
        Start with the 2nds &amp; 3rds, level 1. Focus on just this
        exercise until you can pass the test with less
        than 5 mistakes.
      </p>
      <p>
        When you can do
        this, move onto 4ths &amp; 5ths, level 1.
      </p>
      <p>
        Continue to move
        through all exercise groups until you can complete the melodic
        intervals exercise at the slowest speed. Then move onto level 2
        for 2nds &amp; 3rds. Slowly make your way through all the exercises
        until you can complete them all at the fastest speed.
      </p>
      <h3>Exercises & Tests</h3>
      <p>
        <InlineConfigurator
          :config="{degrees: [0, 2, 4, 5, 7, 9, 11], intervals: [1, 2, 3, 4]}"
          :prog-id="4001"
          t-type="recognition-interval"
        >
          2nds & 3rds
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :config="{degrees: [0, 2, 4, 5, 7, 9, 11], intervals: [5, 6, 7]}"
          :prog-id="4002"
          t-type="recognition-interval"
        >
          4ths & 5ths
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :config="{degrees: [0, 2, 4, 5, 7, 9, 11], intervals: [8, 9, 12]}"
          :prog-id="4003"
          t-type="recognition-interval"
        >
          6ths & 8ves
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :config="{degrees: [0, 2, 4, 5, 7, 9, 11], intervals: [1,2,3,4,5,6,7,8,9,12]}"
          :prog-id="4004"
          t-type="recognition-interval"
        >
          Melodic Intervals
        </InlineConfigurator>
      </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/chords/overview"
      >
        Next module
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import InlineConfigurator from "../components/InlineConfigurator";

export default {
  name: "RecognisingMelodiesMethod",
  components: {InlineConfigurator},
  data: function () {
    return {
      curStep: 1,
    };
  },
};
</script>

<style scoped>

</style>