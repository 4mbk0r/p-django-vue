// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import '@mdi/font/css/materialdesignicons.css'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueCookies from 'vue-cookies';


const Cookies = require('js-cookie');
Vue.config.productionTip = false
Vue.use(Cookies);
Vue.use(VueCookies);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
/* eslint-disable no-new */
Vue.use(Vuetify, )

export default new Vuetify({ icons: { iconfont: 'mdi'}}) // default - only for display purposes }, })
new Vue({
  el: '#app',
  router,
  vuetify : new Vuetify(),
  components: { App },
  template: '<App/>'
})
