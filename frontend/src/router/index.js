import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/home',
    name: 'main',
    component: () => import('../views/MainView.vue'),
    children: [{
        path: '/home',
        name: 'home',
        component: () => import('../views/HomeView.vue')
      },
      {
        path: '/user',
        name: 'user',
        component: () => import('../views/UserView.vue')
      },
      {
        path: '/other',
        name: 'other',
        component: () => import('../views/OtherView.vue')
      },
      {
        path: '/return',
        name: 'return',
        component: () => import('../views/ReturnView.vue')
      },
      {
        path: '/available',
        name: 'available',
        component: () => import('../views/ReturnView.vue')
      }
      
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router