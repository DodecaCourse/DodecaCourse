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
      <h2>Individual Note Recognition Exercises</h2>
      <h3 />
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
        is a pedal played throughout the exercise. The pedal is the »Do« and
        »Re« played before every note. This makes it easy to keep
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
        Follow the steps below for the recognition exercises:
      </p>
      <ol>
        <li>
          <p>
            <b>Listen to the
              <i>I - IV - V - I</i> progression:</b> Simply listening to the <i>I - IV - V - I</i>
            progression will make it clear to your ear which note is the tonic
            (even if you can't identify which note it is yet). So just sit back
            and listen.
          </p>
        </li>
        <li>
          <p>
            <b>Listen to the
              note played after the <i>I - IV - V - I</i> progression:</b> Listen to the note and
            listen for the way that is sounds and resonates in relation to the
            tonic chord/pedal.
          </p>
        </li>
        <li>
          <p>
            <b>[OPTIONAL] Sing
              the note:</b> singing the note helps to hear the way that it relates to
            the tonic and often helps to make it easier to identify.
          </p>
        </li>
        <li>
          <p>
            <b>Try to
              recognise the note's scale degree:</b> if you think you've identified
            the note's scale degree, sing the syllable on the note.
          </p>
        </li>
        <li>
          <p>
            <b>Check that
              you've identified it correctly:</b> enter your answer
            to check that you identified the scale degree correctly.
          </p>
        </li>
      </ol>
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
      <h2>Recognition Tests</h2>
      <p>
        The exercises and tests come in three levels at varying speeds.
        Progress to the next level when you passed the test with less then
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
};
</script>
