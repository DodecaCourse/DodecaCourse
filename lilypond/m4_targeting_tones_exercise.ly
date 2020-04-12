\version "2.18.2"
\paper {
  indent = 0\cm
  \context {}
}
\score {
  <<
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative c' { \repeat unfold 4 {<c e g>1 c1} \bar "||"} \break
        \relative c' { \repeat unfold 4 {<e gis b>1 e1} \bar "||"} \break
        \relative c' { \repeat unfold 4 {<f a c>1 f1} \bar "||"}
      }
    }
    \new Lyrics {
      \lyricsto "melody" {
       \repeat unfold 4 { C,E,G C } \break
       \repeat unfold 4 { \markup{E,G♯,B} E } \break
       \repeat unfold 4 { F,A,C F }
    }
    }
  >>
}