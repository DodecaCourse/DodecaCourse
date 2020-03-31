<template>
    <v-layout row align-center justify-center>
        <v-flex xs10>
            <h1>2. Recognising Individual Notes</h1>
            <h2>Method</h2>
            <v-banner id="player" elevation="0" sticky app>
                <InternalizationPlayer />
            </v-banner>
            <ol>
                <li><p>
                    Read the lesson on scale degrees to learn about the system you’ll
                    use to recognise each note as you develop relative pitch.</p></li>
                <li><p>Continue to
                    the lessons on individual note internalisation exercises, individual
                    note internalisation tests and recognition exercises. We’ll add an
                    additional step to the internalisation exercises and tests in this
                    module so make sure you read the lesson to find out what it is.</p></li>
                <li><p>Practice one
                    internalisation exercise until you can pass the corresponding test.</p></li>
                <li><p>Repeat this
                    with all the scale degrees from the pentatonic scale (2, 3, 5 and
                    6).</p></li>
                <li><p>Add the
                    pentatonic scale recognition exercises to your practice routine.</p></li>
                <li><p>Split your
                    practice sessions between the pentatonic scale recognition exercises
                    and the final two internalisation exercises until you can pass the
                    internalisation tests and get over 80% on the recognition exercises.</p></li>
                <li><p>Focus
                    on the major scale recognition exercises until you reach the target
                    for the module.</p></li>
            </ol>
            <p>
                Now that you can recognise the sound of the tonic, the next step is
                to learn to recognise other notes in relation to the tonic.</p>
            <p>Scale degrees are
                the tool that we use here at Ear Training HQ to do this.</p>
            <p>Scale degrees
                number each note in a scale based on its position in that scale. The
                tonic is labelled as scale degree one, the second note is labelled as
                scale degree two and so on. Take a look at the diagram below to see
                the C major scale with scale degrees shown below it:</p>
            <p><br/>

            </p>
            <p><img src="/img/m2_c_major.png" alt="C major"/>
            </p>
            <p>C Major Scale with
                Scale Degrees</p>
            <p>If we were to
                write out a different major scale C would no longer be scale degree
                1, the new tonic would be. You can see scale degrees applied to the F
                major scale below where F is now scale degree 1 and C has become the
                fifth scale degree.</p>
            <p><img src="/img/m2_f_major.png" alt="F major"/>
            </p>
            <p>F Major Scale with
                Scale Degrees</p>
            <p>Scale degrees are
                incredibly useful because each scale degree has a unique and
                identifiable sound. Now that we can identify the tonic by ear, we can
                start learning the unique and identifiable sound of each scale degree
                so we can recognise any note by ear.</p>
            <p>Above we’ve
                applied scale degrees to the notes of the major scale but we can
                apply scale degrees to any note so they’re useful even for very
                complicated chromatic music. A minor third can be labelled as b3 or a
                raised fourth scale degree can labelled as #4 for example.</p>
            <p>However, we must
                walk before we can run so in the Ear Training HQ method we focus
                specifically on the scale degrees of the major and minor scales (the
                minor scale is introduced in Module 5). These two scales form the
                backbone of so many styles of music so they’re the perfect place to
                start, and once you’ve mastered them, adding scale degrees from
                outside those two scales is much easier.</p>
            <p>In this module you
                will internalise the sound of each scale degree from the major scale,
                just as you did in the last module with the tonic. The approach is
                simple: focus on an internalisation exercise for one scale degree at
                a time until you can pass the corresponding test, then move onto the
                next scale degree.</p>
            <p>Once you've passed
                the internalisation test for all the scale degrees of the pentatonic
                scale (scale degrees 1, 2, 3, 5 and 6) we'll also introduce a new
                exercise, called a recognition exercise which gives you an easy way
                to revise and consolidate everything you've learned up until now.</p>
            <p>There is an extra
                step in the approach to the internalisation exercises for this module
                so even though you're already familiar with them, continue to the
                next lesson to find out before starting on the exercises.</p>
            <p><br/>

            </p>
            <p>
                In this module there is an internalisation exercise for each scale
                degree. The scale degree that an internalisation exercise focuses on
                is called the target scale degree of the exercise.</p>
            <p>These exercises
                are just like the internalisation exercise from the first module. A I
                - IV - V progression is played for the first two bars, followed by 8
                bars with the tonic chord played in every second bar. However, the
                target scale degree is played in each bar instead of the tonic.</p>
            <p>You can see the
                first 10 bars from the internalisation exercise for the second scale
                degree below.</p>
            <p><img src="/img/m2_10bars.png" alt="10 Bars"/>
            </p>
            <p>
                The approach to the individual note exercises is the same as it was
                in the previous module with one addition: when you sing the scale
                degree, hold it for a couple of seconds then sing the tonic. Then
                return to the target scale degree.</p>
            <p>If you can sing
                the tonic in this way it shows that you're recognising the tonic
                clearly so you're hearing the relationship between the tonic and the
                target scale degree.</p>
            <p>So the complete
                process is:</p>
            <ol>
                <li><p>Listen to the
                    I - IV - V Progression: Simply listening to the I - IV - V
                    progression will make it clear to your ear which note is the tonic
                    (even if you can't identify which note it is yet). So just sit back
                    and listen.</p></li>
                <li><p>Focus your
                    attention on the target scale degree: for the following 8 bars,
                    listen closely to the target scale degree. Listen to the way that it
                    sounds in relation to the tonic chord.</p></li>
                <li><p>Sing the
                    target scale degree: alongside listening to the sound of the target
                    scale degree, singing it will help you to really hear and
                    internalise it's stable sound.</p></li>
                <li><p>Sing the
                    tonic: after you sing the target scale degree for a couple of
                    seconds, sing the tonic to ensure you can recognise it accurately.</p></li>
                <li><p>Sing the
                    target scale degree again: return to the target scale degree and
                    continue listening to the way that it sounds next to the tonic
                    chord.</p></li>
                <li><p>Repeat: when
                    the I - IV - V progression is played in a new key, listen to the
                    progression as you did the first time. This will establish a new
                    note as the tonic and then you can repeat listening to/singing the
                    target scale degree in the new key.</p></li>
            </ol>
            <p>Practice
                with this exercise until you start to feel confident that you are
                internalising the sound of the target scale degree. Then try the
                internalisation test for the target scale degree.</p>
        </v-flex>
    </v-layout>
</template>

<script>
    import InternalizationPlayer from "../components/InternalizationPlayer";

    export default {
        name: "IndividualNotesMethod",
        components: {
            InternalizationPlayer
        }
    }
</script>
