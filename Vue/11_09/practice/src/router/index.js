import Vue from 'vue'
import VueRouter from 'vue-router'
import FirstView from '@/views/FirstView.vue'
import SecondView from '@/views/SecondView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/firstview',
    name: 'FirstView',
    component: FirstView
  },
  {
    path: '/secondview',
    name: 'SecondView',
    component: SecondView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
