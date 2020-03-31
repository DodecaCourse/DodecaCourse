import Vue from 'vue'
import Home from './views/Home.vue'
import App from './App.vue'
import About from './views/About.vue'
import VueRouter from "vue-router";
import TonicInternalization from "./views/TonicInternalization";
import vuetify from './plugins/vuetify';
import TonicInternalizationOverview from "./views/TonicInternalizationOverview";
import TonicInternalizationMethod from "./views/TonicInternalizationMethod";
import TonicInternalizationTest from "./views/TonicInternalizationTest";
import NotFound from "./views/NotFound";


Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(vuetify);

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/internalization', component: TonicInternalization},
    { path: '/tonicinternalization/overview', component: TonicInternalizationOverview},
    { path: '/tonicinternalization/method', component: TonicInternalizationMethod},
    { path: '/tonicinternalization/test', component: TonicInternalizationTest},
    { path: '/*', component: NotFound}
  ]
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
