<template>
 
  <el-container>
    <el-aside style="width: fit-content">
      <el-menu
      style="width: fit-content"
        class="el-menu-demo flex"
        router
        :default-active="$route.path"
      >
        <el-menu-item index="/">
          <el-icon>
            <HomeFilled />
          </el-icon>
          首页
        </el-menu-item>     
        <el-menu-item
          v-for="(item,id) in items"
          :key="id"
          :index="`1:${id}`"
          :route="{ name:'data', query: { item:JSON.stringify({dataColumns:item.dataColumns,table:item.table,pk:item.pk,dateCol:item.dateCol,datetimeCol:item.datetimeCol}) } }"
        >
          <el-icon><HomeFilled /></el-icon>{{item.name}}
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
     
      <router-view :key=$route.fullPath></router-view>
    </el-main>
  </el-container>
</template>

<script setup>
import {useStore} from 'vuex'
import { ref } from 'vue';
const items=ref(useStore().state.rawTableParanms)
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
