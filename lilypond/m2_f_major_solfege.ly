\version "2.18.2"
#(define Ez_numbers_engraver
   (make-engraver
    (acknowledgers
     ((note-head-interface engraver grob source-engraver)
      (let* ((context (ly:translator-context engraver))
	     (tonic-pitch (ly:context-property context 'tonic))
	     (tonic-name (ly:pitch-notename tonic-pitch))
	     (grob-pitch
	      (ly:event-property (event-cause grob) 'pitch))
	     (grob-name (ly:pitch-notename grob-pitch))
	     (delta (modulo (- grob-name tonic-name) 7))
	     (note-names
	      (make-vector 7 (number->string (1+ delta)))))
	(ly:grob-set-property! grob 'note-names note-names))))))

#(set-global-staff-size 26)
\score {
  <<
    \new Staff = "staff" {
      \new Voice = "melody" {
        \relative f'{ \key f \major \easyHeadsOn f g a bes c d e f \easyHeadsOff }
      }
    }
    \new Lyrics {
      \lyricsto "melody" {
        F G A \markup{\concat{B\small\flat}} C D E F
      }
    }
    \new Lyrics \with { alignAboveContext = "staff" } {
      \lyricsto "melody" {
        Do Re Mi Fa So La Ti Do
      }
    }
  >>
  \layout {
    ragged-right = ##t
    \context {
      \Score
      \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/16)
    }
    \context {
    \Voice
    \consists \Ez_numbers_engraver
  }
  }
}