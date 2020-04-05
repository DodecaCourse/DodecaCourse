\version "2.18.2"
rs = {
  \once \override Rest.stencil = #ly:percent-repeat-item-interface::beat-slash
  \once \override Rest.thickness = #0.48
  \once \override Rest.slope = #1.7
  r4
}
% Function to print a specified number of slashes
comp = #(define-music-function (parser location count) (integer?)
  #{
    \override Rest.stencil = #ly:percent-repeat-item-interface::beat-slash
    \override Rest.thickness = #0.48
    \override Rest.slope = #1.7
    \repeat unfold $count { r4 }
    \revert Rest.stencil
  #}
)
\paper {
  indent = 0\cm
  \context {}
}
\score {
  <<
    \new ChordNames = "chords" {
      \chordmode { c1 f2 g2 \set chordChanges = ##t \repeat unfold 6 c1 } \break
      \chordmode { bes1 ees2 f2 \set chordChanges = ##t \repeat unfold 6 bes1 } \break
      \chordmode { d1 g2 a2 \set chordChanges = ##t \repeat unfold 6 d1 } \break
    }
    \new Lyrics \lyrics \with { alignAboveContext = "chords" } {
      I1 IV2 V I1 \repeat unfold 5 _ \break
      I1 IV2 V I1 \repeat unfold 5 _ \break
      I1 IV2 V I1 \repeat unfold 5 _
    }
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative c' { \key c \major \comp #12 r1 r1 r1 <c c' c'>~  <c c' c'> \bar "||"} \break
        \relative c' { \key c \major \comp #12 r1 r1 r1 <bes bes' bes'>~  <bes bes' bes'> \bar "||"} \break
        \relative c' { \key c \major \comp #12 r1 r1 r1 <d d' d'>~  <d d' d'> \bar "||"}
      }
    }
    \new Lyrics \lyrics {
       \repeat unfold 6 _ \markup{1} \markup{1} \break
       \repeat unfold 6 _ \markup{1} \markup{1} \break
       \repeat unfold 6 _ \markup{1} \markup{1}
    }
  >>
}