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
    <el-table :data="doctor" @row-click="handleRowClick">
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
const doctor=ref([])
const dialogFormVisible = ref(false)
const formData = ref({})
onMounted(async () => {
  const response = await DataService.getAllDoctorData()
  doctor.value = response.data
  let col = []
  for (let key in doctor.value[0]) {
    col.push({ prop: key, label: key })
  }
  columns.value = col
});
const handleRowClick=(row)=>{
  formData.value = { ...row };
  dialogFormVisible.value = true
}
</script>
<style scoped>
.el-button--text {
  margin-right: 15px;
}
.el-select {
  width: 300px;
}
.el-input {
  width: 300px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>