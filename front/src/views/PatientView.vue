<template>
  <el-dialog v-model="dialogFormVisible" title="编辑" draggable>
    <el-form :model="formData" >
      <el-form-item v-for="(value, key) in formData" :key="key" :label="columns.get(key)">
        <el-input v-model="formData[key]"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="update">
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
      :data="tableData" @row-click="handleRowClick"
    >
      <el-table-column type="index"></el-table-column>
      <el-table-column>
        <el-input :placeholder=data>
          
        </el-input>
      </el-table-column>
      <el-table-column prop="Pname" :label="columns.get(`Pname`)"></el-table-column>
      <el-table-column prop="Pid" :label="columns.get(`Pid`)"></el-table-column>
      <el-table-column prop="Pino" :label="columns.get(`Pino`)"></el-table-column>
      <el-table-column prop="Pmno" :label="columns.get(`Pmno`)"></el-table-column>
      <el-table-column prop="Psex" :label="columns.get(`Psex`)"></el-table-column>
      <el-table-column prop="Pbd" :label="columns.get(`Pbd`)"></el-table-column>
      <el-table-column prop="Padd" :label="columns.get(`Padd`)"></el-table-column>
    </el-table>
  </el-main>
</template>

<script setup>
import DataService from "@/components/services/DataService.js"
import { ref,onMounted } from "vue"
const tableData=ref([])
const columns=new Map([
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
  ["手机","手机"]
])
const loadData=async () => {
  const response  =await DataService.getAllPatientData()
  tableData.value=response.data
}
onMounted(loadData);
const dialogFormVisible = ref(false)
const formData = ref({})
const handleRowClick=(row)=>{
  console.log(row)
  formData.value = { ...row };
  dialogFormVisible.value = true
}
const update=()=>{
  console.log(formData)
  loadData()
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