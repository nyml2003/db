<template>
  <el-container>
  <el-aside style="width: fit-content">
  <el-menu :router="true" class="el-menu-vertical-demo" default-active="2">
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
    
 </el-menu>
</el-aside>
<el-main>
  <router-view/>
</el-main>
  
</el-container>
</template>

<script setup>
</script>

<style>
#app{
  position : absolute;
  height: 98%;
  width: 98%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.el-table--scrollable-x .el-table__body-wrapper {
  overflow-x: hidden;
}
</style>
