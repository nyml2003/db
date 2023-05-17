import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/data',
    name:'data',
    component:()=>import('../views/DataRaw.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})



// 路由配置...

export default router
