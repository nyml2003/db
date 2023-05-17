<template>
  <el-container>
    <el-aside style="width: fit-content">
      <!-- <el-menu :router="true" class="el-menu-vertical-demo" default-active="2">
    <el-menu-item index="/">
      <el-icon><HomeFilled /></el-icon>
      首页
    </el-menu-item>
    <el-sub-menu>
      <template #title><el-icon><Document /></el-icon>原始表格</template>
    <el-menu-item index="/patient">
      <el-icon><Postcard /></el-icon>
      患者
    </el-menu-item>
    <el-menu-item index="/dept">
      <el-icon><Postcard /></el-icon>
      部门
    </el-menu-item>
    <el-sub-menu index="">
      <template #title><el-icon><Postcard /></el-icon>员工</template>
      <el-menu-item index="/doctor">
        <el-icon><Postcard /></el-icon>医生
      </el-menu-item>
    </el-sub-menu> 
    <el-menu-item index="/Title">
      <el-icon><Postcard /></el-icon>
      职称
    </el-menu-item>
    <el-menu-item index="/Salary">
      <el-icon><Postcard /></el-icon>
      工资
    </el-menu-item>
    <el-menu-item index="/GoDown_Entry">
      <el-icon><Postcard /></el-icon>
      入库主单
    </el-menu-item>
    <el-menu-item index="/GoDown_Slave">
      <el-icon><Postcard /></el-icon>
      入库从单
    </el-menu-item>
    <el-menu-item index="/Medicine">
      <el-icon><Postcard /></el-icon>
      药品
    </el-menu-item>
    <el-menu-item index="/Diagnosis">
      <el-icon><Postcard /></el-icon>
      就诊
    </el-menu-item>
    

    </el-sub-menu>
     -->
      <!-- </el-menu> -->
      <el-menu router :default-active="$route.path" class="el-menu-vertical-demo">
        <el-menu-item index="/">
          <el-icon>
            <HomeFilled />
          </el-icon>
          首页
        </el-menu-item>
        <el-sub-menu index="">
          <template #title><el-icon>
              <Document />
            </el-icon>原始表格</template>
          <el-menu-item v-for="item in items" :key="item.id" index="data_raw"
            :route="{ path: item.url, params: {} }">
            <template #title><el-icon>
                <Postcard />
              </el-icon>{{ item.name }}</template>
          </el-menu-item>

        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-main>
      <router-view />
    </el-main>

  </el-container>
</template>

<script setup>
const items = [
  {
    id: 1, url: "/patient", name: "患者",
    dataColumns: [
      "Pno",
      "Pname",
      "Pid",
      "Pino",
      "Pmno",
      "Psex",
      "Pbd",
      "Padd"
    ], table: "`cs2305.patient`", pk: "Pno", dateCol: "Pbd"
  },
  {
    id: 2, url: "/dept", name: "部门", dataColumns: [
      "DeptNo",
      "DeptName",
      "ParentDeptNo",
      "Manager"
    ], table: "`cs2305.dept`", pk: "DeptNo", dateCol: null
  },
  {
    id: 3, url: "/doctor", name: "医生", dataColumns: [
      "Dno",
      "Dname",
      "Dsex",
      "Dage",
      "Ddeptno",
      "Tno"
    ], table: "`cs2305.doctor`", pk: "Dno", dateCol: null
  },
  {
    id: 4, url: "/Title", name: "职称", dataColumns: [
      "Tno",
      "Sno",
      "Ttype",
      "Ttrade"
    ], table: "`cs2305.title`", pk: "Tno", dateCol: null
  },
  {
    id: 5, url: "/Salary", name: "工资", dataColumns: [
      "Sno",
      "Slevel",
      "Snumber"
    ], table: "`cs2305.Salary`", pk: "Sno", dateCol: null
  },
  {
    id: 6, url: "/GoDown_Entry", name: "入库主单", dataColumns: [
      "GMno",
      "GMdate",
      "GMname"
    ], table: "`cs2305.godown_entry`", pk: "GMno", dateCol: null
  },
  {
    id: 7, url: "/GoDown_Slave", name: "入库从单", dataColumns: [
      "GSno",
      "GMno",
      "Mno",
      "GSnumber",
      "GSunit",
      "GSbatch",
      "GSprice",
      "GSexpdate"
    ], table: "`cs2305.godown_slave`", pk: "GSno", dateCol: null
  },
  {
    id: 8, url: "/Medicine", name: "药品", dataColumns: [
      "Mno",
      "Mname",
      "Munit",
      "Mprice",
      "Mexpdate"
    ], table: "`cs2305.medicine`", pk: "Mno", dateCol: null
  },
  {
    id: 9, url: "/Diagnosis", name: "就诊",dataColumns: [
      "DGno",
      "Pno",
      "Dno",
      "Symptom",
      "Diagnosis",
      "DGtime",
      "Rfee"
    ], table: "`cs2305.diagnosis`", pk: "DGno", dateCol: null
  },
  { id: 10, url: "/Recipe_Master", name: "处方主单" },
]
</script>

<style>
#app {
  position: absolute;
  height: 98%;
  width: 98%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.el-table--scrollable-x .el-table__body-wrapper {
  overflow-x: hidden;
}</style>
