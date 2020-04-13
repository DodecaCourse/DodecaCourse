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
}

\score {
  <<
    \new ChordNames = "chords" {
      \set chordChanges = ##t
      \chordmode { c1 f2 g2 c1 c\breve
                   \repeat unfold 7 {\powerChords c\breve:1.5 \set chordChanges = ##t c1:1.5 \set chordChanges = ##f }
      }
    }
    \new Lyrics \lyrics \with { alignAboveContext = "chords" }  {
      I1 IV2 V I1
    }
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative c''{ \comp #12 d1 r2\fermata r2^\markup{»Re«} \bar "||"
                       \comp #4 a1 r2\fermata r2^\markup{»La«} \bar "||" \break
                       \comp #4 c1 r2\fermata r2^\markup{»Do«} \bar "||"
                       \comp #4 g1 r2\fermata r2^\markup{»So«} \bar "||"
                       \comp #4 c1 r2\fermata r2^\markup{»Do«} \bar "||"\break
                       \comp #4 e,1 r2\fermata r2^\markup{»Mi«} \bar "||"
                       \comp #4 a1 r2\fermata r2^\markup{»La«} \bar "||"
                       \comp #4 d1 r2\fermata r2^\markup{»Re«} \bar "||"
        }
       
      }
    }
  >>
}