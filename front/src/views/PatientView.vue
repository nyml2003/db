<template>
  <el-main>
    <el-table 
      :data="patient"
    >
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
import { toggleRowStatus } from "element-plus/es/components/table/src/util";
import { ref,onMounted } from "vue"
const columns = ref([])
const patient=ref([])
onMounted(async () => {
  const response  =await DataService.getAllPatientData()
  patient.value=response.data
  let col=[]
  for (let key in patient.value[0]) {
  col.push({ prop: key, label: key })
}
  columns.value=col
});
</script>

<style>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>