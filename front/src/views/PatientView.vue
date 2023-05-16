<template>
  <el-dialog v-model="dialogFormVisible" title="修改" draggable>
    <el-form :model="formData" >
      <el-form-item v-for="(value, key) in formData" :key="key" :label="key">
        <el-input v-model="formData[key]"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          修改
        </el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          删除
        </el-button>
      </span>
    </template>
  </el-dialog>
  <el-main>
    <el-table 
      :data="patient" @row-click="handleRowClick"
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
const dialogFormVisible = ref(false)
const formData = ref({})
const handleRowClick=(row)=>{
  formData.value = { ...row };
  dialogFormVisible.value = true
}
</script>

<style>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>