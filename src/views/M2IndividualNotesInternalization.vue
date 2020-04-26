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
      <h2>Internalisation</h2>
      <h3>Exercise Description</h3>
      <p>
        In this module there is an internalisation exercise for each scale
        degree (see <router-link to="#targets">
          below
        </router-link>). The scale degree that an internalisation exercise focuses on
        is called the target scale degree of the exercise.
      </p>
      <p>
        These exercises
        are just like the internalisation exercise from the first module. A
        <i>I - IV - V</i> progression is played for the first two bars, followed by 8
        bars with the tonic chord played in every second bar. However, the
        target scale degree is played in each bar instead of the tonic.
      </p>
      <p>
        You can see the
        first 10 bars from the internalisation exercise for the second scale
        degree "Re" below. In the key of C major, this is the note D.
      </p>
      <p>
        <v-img
          contain
          :class="{'invert-img': $vuetify.theme.dark}"
          max-height="11.2ch"
          max-width="83.5vw"
          src="/img/m2_c_major_intern_solfege.svg"
          title="First 10 bars from the internalisation exercise for the second scale degree"
        />
      </p>
      <h3>How to use the individual note internalisation exercises</h3>
      <p>
        The approach to the individual note exercises is the same as it was
        in the previous module with one addition: when you sing the scale
        degree, hold it for a couple of seconds then sing the tonic. Then
        return to the target scale degree.
      </p>
      <p>
        If you can sing
        the tonic in this way it shows that you're recognising the tonic
        clearly so you're hearing the relationship between the tonic and the
        target scale degree.
      </p>
      <p>
        So the complete
        process is:
      </p>
      <p>
        <v-stepper
          v-model="exStep"
          vertical
          class="explanation-stepper"
        >
          <v-stepper-step
            :complete="exStep > 1"
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
                  @click.native="exStep = 2"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="exStep > 2"
            step="2"
          >
            Focus your attention on the target scale degree
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-card>
              <v-card-text>
                For the following 8 bars,
                listen closely to the target scale degree. Listen to the way that it
                sounds in relation to the tonic chord.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="exStep=1"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="exStep = 3"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="exStep > 3"
            step="3"
          >
            Sing the target scale degree
          </v-stepper-step>
          <v-stepper-content step="3">
            <v-card>
              <v-card-text>
                Alongside listening to the sound of the target
                scale degree, singing it will help you to really hear and
                internalise it's unique sound.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="exStep=2"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="exStep = 4"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="exStep>4"
            step="4"
          >
            Sing the tonic
          </v-stepper-step>
          <v-stepper-content step="4">
            <v-card>
              <v-card-text>
                After you've sung the target scale degree for a couple of
                seconds, sing the tonic to ensure you can recognise it accurately.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="exStep=3"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="exStep = 5"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="exStep>5"
            step="5"
          >
            Sing the target scale degree again
          </v-stepper-step>
          <v-stepper-content step="5">
            <v-card>
              <v-card-text>
                Return to the target scale degree and
                continue listening to the way that it sounds next to the tonic
                chord.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="exStep=4"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="exStep = 6"
                >
                  Next
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <v-stepper-step
            :complete="exStep>6"
            step="6"
          >
            Repeat
          </v-stepper-step>
          <v-stepper-content step="6">
            <v-card>
              <v-card-text>
                When the <i>I - IV - V</i> progression is played in a new key, listen to the
                progression as you did the first time. This will establish a new
                note as the tonic and then you can repeat listening to/singing the
                target scale degree in the new key.
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="secondary"
                  @click.native="exStep=5"
                >
                  Previous
                </v-btn>
                <v-btn
                  color="primary"
                  @click.native="exStep = 7"
                >
                  Finish
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <div v-if="exStep>6">
            <v-btn
              fab
              color="secondary"
              elevation="1"
              small
              style="float: right; margin-top: -3ch; margin-bottom: -3ch"
              class="mr-7"
              @click.native="exStep=1"
            >
              <v-icon>mdi-restart</v-icon>
            </v-btn>
          </div>
        </v-stepper>
      </p>
      <p>
        Practice
        with this exercise until you start to feel confident that you are
        internalising the sound of the target scale degree. Then try the
        internalisation test for the target scale degree.
      </p>
      <h3>Internalisation Tests</h3>
      <p>
        Each scale degree has an internalisation test that goes alongside
        it's internalisation exercise.
      </p>
      <p>
        The
        internalisation test for each scale degree is just like the
        internalisation test for the tonic from the first module. A <i>I - IV - V - I</i>
        progression is played for the first two bars, followed by a pause,
        and finally the target scale degree is played before the sequence is
        repeated in a new key.
      </p>
      <p>
        You can see the
        first 8 bars from the internalisation test for the second scale
        degree below.
      </p>
      <p>
        <v-img
          contain
          :class="{'invert-img': $vuetify.theme.dark}"
          max-height="10.8ch"
          max-width="83.5vw"
          src="/img/m2_c_major_re_intern_test.svg"
          title="First 8 bars from the internalisation test for the second scale degree"
        />
      </p>
      <h3>How to use the individual note internalisation tests</h3>
      <p>
        In the internalisation tests in this module we'll add the additional
        step of singing the tonic, just as we did with the internalisation
        exercises.
      </p>
      <p>
        This creates two
        'difficulty levels' with the internalisation tests.
      </p>
      <h4>1. Sing the tonic</h4>
      <p>
        In this first
        'difficulty level', you'll sing the tonic before you attempt to sing
        the target scale degree. So you will:
      </p>
      <v-tabs
      grow
      >
        <v-tab>
          Level 1
        </v-tab>
        <v-tab-item>
          <v-stepper
            v-model="curStep1"
            vertical
            class="explanation-stepper"
          >
            <v-stepper-step
              :complete="curStep1 > 1"
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
                    @click.native="curStep1 = 2"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1 > 2"
              step="2"
            >
              Listen for the sound of the tonic and hear it clearly in your head
            </v-stepper-step>
            <v-stepper-content step="2">
              <v-card>
                <v-card-text>
                  Wait until the <i>I - IV - V - I</i> progression has been played and you
                  hear the tonic chord played again, then identify which note is the
                  tonic and hear it internally.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=1"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 3"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1 > 3"
              step="3"
            >
              Sing the tonic
            </v-stepper-step>
            <v-stepper-content step="3">
              <v-card>
                <v-card-text>
                  Sing the note you hear as the tonic in your head just as you
                  did in the tonic internalisation exercise.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=2"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 4"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1>4"
              step="4"
            >
              Try to hear the sound of the target scale degree clearly in your head
            </v-stepper-step>
            <v-stepper-content step="4">
              <v-card>
                <v-card-text>
                  after you've sung the tonic, try to hear the sound of the target scale
                  degree as clearly in your head as you can. You are repeating the
                  movement from the tonic to the target scale degree you've been
                  singing in the internalisation exercise so listen for that sound.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=3"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 5"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1>5"
              step="5"
            >
              Sing the target scale degree
            </v-stepper-step>
            <v-stepper-content step="5">
              <v-card>
                <v-card-text>
                  If you can hear the target scale degree
                  internally, sing it. Then hold it or repeat it for the next few
                  seconds.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=4"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 6"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1>6"
              step="6"
            >
              Check that you have sung the target scale degree correctly
            </v-stepper-step>
            <v-stepper-content step="6">
              <v-card>
                <v-card-text>
                  If the microphone is activated (toggle it using the
                  <v-icon>mdi-microphone</v-icon> button), you can record your singing and it will tell you if you've sung correctly
                  (keep in mind that the software might not be 100% accurate. It's important you hold the target scale degree until the end).
                  If not, listen to the target scale degree when it is played to see if it's the same note
                  as the one you're singing.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=5"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 7"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep1>7"
              step="7"
            >
              Repeat
            </v-stepper-step>
            <v-stepper-content step="7">
              <v-card>
                <v-card-text>
                  The internalisation tests move through 12 random keys, so repeat this
                  process to see how well you've internalised the sound of each scale degree.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep1=6"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep1 = 8"
                  >
                    Finish
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <div v-if="curStep1>7">
              <v-btn
                fab
                color="secondary"
                elevation="1"
                small
                style="float: right; margin-top: -3ch; margin-bottom: -3ch"
                class="mr-7"
                @click.native="curStep1=1"
              >
                <v-icon>mdi-restart</v-icon>
              </v-btn>
            </div>
          </v-stepper>
        </v-tab-item>
        <v-tab>
          Level 2
        </v-tab>
        <v-tab-item>
          <v-stepper
            v-model="curStep2"
            vertical
            class="explanation-stepper"
          >
            <v-stepper-step
              :complete="curStep2 > 1"
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
                    @click.native="curStep2 = 2"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep2 > 2"
              step="2"
            >
              Listen for the sound of the tonic and hear it clearly in your head
            </v-stepper-step>
            <v-stepper-content step="2">
              <v-card>
                <v-card-text>
                  Wait until the <i>I - IV - V - I</i> progression has been played and you hear the tonic
                  chord played again, then identify which note is the tonic and hear it internally.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep2=1"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep2 = 3"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep2 > 3"
              step="3"
            >
              Try to hear the sound of the target scale degree clearly in your head
            </v-stepper-step>
            <v-stepper-content step="3">
              <v-card>
                <v-card-text>
                  Once you can hear the tonic clearly in your head, listen for the sound of the
                  target scale degree. You are listening for the same relationship,
                  but you simply haven't sung the tonic.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep2=2"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep2 = 4"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep2>4"
              step="4"
            >
              Sing the target scale degree
            </v-stepper-step>
            <v-stepper-content step="4">
              <v-card>
                <v-card-text>
                  If you can hear the target scale degree
                  internally, sing it. Then hold it or repeat it for the next few second.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep2=3"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep2 = 5"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep2>5"
              step="5"
            >
              Check that you have sung the target scale degree correctly
            </v-stepper-step>
            <v-stepper-content step="5">
              <v-card>
                <v-card-text>
                  If the microphone is activated (toggle it using the
                  <v-icon>mdi-microphone</v-icon> button), you can record your singing and it will tell you if you've sung correctly
                  (keep in mind that the software might not be 100% accurate. It's important you hold the target scale degree until the end).
                  If not, listen to the target scale degree when it is played to see if it's the same note
                  as the one you're singing.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep2=4"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep2 = 6"
                  >
                    Next
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <v-stepper-step
              :complete="curStep2>6"
              step="6"
            >
              Repeat
            </v-stepper-step>
            <v-stepper-content step="6">
              <v-card>
                <v-card-text>
                  The internalisation tests move through 12 random keys, so repeat this
                  process to see how well you've internalised the
                  sound of each scale degree.
                </v-card-text>
                <v-card-actions>
                  <v-spacer />
                  <v-btn
                    color="secondary"
                    @click.native="curStep2=5"
                  >
                    Previous
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click.native="curStep2 = 7"
                  >
                    Finish
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-stepper-content>
            <div v-if="curStep2>6">
              <v-btn
                fab
                color="secondary"
                elevation="1"
                small
                style="float: right; margin-top: -3ch; margin-bottom: -3ch"
                class="mr-7"
                @click.native="curStep2=1"
              >
                <v-icon>mdi-restart</v-icon>
              </v-btn>
            </div>
          </v-stepper>
        </v-tab-item>
      </v-tabs>
      <br />
      <p>
        Once you can get
        10 out of 12 keys right at the first difficult level, you're ready to
        move onto the second one.
      </p>

      <p>
        Once you can pass
        an internalisation test (sing the target scale degree correctly 10
        out of 12 times), move onto the next internalisation exercise.
      </p>
      <p>
        Repeat
        this until you've passed the first 4 internalisation tests. Then
        you're read to add the recognition exercises to your practice
        routine.
      </p>
      <p>
        Start with the scale degrees of the pentatonic scale. You already learned the sound
        of »Do«, now continue with »Re«, »Mi«, »So« and »La«.
      </p>
      <h3 id="targets">
        Practice & Test
      </h3><br>
      <p>
        <InlineConfigurator
          :prog-id="2001"
          t-type="internalization"
          :config="{degree: 2}"
        >
          »Re« Internalisation
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :prog-id="2002"
          t-type="internalization"
          :config="{degree: 4}"
        >
          »Mi« Internalisation
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :prog-id="2004"
          t-type="internalization"
          :config="{degree: 7}"
        >
          »So« Internalisation
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :prog-id="2005"
          t-type="internalization"
          :config="{degree: 9}"
        >
          »La« Internalisation
        </InlineConfigurator>
      </p>
      <p>
        Having internalised the pentatonic scale, you can already play many
        pop songs by ear. You can already continue to the pentatonic
        <router-link to="/individual-notes/recognition">
          recognition
          exercises
        </router-link>, while also doing the internalisation exercises of the two missing
        scale degrees, »Fa« and »Ti«.
      </p><p>
        <InlineConfigurator
          :prog-id="2003"
          t-type="internalization"
          :config="{degree: 5}"
        >
          »Fa« Internalisation
        </InlineConfigurator>
      </p>
      <p>
        <InlineConfigurator
          :prog-id="2006"
          t-type="internalization"
          :config="{degree: 11}"
        >
          »Ti« Internalisation
        </InlineConfigurator>
      </p>
      <v-btn
        style="float: right"
        color="secondary"
        class="ma-2"
        to="/individual-notes/recognition"
      >
        Next Chapter
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import InlineConfigurator from "../components/InlineConfigurator";

export default {
  name: "IndividualNotesMethod",
  components: {
    InlineConfigurator,
  },
  data: function () {
    return {
      exStep: 1,
      curStep1: 1,
      curStep2: 1,
    };
  },
};
</script>
