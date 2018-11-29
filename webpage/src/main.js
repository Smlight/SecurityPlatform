// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'xterm/dist/xterm.css'
import 'element-ui/lib/theme-chalk/index.css' // Element-ui 默认主题

import Qs from 'qs'
import axios from 'axios'
import VueAxios from 'vue-axios'

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

axios.defaults.withCredentials = true;
var axios_instance = axios.create({
  transformRequest: [function (data) {
    data = Qs.stringify(data);
    return data;
  }],
  headers:{
    'Content-Type':'application/x-www-form-urlencoded',
    'X-CSRFToken': getCookie('csrftoken')
  }
});
Vue.use(VueAxios, axios_instance);
Vue.use(ElementUI);

Vue.config.productionTip = false;


new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
}).$mount('#app');

export default getCookie
