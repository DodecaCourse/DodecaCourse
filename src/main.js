import Vue from 'vue'
import Home from './views/Home.vue'
import App from './App.vue'
import About from './views/About.vue'
import VueRouter from "vue-router";
import vuetify from './plugins/vuetify';
import TonicInternalizationOverview from "./views/TonicInternalizationOverview";
import TonicInternalizationMethod from "./views/TonicInternalizationMethod";
import TonicInternalizationTest from "./views/TonicInternalizationTest";
import NotFound from "./views/NotFound";
import IndividualNotesOverview from "./views/IndividualNotesOverview";
import IndividualNotesInternalizationMethod from "./views/IndividualNotesInternalizationMethod";
import IndividualNotesInternalizationTest from "./views/IndividualNotesInternalizationTest";
import IndividualNotesRecognitionMethod from "./views/IndividualNotesRecognitionMethod";
import IndividualNotesRecognitionTest from "./views/IndividualNotesRecognitionTest";
import RecognisingMelodiesOverview from "./views/RecognisingMelodiesOverview";
import RecognisingMelodiesMethod from "./views/RecognisingMelodiesMethod";
import TeacherPlayground from "./views/TeacherPlayground";


Vue.config.productionTip = false;

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/teacher-playground', component: TeacherPlayground},
    { path: '/tonic-internalization/overview', component: TonicInternalizationOverview},
    { path: '/tonic-internalization/method', component: TonicInternalizationMethod},
    { path: '/tonic-internalization/test', component: TonicInternalizationTest},
    { path: '/individual-notes/overview', component: IndividualNotesOverview},
    { path: '/individual-notes/internalisation-method', component: IndividualNotesInternalizationMethod},
    { path: '/individual-notes/internalisation-test', component: IndividualNotesInternalizationTest},
    { path: '/individual-notes/recognition-method', component: IndividualNotesRecognitionMethod},
    { path: '/individual-notes/recognition-test', component: IndividualNotesRecognitionTest},
    { path: '/recognising-melodies/overview', component: RecognisingMelodiesOverview},
    { path: '/recognising-melodies/recognition-exercises', component: RecognisingMelodiesMethod},
    { path: '/*', component: NotFound}
  ],
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    else {
      return {x: 0, y: 0};
    }
  }
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
