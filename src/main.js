import Vue from 'vue'
import Home from './views/Home.vue'
import App from './App.vue'
import About from './views/About.vue'
import VueRouter from "vue-router";
import vuetify from './plugins/vuetify';
import M1TonicInternalizationOverview from "./views/M1TonicInternalizationOverview";
import M1TheTonic from "./views/M1TheTonic";
import M1TonicInternalizationExercise from "./views/M1TonicInternalizationExercise";
import M1TonicInternalizationTest from "./views/M1TonicInternalizationTest";
import NotFound from "./views/NotFound";
import M2IndividualNotesOverview from "./views/M2IndividualNotesOverview";
import M2ScaleDegrees from "./views/M2ScaleDegrees";
import M2IndividualNotesInternalization from "./views/M2IndividualNotesInternalization";
import M2IndividualNotesRecognition from "./views/M2IndividualNotesRecognition";
import M3RecognisingMelodiesOverview from "./views/M3RecognisingMelodiesOverview";
import M3RecognisingMelodies from "./views/M3RecognisingMelodies";
import TeacherPlayground from "./views/TeacherPlayground";
import M4RecognisingChordsOverview from "./views/M4RecognisingChordsOverview";
import M4TargetingTones from "./views/M4TargetingTones";
import M4ChordQualityRecognition from "./views/M4ChordQualityRecognition";
import M4DiatonicChordsInternalization from "./views/M4DiatonicChordsInternalization";
import M4DiatonicChordsRecognition from "./views/M4DiatonicChordsRecognition";


Vue.config.productionTip = false;

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/teacher-playground', component: TeacherPlayground},
    { path: '/tonic-internalization/overview', component: M1TonicInternalizationOverview},
    { path: '/tonic-internalization/tonic', component: M1TheTonic},
    { path: '/tonic-internalization/exercise', component: M1TonicInternalizationExercise},
    { path: '/tonic-internalization/test', component: M1TonicInternalizationTest},
    { path: '/individual-notes/overview', component: M2IndividualNotesOverview},
    { path: '/individual-notes/scale-degrees', component: M2ScaleDegrees},
    { path: '/individual-notes/internalisation', component: M2IndividualNotesInternalization},
    { path: '/individual-notes/recognition', component: M2IndividualNotesRecognition},
    { path: '/recognising-melodies/overview', component: M3RecognisingMelodiesOverview},
    { path: '/recognising-melodies/exercise-test', component: M3RecognisingMelodies},
    { path: '/chords/overview', component: M4RecognisingChordsOverview },
    { path: '/chords/targeting-tones', component: M4TargetingTones },
    { path: '/chords/chord-quality-recognition', component: M4ChordQualityRecognition },
    { path: '/chords/diatonic-chord-internalisation', component: M4DiatonicChordsInternalization },
    { path: '/chords/diatonic-chord-recognition', component: M4DiatonicChordsRecognition },
    { path: '/*', component: NotFound}
  ],
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
      return {selector: to.hash};
    } else if (savedPosition) {
      return savedPosition
    } else {
      return {x: 0, y: 0};
    }
  }
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
