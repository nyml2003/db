<template>
    <el-row 
         class="info">
        <p>{{ name }}</p>
    <div class="button-wrapper">
        <el-button type="primary" circle @click="updateInfoDialog"><el-icon><Edit /></el-icon></el-button>
        <el-button type="primary" circle @click="isExit = true"><el-icon><Close /></el-icon></el-button>
    </div>
    </el-row>
    <!--基本信息显示区-->
    <div class="info2">
        <el-row class="info3"><el-icon size="25" style="margin-right: 15px;"><PriceTag /></el-icon>{{ uid }}</el-row>
        <el-row class="info3"><el-icon size="25" style="margin-right: 15px;"><PriceTag /></el-icon>{{ role }}</el-row>
        <div v-if="role!='admin'">
            <el-row class="info3"><el-icon size="25" style="margin-right: 15px;"><PriceTag /></el-icon>{{sex}}</el-row>
        </div>
    </div>
  <!-- 退出登录 -->
  <el-dialog v-model="isExit" title="您是否要退出登录？" width="500px">
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="isExit = false">取消</el-button>
        <el-button type="primary" @click="logout">
          退出
        </el-button>
      </span>
    </template>
  </el-dialog>

  <el-dialog v-model="dialogVisible" title="修改信息" width="500px">
    <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><Camera/> </el-icon></p></el-col>
        <el-col :span="15"><el-input v-model="initData.avatar" size="small"></el-input></el-col>
    </el-row>
    <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><PriceTag /></el-icon></p></el-col>
        <el-col :span="15"><el-input disabled v-model="id" size="small"></el-input></el-col>
    </el-row>
        <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><User /></el-icon></p></el-col>
        <el-col :span="15"><el-input v-model="initData.username" size="small"></el-input></el-col>
    </el-row>
    <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><Message /></el-icon></p></el-col>
        <el-col :span="15"><el-input v-model="initData.email" size="small"></el-input></el-col>
    </el-row>
    <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><Iphone /></el-icon></p></el-col>
        <el-col :span="15"><el-input v-model="initData.phone_number" size="small"></el-input></el-col>
    </el-row>
    <el-row class="row">
        <el-col :span="5"><p style="font-size: 16px;"><el-icon size="20"><Timer /></el-icon></p></el-col>
        <el-col :span="15"><el-input disabled v-model="time" size="small"></el-input></el-col>
    </el-row>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="updateInfo">
          提交
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import {useStore} from 'vuex'
import { useRouter } from 'vue-router'
import DataService from '@/components/services/DataService'
const store=useStore()
const router = useRouter()
const isExit = ref(false)
const logout=()=>{
    isExit.value = false
    store.commit("logout")
    ElMessage.success('退出成功！')
    router.push({path:'/login'})
}
console.log(store.state.user)
console.log('before uid')
const uid = ref(store.state.user.uid)
const username = ref('')
const role=ref('')
const sex=ref('')
const name=ref('')

const getPersonalInfo = async () => {
    if (store.state.isLogin === false) {
        ElMessage.error('您还没有登录，请先登录！');
        router.push({path:'/login'})
        return;
    }
    else {
        console.log(uid.value)
        const responce = await DataService.select_profile(uid.value)
        console.log(responce.data)
        username.value = responce.data.username
        role.value=responce.data.role
        if (role.value==='医生'){
            if (responce.data.Dname) name.value=responce.data.Dname
            if (responce.data.Dsex) sex.value=responce.data.Dsex
        }
        else if (role.value==='患者'){
            if (responce.data.Pname) name.value=responce.data.Pname
            if (responce.data.Psex )sex.value=responce.data.Psex
        }

    }
};

onMounted(getPersonalInfo)
const updateInfoDialog=()=>{
    
}
</script>

<style scoped>
.row {
    margin-bottom: 15px;
    font-size: 16px;
    margin-left: 80px;
}
.detail {
    background-image: linear-gradient(to right, #5d9cec, #8eb5f3);
    border-radius: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.icon {
    margin-right: 10px;
}
.button-wrapper {
  margin-left: auto;
}

.info2 {
    color:gray;
    margin-left: 70px;
    height: 60vh;
    font-size: 17px;
    font-weight: 340;
    display: flex; 
    align-items: begin;
    justify-items: center;
    flex-direction: column;
}
.info3 {
    margin-bottom: 15px;
    padding-bottom: 15px;
    border-bottom: 2px solid #E6E6E6;
}

.show_detail {
    margin-top: 15px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    padding-right: 50px;
    padding-left: 50px;
    border-right: 2px solid white;
}
.icon {
    color: white;
    border:none !important;
}
.text {
    color: white;
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    font-weight: 220;
    font-size: 16px;
}
.info {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    border-bottom: 3px solid #E6E6E6;
    padding-bottom: 10px;
    justify-content: space-between;
}
.info p {
    margin-left: 20px;
    font-size: 25px;
    font-weight: 190;
}

.detail p{
    margin-left: 68px;
    margin-bottom: 20px;
    font-weight: 190;
}

</style>