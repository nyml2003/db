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
      ["Sno","工资类型"],
      ["Ttype","职称类型"],
      ["Ttrade","所属行业"],
      ["Slevel","工资级别"],
      ["Snumber","工资数额"],
      ["GMno","主单编号"],
      ["GMdate","入库时间"],
      ["GMname","主单名称"],
      ["GSno","子单编号"],
      ["Mno","药品编号"],
      ["GSnumber","数量"],
      ["GSunit","单位"],
      ["GSbatch","批号"],
      ["GSprice","单价"],
      ["GSexpdate","有效期"],
      ["Mname","药品名称"],
      ["Mprice","药品价格"],
      ["Mtype","药品类型"],
      ["Munit","药品单位"],
      ["DGno","诊断编号"],
      ["Symptom","症状"],
      ["Diagnosis","诊断结论"],
      ["DGtime","诊断时间"],
      ["Rfee","就诊费"]
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
