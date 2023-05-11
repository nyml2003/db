<template>
  <el-table :data="patient">
    <el-table-column
    v-for="col in columns"
    :key="col.prop"
    :prop="col.prop"
    :label="col.label"
    :width="col.width"
    />
    </el-table>
</template>

<script setup>
import DataService from "@/components/services/DataService.js";
import { ref,onMounted } from "vue";
const columns = [
	{ prop: 'Pno', label: '患者编号', width: 200 },
	{ prop: 'Pname', label: '患者姓名', width: 200 },
	{ prop: 'Pid', label: '身份证号', width: 200 },
	{ prop: 'Pino', label: '社会保险号', width: 200 },
  { prop: 'Pmno', label: '医疗卡识别号', width: 200 },
  { prop: 'Psex', label: '性别', width: 200 },
  { prop: 'Pbd', label: '出生日期', width: 200 },
  { prop: 'Padd', label: '地址', width: 200 }
]
const patient=ref([]);
onMounted(async () => {
  const response  =await DataService.getAllPatientData();
  patient.value=response.data;
});
</script>
