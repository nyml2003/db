import { createRouter, createWebHashHistory } from 'vue-router'
const routes = [
  {
    path: '/home',
    name: 'home',
    component: ()=>import('../views/HomeView.vue')
  },
  {
    path:'/data',
    name:'data',
    component:()=>import('../views/DataRaw.vue')
  },
  {
    path:'/view',
    name:'view',
    component:()=>import('../views/DataView.vue')
  },
  {
    path:'/',
    name:'login',
    component:()=>import('../views/LoginView.vue')
  },
  {
    path:'/register',
    name:'register',
    component:()=>import('../views/RegisterView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})



// 路由配置...

export default router
