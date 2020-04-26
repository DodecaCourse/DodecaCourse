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
        2. Recognising Individual Notes
      </h1>
      <p>
        You'll find recognition exercises in every module of the Dodeca course
        from here on. The idea behind recognition exercises is
        simple: listen to a sound that you've internalised and try to
        recognise what it is. After you've heard it played you can
        enter your answer and check if you got it right.
      </p>
      <p>
        By repeatedly
        practicing recognising the sounds you're working on you can easily
        develop confidence and speed of recognition - which will allow you to
        start identifying these sounds in music when you're listening and
        playing.
      </p>
      <p>
        The recognition
        exercises in this module focus on recognising individual notes using
        their scale degrees.
      </p>
      <p>
        In the first 3
        bars a <i>I - IV - V - I</i> progression is played. After that an individual
        note is played. After each note there is a pause where you can enter your answer.
      </p>
      <p>
        Additionally there
        is a pedal played throughout the exercise. The pedal is »Do« and
        »So« played before every note. This makes it easy to keep
        the sound of the tonic firmly in your head so you'll always hear each
        note in relation to it.
      </p>
      <p>
        After 8 notes, the key changes and is introduced by a cadence.
      </p>
      <p>
        Below you can see
        the first 26 bars (8 notes) of a recognition exercise:
      </p>
      <p>
        <v-img
          contain
          :class="{'invert-img': $vuetify.theme.dark}"
          max-height="27ch"
          max-width="83.5vw"
          src="/img/m2_recognition.svg"
          title="first 26 bars of a recognition exercise"
        />
      </p>

      <h3>How to use the individual note recognition exercises</h3>
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
            <span>Listen to the note played after the <i>I - IV - V - I</i> progression</span>
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-card>
              <v-card-text>
                Listen to the note and
                listen for the way that is sounds and resonates in relation to the
                tonic chord/pedal.
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
            [OPTIONAL] Sing the note
          </v-stepper-step>
          <v-stepper-content step="3">
            <v-card>
              <v-card-text>
                Singing the note helps to hear the way that it relates to
                the tonic and often helps to make it easier to identify.
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
            Try to recognise the note's scale degree
          </v-stepper-step>
          <v-stepper-content step="4">
            <v-card>
              <v-card-text>
                If you think you've identified
                the note's scale degree, sing the syllable on the note.
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
                Enter your answer to check that you identified the scale degree correctly.
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
        Repeat this
        throughout the exercise.
      </p>
      <p>
        Note that step 3
        is optional. Insert it when you first begin with the recognition
        exercises but with time you will rely less and less on singing the
        note recognise it's scale degree. If you think you may be able to
        identify a note's scale degree without singing, attempt to do so.
        Recognition without singing is the end goal with these exercises.
      </p>
      <p>
        The recognition
        tests are split up into the pentatonic scale and the major scale.
        Once you've internalised scale degrees 1, 2, 3, 5 and 6 begin on the
        pentatonic scale recognition tests. Then practice with these until
        you pass the final internalisation test. Once you've done this
        you're ready to move onto the major scale recognition tests
      </p>
      <h3>Exercises & Tests</h3>
      <p>
        The exercises and tests come in three levels at varying speeds.
        The tests work exactly like the exercises, but they stop after 32 notes.
        Progress to the next level when you passed the test with less than
        five errors.
      </p>
      <p>
        <InlineConfigurator
          :prog-id="3001"
          t-type="recognition-single"
          :config="{degrees: [0, 2, 4, 7, 9]}"
        >
          Pentatonic Recognition
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :prog-id="3002"
          t-type="recognition-single"
          :config="{degrees: [0, 2, 4, 5, 7, 9, 11]}"
        >
          Major Scale Recognition
        </InlineConfigurator>
      </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/recognising-melodies/overview"
      >
        Next Module
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import InlineConfigurator from "../components/InlineConfigurator";
export default {
  name: "IndividualNotesMethod",
  components: {InlineConfigurator},
  data: function () {
    return {
      curStep: 1,
    };
  },
};
</script>
