import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Patient from '../views/PatientRaw.vue'
import Dept from '../views/DeptRaw.vue'
import Doctor from '../views/DoctorRaw.vue'
import Title from '../views/TitleRaw.vue'
import Salary from '../views/SalaryRaw.vue'
import GoDown_Entry from '../views/Godown_Entry_Raw.vue'
import GoDown_Slave from '../views/Godown_Slave_Raw.vue'
import Medicine from '../views/MedicineRaw.vue'
import Diagnosis from '../views/DiagnosisRaw.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/patient',
    name: 'patient',
    component: Patient
  },
  {
    path: '/dept',
    name: 'dept',
    component: Dept
  },
  {
    path: '/doctor',
    name: 'doctor',
    component: Doctor
  },
  {
    path: '/title',
    name: 'title',
    component: Title
  },
  {
    path: '/salary', 
    name: 'salary',
    component: Salary
  },
  {
    path: '/godown_entry',
    name: 'godown_entry',
    component: GoDown_Entry
  },
  {
    path: '/godown_slave',
    name: 'godown_slave',
    component: GoDown_Slave
  },
  {
    path: '/medicine',
    name: 'medicine',
    component: Medicine
  },
  {
    path: '/diagnosis',
    name: 'diagnosis',
    component: Diagnosis
  },
  {
    path:'/data_raw/:table',
    name:'data_raw',
    component:()=>import('../views/DataRaw.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})



// 路由配置...

export default router
