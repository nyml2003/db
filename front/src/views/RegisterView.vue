<template>
  <el-row style="align-items: center; justify-content: center; height:100% width:100%">
    <el-form
      ref="form"
      :model="{username,password,confirmpassword}"
      :rules="rules"
      status-icon
      label-position="top"
      label-width="100px"
      max-width="800px"
    >
      <h2 class="register_title">欢迎使用CS2305.HIS管理系统</h2>
      <el-form-item label="用户名" prop="username">
        <el-input v-model="username" placeholder="用户名长度为1-10，由数字、字母、汉字组成"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="password" placeholder="密码长度为1-15，由数字、字母组成"></el-input>
      </el-form-item>
      <el-form-item label="身份" prop="role">
        <el-radio-group v-model="role">
          <el-radio label="patient">患者</el-radio>
          <el-radio label="doctor">医生</el-radio>
          <el-radio label="admin">管理员</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="确认密码" prop="confirmpassword">
        <el-input v-model="confirmpassword" placeholder="请确认您的密码"></el-input>
      </el-form-item>
      <el-form-item >
        <el-col :span="24" style="text-align: center;">
          <el-button round plain type="info" size="large" @click="submit(form)" >注册</el-button>
        </el-col>
      </el-form-item>
    </el-form>
  </el-row>
</template>

<script setup>
import { ref } from 'vue'
import DataService from '@/components/services/DataService'
import { useStore} from 'vuex'
import router from '@/router';
const form=ref(null)
const role=ref('patient')
const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' },
    { pattern: /^[a-zA-Z0-9\u4e00-\u9fa5]+$/, message: '用户名只能包含数字、字母、汉字', trigger: 'blur' }
  ],

  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 1, max: 15, message: '长度在 1 到 15 个字符', trigger: 'blur' },
    { pattern:/^[a-zA-Z0-9]+$/, message:'密码只能包含数字、字母', trigger:'blur'}
  ],
  confirmpassword:[
    { required:true, message:'请再次输入密码', trigger:'blur'},
    { validator:(rule,value,callback)=>{
      if(value!==password.value){
        callback(new Error('两次输入的密码不一致'))
      }else{
        callback()
      }
    },trigger:'blur'}
  ]
}
const store=useStore()
const password=ref('')
const username=ref('')
const confirmpassword=ref('')
const postData=async()=>{
  const response=await DataService.register(username.value,password.value,role.value)
  console.log(response.data)
  store.commit("setUser",response.data.user)
  router.push({path:'/MyPage'})
}
const submit=(() => {
  console.log("click")
  console.log(form.value)
  if (form.value===null) return
  form.value.validate((valid) => {
    if (valid) {
      postData()
      console.log('submit!')
    } else {
      console.log('error submit!!')
      return false
    }
  })
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
form {
    background-color: #fff;
    padding: 20px;
    margin: 50px;
    border-radius: 10px;
    width: 500px;
    border: 2px solid rgb(193, 186, 186);
}
.register_title {
  font-size: 25px;
  color: rgb(73, 73, 73);
  font-family:  'San Francisco';
  font-weight: 450;
  text-align: center;
  margin-bottom: 15px;
}
.register {
    margin-top: 8vh;
    margin-bottom: 8vh;
    display: flex;
    align-items: center;
    justify-content: center;
    
}
.register input[type=text], input[type=password] {
    padding: 10px;
    margin: 5px 0;
    border: none;
    border-radius: 5px;
    background-color: white;
    border:rgb(214, 214, 214) solid;
    font-size: 16px;
    width: 100%;
}

input[type="submit"] {
    margin-top: 10px;
    margin-bottom: 20px;
    color: rgb(150, 150, 150);
    background-color: white;
    border-radius: 25px / 25px; /* 将按钮变为圆形 */
    width: 60px; /* 设置按钮宽度和高度相等 */
    height: 40px;
    font-size: 12px; /* 设置字体大小 */
    border: 1.5px solid rgb(190, 190, 190);
    transition: background-color 0.2s ease-in-out;
  }

  input[type="submit"]:hover{
    background-color: rgb(190, 190, 190);
    color: white;
  }

::placeholder {
    font-family:  'San Francisco';
    color: #999;
  }
.login_register{
    font-family:  'San Francisco';
    font-size: 10px;
    color: rgb(150, 150, 150);
    text-align: center;
}


</style>