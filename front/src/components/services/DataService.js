// 导入 axios
import axios from 'axios';

// 创建一个 axios 实例，用于发送请求
const apiClient = axios.create({
  // 设置后端 API 的基础 URL
  baseURL: "http://localhost:8090/api",
  // 设置请求头
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// 定义一个用于获取数据的函数
export default {
  getAllPatientData() {
    return apiClient.post('/table',{table:"`cs2305.patient`"});
  },
  getAllDeptData() {
    return apiClient.post('/table',{table:"`cs2305.dept`"});
  },
  getAllDoctorData() {
    return apiClient.post('/table',{table:"`cs2305.doctor`"});
  },
  shutdown() {
    return apiClient.post('/shutdown',{"content":"shutdown"});
  },
  update(table,id,col,value){
    return apiClient.post('/update',{"table":table,"id":id,"col":col,"value":value})
  }
};
