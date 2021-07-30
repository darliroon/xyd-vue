<template>
  <div>
    <el-steps :active="active" finish-status="success" align-center>
      <el-step title="Create Finger Resource" icon="el-icon-edit" description="create an empty finger points resource container" ></el-step>
      <el-step title="Create Objects Resource" icon="el-icon-edit" description="create an empty main objects resource container"></el-step>
      <el-step title="Create Navi Resource" icon="el-icon-edit" description="create an empty navigation resource container"></el-step>
      <el-step title="Create Map Resource" icon="el-icon-edit" description="create an empty map resource container"></el-step>
      <el-step title="Upload Map Resource" icon="el-icon-picture" description="select an image to upload the map resource"></el-step>
      <el-step title="Upload Finger Resource" icon="el-icon-upload" description="select an excel file to upload the finger points resource"></el-step>
      <el-step title="Upload Objects Resource" icon="el-icon-upload" description="select an excel file to upload the main objects resource"></el-step>
      <el-step title="Upload Navi Resource" icon="el-icon-upload" description="select an excel file to upload the navigation resource"></el-step>
      <el-step title="Successfully" icon="el-icon-upload" description="confirm creation and successfully build new resource"></el-step>
<!--      <el-step title="步骤 10" icon="el-icon-edit" description="这是一段很长很长很长的描述性文字"></el-step>-->
    </el-steps>
    <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
      <h3 class="login-title">New Fingerprint</h3>
      <el-form-item label="Container" prop="tableName" class="font_style">
        <el-input class="input_width" type="text" placeholder="Please enter lowercase letters" v-model="form.tableName"/>
      </el-form-item>
      <el-form-item label="ARGS" prop="all_args" class="font_style">
        <el-input class="input_width" type="text" placeholder="(name text, id int, id2 varchar(255))" v-model="form.all_args"/>
      </el-form-item>
      <el-row :gutter="180">
        <el-col :span="6">
          <el-form-item>
            <el-button type="primary" v-on:click="onSubmit('loginForm')" v-loading.fullscreen.lock="fullscreenLoading" style="margin-left: 20px;">Confirm</el-button>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item>
            <el-button type="primary" v-on:click="onSubmit('loginForm')">Return</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%"
    >
      <span>The table name has already exist!</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible2"
      width="30%"
    >
      <span>The table name has already exist!</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible2 = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'mode_two',
  data () {
    return {
      form: {
        tableName: '',
        all_args: 'psx int, psy int, psz int, id1 text, ap1 int, id2 text, ap2 int, id3 text, ap3 int, id4 text,' +
          ' ap4 int, id5 text, ap5 int, id6 text, ap6 int, id7 text, ap7 int, id8 text, ap8 int, id9 text, ap9 int, id10 text, ap10 int'
      },

      // 表单验证，需要在 el-form-item 元素中增加 prop 属性
      rules: {
        tableName: [
          {required: true, message: '数据不可为空', trigger: 'blur'}
        ],
        all_args: [
          {required: true, message: '数据不可为空', trigger: 'blur'}
        ]
      },
      // 对话框显示和隐藏
      dialogVisible: false,
      dialogVisible2: false,
      active: 0,
      fullscreenLoading: false
    }
  },
  methods: {
    onSubmit (formName) {
      this.form.all_args = 'psx int, psy int, psz int, id1 text, ap1 int, id2 text, ap2 int, id3 text, ap3 int, id4 text,' +
        ' ap4 int, id5 text, ap5 int, id6 text, ap6 int, id7 text, ap7 int, id8 text, ap8 int, id9 text, ap9 int, id10 text, ap10 int'
      console.log(this.form.tableName)
      console.log(this.form.all_args)
      console.log('CREATE TABLE ' + this.form.tableName + ' ' + '(' + this.form.all_args + ')')
      this.fullscreenLoading = true
      this.$axios({
        url: 'http://127.0.0.1:5000/newFingerTable',
        method: 'post',
        // 发送格式为json
        data: {name: this.form.tableName,
          sql: 'CREATE TABLE ' + this.form.tableName + ' ' + '(' + this.form.all_args + ')'}
        // headers: {
        //   'Content-Type': 'application/json'
        // }
      }).then(res => {
        if (res['data'] === 0) {
          this.$message({
            message: 'Successfully!',
            type: 'success'
          })
          this.fullscreenLoading = false
          this.$router.push({
            path: this.$route.path + '/mode2',
            query: {
              finger_name: this.form.tableName,
              user_name: this.$route.query.user_name
            }
          })
        } else {
          this.$message.error('Failed!')
          this.fullscreenLoading = false
        }
      }).catch(err => {
        this.$message.error('Error Occurred!')
        console.log('Error Occurred!')
        console.log(err)
        this.fullscreenLoading = false
      })
    }
  }
}
// this.$http.post('http://192.168.129.16:8080/newFingerTable',
//   {name: this.tableName, sql: 'CREATE TABLE ' + this.form.tableName + ' ' + '(' + this.form.all_args + ')'},
//   {emulateJSON: true}).then(res => {
//   if (res === '0') {
//     this.$router.push('/about')
//   } else if (res === '-1') {
//     this.dialogVisible = true
//   } else {
//     this.dialogVisible2 = true
//   }
// })
// this.$http.get('http://192.168.129.16:8080/dmLogIn/' + this.form.username + '/' + this.form.password).then(res => {
//   if (res['data'] === 1) {
//     console.log('Successfully')
//     console.log(this.$route.path + '/developMode')
//     this.$router.push(this.$route.path + '/developMode')
//   } else {
//     console.log('Failed')
//     this.dialogVisible = true
//   }
// })
</script>

<style>

.input_width {
  width: 350px;
  position: absolute;
  left: 10px;
}

.login-box {
  border: 1px solid #DCDFE6;
  width: 450px;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
}

.login-title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #303133;
}

.font_style{
  font-weight: bold;
}
</style>
