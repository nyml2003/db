import { createStore } from 'vuex'

export default createStore({
  state: {
    columns:new Map([
      ["Pno","患者编号"],
      ["Pname","患者姓名"],
      ["Pid","身份证号"],
      ["Pino","社会保险号"],
      ["Pmno","医疗卡识别号"],
      ["Psex","性别"],
      ["Pbd","出生日期"],
      ["Padd","地址"],
      ["单位电话","单位电话"],
      ["家庭电话","家庭电话"],
      ["手机","手机"],
      ["Dno","医生编号"],
      ["Dname","医生姓名"],
      ["Dsex","性别"],
      ["Dage","年龄"],
      ["Ddeptno","所属部门编号"],
      ["Tno","职称编号"],
      ["DeptNo","部门编号"],
      ["DeptName","部门名称"],
      ["ParentDeptNo","上级部门编号"],
      ["Manager","部门负责人编号"],
    ])
  },
  getters: {
  },
  mutations: {
    
  },
  actions: {
  },
  modules: {
  }
})
