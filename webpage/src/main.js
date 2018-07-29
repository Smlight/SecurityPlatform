// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css' // Element-ui 默认主题

Vue.config.productionTip = false
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
}).$mount('#app');

import Qs from 'qs'
import axios from 'axios'
import VueAxios from 'vue-axios'
var axios_instance = axios.create({
  transformRequest: [function (data) {
    data = Qs.stringify(data);
    return data;
  }],
  headers:{'Content-Type':'application/x-www-form-urlencoded'}
})
Vue.use(VueAxios, axios_instance)
