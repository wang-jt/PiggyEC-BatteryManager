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
    path: '/register',
    name: 'register',
    component: () => import('../views/RegiView.vue')
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
        path: '/overview',
        name: 'overview',
        component: () => import('../views/OverView.vue')
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
        component: () => import('../views/BatteryView.vue')
      },
      {
        path: '/order',
        name: 'order',
        component: () => import('../views/WOView.vue')
      },
      {
        path: '/cabinet',
        name: 'cabinet',
        component: () => import('../views/CabinetView.vue')
      },
      {
        path: '/company',
        name: 'company',
        component: () => import('../views/CompanyView.vue')
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