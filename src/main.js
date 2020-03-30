import Vue from 'vue'
import Home from './views/Home.vue'
import App from './App.vue'
import About from './views/About.vue'
import VueRouter from "vue-router";
import Vuetify from "vuetify";
import Internalization from "./views/Internalization";
import TonicInternalization from "./views/TonicInternalization";
import vuetify from './plugins/vuetify';


Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(vuetify);

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/internalization', component: Internalization},
    { path: '/tonicinternalization', component: TonicInternalization}
  ]
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
