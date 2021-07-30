<template>
  <div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,2,255', count: 250}" :el="'#area9'">
      </vue-canvas-nest>
      <div id="area9" class="background"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'238,99,99', count: 250}" :el="'#area10'">
      </vue-canvas-nest>
      <div id="area10" class="background"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,0,0', count: 250}" :el="'#area'">
      </vue-canvas-nest>
      <div id="area" class="background"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'106,90,205', count: 250}" :el="'#area2'">
      </vue-canvas-nest>
      <div id="area2" class="background"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'10,255,0', count: 250}" :el="'#area3'">
      </vue-canvas-nest>
      <div id="area3" class="background4"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,255,0', count: 250}" :el="'#area5'">
      </vue-canvas-nest>
      <div id="area5" class="background6"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,2,255', count: 250}" :el="'#area4'">
      </vue-canvas-nest>
      <div id="area4" class="background4"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'238,99,99', count: 250}" :el="'#area6'">
      </vue-canvas-nest>
      <div id="area6" class="background6"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,2,255', count: 250}" :el="'#area11'">
      </vue-canvas-nest>
      <div id="area11" class="background4"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'238,99,99', count: 250}" :el="'#area12'">
      </vue-canvas-nest>
      <div id="area12" class="background6"></div>
    </div>
<!--    <particles-bg type="lines" :bg="true" />-->
<!--    <img src="../../assets/bg1.jpeg" class="background_img">-->
    <el-form ref="loginForm" :model="form" :rules="rules" label-width="90px" class="login-box">
      <h3 class="login-title">Welcome</h3>
      <el-form-item label="Account" prop="username" class="font_style">
        <el-input type="text" placeholder="请输入账号" v-model="form.username" style="z-index: 200"/>
      </el-form-item>
      <el-form-item label="Password" prop="password" class="font_style">
        <el-input type="password" placeholder="请输入密码" v-model="form.password" style="z-index: 200"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-on:click="onSubmit('loginForm')" v-loading.fullscreen.lock="fullscreenLoading" style="z-index: 300;margin-left: 33px;width:100px;height: 40px;">Log In</el-button>
      </el-form-item>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%"
    >
      <span>Please enter right user id and password</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
// import { ParticlesBg } from 'particles-bg-vue'
import vueCanvasNest from 'vue-canvas-nest'
export default {
  name: 'Content',
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      // 表单验证，需要在 el-form-item 元素中增加 prop 属性
      rules: {
        username: [
          {required: true, message: '账号不可为空', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不可为空', trigger: 'blur'}
        ]
      },

      // 对话框显示和隐藏
      dialogVisible: false,
      fullscreenLoading: false
    }
  },
  components: {
    vueCanvasNest
  },
  methods: {
    onSubmit (formName) {
      this.fullscreenLoading = true
      this.$axios.get('http://127.0.0.1:5000/dmLogIn/' + this.form.username + '/' + this.form.password).then(res => {
        if (res['data'] === 1) {
          this.$message({
            message: 'Successfully!',
            type: 'success'
          })
          this.fullscreenLoading = false
          console.log(this.$route.path + '/developMode')
          this.$router.push({
            path: this.$route.path + '/developMode',
            query: {
              user_name: this.form.username
            }
          })
        } else {
          this.$message.error('Failed!')
          this.fullscreenLoading = false
          this.dialogVisible = true
        }
      })
      // // 为表单绑定验证功能
      // this.$refs[formName].validate((valid) => {
      //   if (valid) {
      //     // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
      //     this.$router.push('/main/' + this.form.username)
      //   } else {
      //     this.dialogVisible = true
      //     return false
      //   }
      // })
    }
  }
}
</script>

<style>
.background_img {

  width: 1200px;
  height: 800px;
}

.login-box {
  border: 1px solid #DCDFE6;
  width: 350px;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
  background-color: rgba(225, 221, 204, 0.86);
}
.font_style{
  font-weight: bold;
}

.login-title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #303133;
}
.background {
  position: absolute;
  left: 10px;
  top: 100px;
  width: 850px;
  height: 900px;
  z-index: 10;

}
.background2 {
  position: absolute;
  left: 310px;
  top: 100px;
  width: 700px;
  height: 900px;
  z-index: 10;
}
.background3 {
  position: absolute;
  left: 610px;
  top: 100px;
  width: 700px;
  height: 900px;
  z-index: 10;
}
.background4 {
  position: absolute;
  left: 980px;
  top: 100px;
  width: 700px;
  height: 900px;
  z-index: 10;
}
.background5 {
  position: absolute;
  left: 1250px;
  top: 100px;
  width: 700px;
  height: 900px;
  z-index: 10;
}
.background6 {
  position: absolute;
  left: 1510px;
  top: 100px;
  width: 700px;
  height: 900px;
  z-index: 10;
}
</style>
