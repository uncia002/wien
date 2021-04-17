import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';
Vue.config.devtools = true;
Vue.config.productionTip = false


/* eslint-disable no-new */
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
