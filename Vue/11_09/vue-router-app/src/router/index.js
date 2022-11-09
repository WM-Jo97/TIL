import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '@/views/DogView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:usesrName',
    name: 'hello',
    component: HelloView,
  },
  {
    path : '/login',
    name : 'login',
    component : LoginView,
    beforEnter(to, from, next){
      const isLoggedIn = true
      if(isLoggedIn === true){
        console.log('이미 로그인 되어있음')
        next({ name: 'home' })
      } else{
        next()
      }
    }
  },
  {
    path : '/404',
    name : 'NotFound404',
    component : NotFound404,
  },
  {
    path: '/dog/:breed',
    name : 'dog',
    component : DogView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = false
  const authPages = ['hello']
  const isAuthRequired = authPages.includes(to.name)
  if (isAuthRequired && !isLoggedIn){
    console.log('login으로 이동')
    next({ name : 'login' })
  }else{
    console.log('to로 이동')
    next()
  }
})

export default router
