<template>
  <el-menu :router="true" mode="horizontal">
    <el-menu-item index="/">
      <el-icon><UserFilled /></el-icon>
      首页
    </el-menu-item>
    <el-menu-item index="/patient">
      <el-icon><UserFilled /></el-icon>
      患者管理
    </el-menu-item>
    <el-menu-item index="/dept">
      <el-icon><UserFilled /></el-icon>
      部门管理
    </el-menu-item>
  </el-menu>
  <router-view/>
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
