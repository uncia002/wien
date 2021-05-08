import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';
import axios from 'axios' //追記
import VueAxios from 'vue-axios' //追記

/* eslint-disable no-new */
Vue.config.devtools = true;
Vue.config.productionTip = false
Vue.use(VueAxios, axios) //追記

new Vue({
  el: '#app',
  data:{
    tablewidth:500
  },
  router,
  vuetify,
  render: h => h(App)

}).$mount("#app");

Vue.component(VueCropper)
