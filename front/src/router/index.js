import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PatientView from '../views/PatientView.vue'
import DeptView from '../views/DeptView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/patient',
    name: 'patient',
    component: PatientView
  },
  {
    path: '/dept',
    name: 'dept',
    component: DeptView
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})



// 路由配置...

export default router
