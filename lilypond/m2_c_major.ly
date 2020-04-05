\version "2.18.2"
\score {
  <<
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative c'{ c d e f g a b c }
      }
    }
    \new Lyrics \with { alignAboveContext = "staff" } {
      \lyricsto "melody" {
        \markup{1} \markup{2} \markup{3} \markup{4} \markup{5} \markup{6} \markup{7} \markup{1}
      }
    }
    \new Lyrics {
      \lyricsto "melody" {
        C D E F G A B C
      }
    }
  >>
  \layout {
    \context {
      \Score
      \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/16)
    }
  }
}