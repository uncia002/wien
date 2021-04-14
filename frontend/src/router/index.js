import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Upload from '@/components/Upload.vue'
import Table from '@/components/Table.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Table
    },
    {
      path: '/upload',
      component: Upload
    }
  ]
})
