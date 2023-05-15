<template>
  <el-main>
    <el-table :data="patient">
      <el-table-column type="index"></el-table-column>
  <el-table-column
  v-for="col in columns"
  :key="col.prop"
  :prop="col.prop"
  :label="col.label"
  />
  </el-table>
  </el-main>
</template>

<script setup>
import DataService from "@/components/services/DataService.js"
import { ref,onMounted } from "vue"
const columns = ref([])
const patient=ref([])
onMounted(async () => {
const response  =await DataService.getAllDeptData()
patient.value=response.data
let col=[]
for (let key in patient.value[0]) {
col.push({ prop: key, label: key })
}
columns.value=col
});
</script>
