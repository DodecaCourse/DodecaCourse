<template>
    <v-layout align-center justify-center row>
        <v-flex class="article" xs10>
            <h1 class="hidden-xs-only">2. Recognising Individual Notes</h1>
            <h2>Scale Degrees</h2>
            <p>
                Now that you can recognise the sound of the tonic, the next step is
                to learn to recognise other notes in relation to the tonic.</p>
            <p>Scale degrees are
                the tool that we use to do this.</p>
            <p>Scale degrees
                number each note in a scale based on its position in that scale. The
                tonic is labelled as scale degree one, the second note is labelled as
                scale degree two and so on. Take a look at the diagram below to see
                the C major scale with scale degrees shown below it:</p>
            <p>
                <v-img contain :class="{'invert-img': $vuetify.theme.dark}" max-height="10ch" max-width="83.5vw" src="/img/m2_c_major.svg"
                title="C Major Scale with Scale Degrees"/>
            </p>

            <p>In the tradition of music education, scale degrees have always been a tool
                to remember musical ideas independent of the notes of a specific key.
                As singing plays a major role in internalising music, a more singable
                alternative to name the scale degrees was developed, the
                <a href="https://en.wikipedia.org/wiki/Solf%C3%A8ge#Movable_do_solf%C3%A8ge">movable do solfège</a>
                system.
            </p>

            <p>Instead of one, two, three, ... the scale degrees of the major scale become
                »Do«, »Re«, »Mi«, »Fa«, »So«, »La« and »Ti«. The picture below shows the
                C major scale with both systems applied.
            </p>
            <p>
                <v-img contain :class="{'invert-img': $vuetify.theme.dark}" max-height="10ch" max-width="83.5vw" src="/img/m2_c_major_solfege.svg"
                       title="C Major Scale with Scale Degrees and Solfege"/>
            </p>
            <p>
                These syllables are really useful when it comes to naming the scale degrees while
                singing. This opens up the possibility of an even deeper connection of sound and
                name and will therefore be used in this course.
            </p>
            <p>If we were to
                write out a different major scale C would no longer be Do,
                the new tonic would be. You can see scale degrees applied to the F
                major scale below where F is now Do (scale degree 1) and C has become So (the
                fifth scale degree).</p>
            <p>
                <v-img contain :class="{'invert-img': $vuetify.theme.dark}" max-height="10ch" max-width="83.5vw" src="/img/m2_f_major_solfege.svg"
                title="F Major Scale with Scale Degrees"/>
            </p>
            <p>Scale degrees are
                incredibly useful because each scale degree has a unique and
                identifiable sound. Now that we can identify the tonic by ear, we can
                start learning the unique and identifiable sound of each scale degree
                so we can recognise any note by ear.</p>
            <p>Above we’ve
                applied scale degrees to the notes of the major scale but we can
                apply scale degrees to any note so they’re useful even for very
                complicated chromatic music. A minor third can be labelled as »Me« (or b3) or a
                raised fourth scale degree can labelled as »Fi« (or #4) for example.</p>
            <p>However, we must
                walk before we can run so in the Dodeca course we focus
                specifically on the scale degrees of the major and minor scales (the
                minor scale is introduced in Module 5). These two scales form the
                backbone of so many styles of music so they’re the perfect place to
                start, and once you’ve mastered them, adding scale degrees from
                outside those two scales is much easier.</p>
            <p>The twelve scale degrees can be displayed in the style of a clock,
                with »Do« being twelve o'clock and the other scale degrees following
                clockwise. The position of the hour corresponds to the number of half steps
                you have to go down to get back to the tonic. Below you can see the complete circle,
                in the second picture only the major scale is selected:</p>
            <div style="display: flex; justify-content: center; pointer-events: none">
                <DegreeCircle :submit-solution="function() {}" :solution="0"
                              :enabled-buttons="[0,1,2,3,4,5,6,7,8,9,10,11]"
                              :labels="['Do', 'Ra', 'Re', 'Me', 'Mi', 'Fa', 'Fi', 'So', 'Le', 'La', 'Te', 'Ti']">
                </DegreeCircle>
                <div style="margin-left: 5px">
                    <DegreeCircle :submit-solution="function() {}" :solution="0"
                                  :enabled-buttons="[0,2,4,5,7,9,11]"
                                  :labels="['Do', 'Ra', 'Re', 'Me', 'Mi', 'Fa', 'Fi', 'So', 'Le', 'La', 'Te', 'Ti']">
                    </DegreeCircle>
                </div>
            </div>
            <p>This system will be used
                throughout the exercises, as it allows to display to relevant scale
                degrees in a compact and efficient way, using the circle as an icon.
                Look at the examples below to see how it works:
            </p>
            <div style="display: flex; justify-content: left; align-items: center; margin-left: 3ch">
            <DegreeCirclePictogram :enabled-degrees="[0]"></DegreeCirclePictogram>
                <span style="margin-left: 1ch">Only »Do« is selected</span>
            </div>
            <div style="display: flex; justify-content: left; align-items: center; margin-left: 3ch">
                <DegreeCirclePictogram :enabled-degrees="[0,2,4,7,9]"></DegreeCirclePictogram>
                <span style="margin-left: 1ch">The pentatonic scale (Do, Re, Mi, So, La)</span>
            </div>
            <div style="display: flex; justify-content: left; align-items: center; margin-left: 3ch">
                <DegreeCirclePictogram :enabled-degrees="[0,2,4,5,7,9,11]"></DegreeCirclePictogram>
                <span style="margin-left: 1ch">The major scale (Do, Re, Mi, Fa, So, La, Ti)</span>
            </div>
            <p v-show="!$vuetify.breakpoint.xsOnly">
                You can hover over an icon to see the selected degrees as text.
            </p>
            <p>In this module you
                will internalise the sound of each scale degree from the major scale,
                just as you did in the last module with the tonic. The approach is
                simple: focus on an internalisation exercise for one scale degree at
                a time until you can pass the corresponding test, then move onto the
                next scale degree.</p>
            <p>Once you've passed
                the internalisation test for all the scale degrees of the pentatonic
                scale (scale degrees Do, Re, Mi, So and La) we'll also introduce a new
                exercise, called a recognition exercise which gives you an easy way
                to revise and consolidate everything you've learned up until now.</p>
            <p>There is an extra
                step in the approach to the internalisation exercises for this module
                so even though you're already familiar with them, continue to the
                next lesson to find out before starting on the exercises.</p>
            <v-btn style="float: right" color="secondary" class="ma-2"
                   to="/individual-notes/internalisation">Next Chapter</v-btn>
        </v-flex>
    </v-layout>
</template>

<script>
    import DegreeCircle from "../components/DegreeCircle";
    import DegreeCirclePictogram from "../components/DegreeCirclePictogram";
    export default {
        name: "IndividualNotesMethod",
        components: {
            DegreeCirclePictogram,
            DegreeCircle
        },
    }
</script>
