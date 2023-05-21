<template>
 
  <el-container>
    <el-aside style="width: fit-content">
      <el-menu
      style="width: fit-content"
        class="el-menu-demo flex"
        router
        :unique-opened="true"
        :default-active="$route.path"
      >
        <el-menu-item index="/">
          <el-icon>
            <HomeFilled />
          </el-icon>
          首页
        </el-menu-item>
        <el-sub-menu index=1>
          <template #title><el-icon><Filter /></el-icon>原始数据</template>   
          <el-menu-item
          v-for="(item,id) in items"
          :key="id"
          :index="`1+${id}`"
          :route="{ name:'data', query: { item:JSON.stringify({dataColumns:item.dataColumns,table:item.table,pk:item.pk,dateCol:item.dateCol,datetimeCol:item.datetimeCol}) } }"
          >
          <el-icon><Document /></el-icon>{{item.name}}
          </el-menu-item> 
        </el-sub-menu>
        <el-sub-menu index=2>
          <template #title><el-icon><Filter /></el-icon>视图</template>   
          <el-menu-item
          v-for="(item,id) in viewItems"
          :key="id"
          :index="`20+${id}`"
          :route="{ name:'view', query: { item:JSON.stringify({dataColumns:item.dataColumns,view:item.view,dateCol:item.dateCol,datetimeCol:item.datetimeCol}) } }"
          >
          <el-icon><Document /></el-icon>{{item.name}}
          </el-menu-item> 
        </el-sub-menu>
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
const viewItems=ref(useStore().state.rawViewParanms)
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
