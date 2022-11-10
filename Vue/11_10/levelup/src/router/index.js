import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import NocolorView from '@/views/NocolorView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path:'/Nocolor',
    name: 'NocolorView',
    component: NocolorView
  },
  {
    path: '*',
    name: 'NotFound404',
    component: NotFound404
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
