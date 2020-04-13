\version "2.18.2"
\paper {
  indent = 0\cm
  \context {}
}
\score {
  <<
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative c' {  {<c e g>1 r1 c1 r1} {<a' cis e>1 r1 a1 r1} } \break
        \relative c' {  {<d fis a>1 r1 d1 r1} {<f a c>1 r1 f1 r1} \bar "||" } \break
      }
    }
    \new Lyrics {
      \lyricsto "melody" {
        C,E,G C A,C♯,E A D,F♯,A D F,A,C F
    }
    }
  >>
}