<template>
    <el-main>
      <el-table :data="doctor">
        <el-table-column type="index"></el-table-column>
    <el-table-column
    v-for="col in columns"
    :key="col.prop"
    :prop="col.prop"
    :label="col.label"
    />
    <template scoped="scoped">
      <el-button @click="editForm(scoped.row)">编辑</el-button>
    </template>
    </el-table>
    </el-main>
</template>

<script setup>
import DataService from "@/components/services/DataService.js"
import UpdateData from "@/components/UpdateData.vue"
import { ref,onMounted } from "vue"
const columns = ref([])
const doctor=ref([])
onMounted(async () => {
  const response = await DataService.getAllDoctorData()
  doctor.value = response.data
  let col = []
  for (let key in doctor.value[0]) {
    col.push({ prop: key, label: key })
  }
  columns.value = col
});

</script>
