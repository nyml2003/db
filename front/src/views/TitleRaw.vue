<template>
    <el-dialog v-model="dialogFormVisible" title="编辑" draggable style="max-width: fit-content;" label-position="right">
      <el-form>
        <el-form-item v-for="col in dataColumns" :key="col" :prop="col" :label="columns.get(col)"><el-input v-model="formData[col]" :disabled="!isAdd && disabledColumns.includes(col)"></el-input></el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          
          <div v-if="isAdd">
            <el-button @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="handleAdd">
              添加
            </el-button>
          </div>
          <div v-else>
            <el-button @click="dialogFormVisible = false">取消</el-button>
              <el-button type="primary" @click="update">
              修改
            </el-button>
            <el-button type="primary" @click="handleDelete">
              删除
            </el-button>
          </div>       
          
        </span>
      </template>
    </el-dialog>
    
    <el-main>
      <el-table 
        :data="tableData" @row-click="handleRowClick" border
      >
        <el-table-column type="index"></el-table-column>
        <el-table-column v-for="col in dataColumns" :key="col" :prop="col" :label="columns.get(col)"></el-table-column>
      </el-table>
    </el-main>
    <el-footer>
      <el-row style="{align-items: center;justify-content: center;  display: flex;}">
        <el-button type="primary" @click="loadData">刷新</el-button>
        <el-button type="primary" @click="handleAddButton">添加</el-button>
      </el-row>
    </el-footer>
  </template>
  
  <script setup>
  import DataService from "@/components/services/DataService.js"
  import { ref,onMounted } from "vue"
  import { useStore } from "vuex";
  const tableData=ref([])
  const columns=useStore().state.columns
  const dataColumns=[
    "Tno",
    "Sno",
    "Ttype",
    "Ttrade"
  ]
 
  const table="`cs2305.title`"
  const pk="Tno"
  const dateCol=null
  const disabledColumns=[
    pk
  ]
  const loadData=async () => {
    const response  =await DataService.getAllData(table)
    if (response.data.status) {
      console.log(response.data.status)
    }
    tableData.value=response.data.content
  }
  onMounted(loadData);
  const dialogFormVisible = ref(false)
  const formData = ref({})
  const isAdd= ref(false)
  let initFormData={}
  const handleRowClick=(row)=>{
    isAdd.value=false
    formData.value = { ...row };
    initFormData={ ...row };
    dialogFormVisible.value = true
  }
  const update=()=>{
    for (let key in formData.value) {
      if(formData.value[key]!=initFormData[key]){
        if (key===dateCol) {
          let d=new Date(formData.value[key])
          d=d - d.getTimezoneOffset()*60000
          formData.value[key]=new Date(d).toISOString().slice(0, 10)
        }
        DataService.update(table,formData.value[pk],key,formData.value[key],pk)
      }
    }
    loadData()
  }
  const handleDelete=()=>{
    DataService.delete(table,formData.value[pk],pk)
    dialogFormVisible.value=false
    loadData()
  }
  const handleAdd=()=>{
    let data=[]
    for (let key in formData.value) {
      if (key===dateCol) {
        let d=new Date(formData.value[key])
        d=d - d.getTimezoneOffset()*60000
        formData.value[key]=new Date(d).toISOString().slice(0, 10)
      }
      data.push(formData.value[key])
    }
    DataService.insert(table,data)
    dialogFormVisible.value=false
    loadData()
  }
  const handleAddButton=()=>{
    isAdd.value=true
    dialogFormVisible.value=true
    formData.value={}
  }
  </script>
  