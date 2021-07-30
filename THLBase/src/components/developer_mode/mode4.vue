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
<!--    <img src="../../assets/map1.png" class="pic1_position">-->
<!--    <img src="../../assets/map3.png" class="pic2_position">-->
<!--    <img src="../../assets/index_img1.png" class="main_pic_position">-->
    <el-form :model="form" class="form_position">
      <el-form-item label="Your Map" :label-width="formLabelWidth">
        <el-upload
          ref="upload"
          action="#"
          accept="image/png,image/gif,image/jpg,image/jpeg"
          list-type="picture-card"
          :limit=limitNum
          :auto-upload="false"
          :http-request="httpRequest"
          :on-exceed="handleExceed"
          :before-upload="handleBeforeUpload"
          :on-preview="handlePictureCardPreview"
          :on-remove="handleRemove">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
      </el-form-item>
      <el-form-item>
        <el-button size="small" type="primary" @click="uploadFile" style="margin-left: 70px; margin-top: -20px"
                   v-loading.fullscreen.lock="fullscreenLoading">Upload</el-button>
        <el-button size="small" style="margin-left: 20px" @click="cancelClick">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      formLabelWidth: '80px',
      limitNum: 3,
      form: {},
      active: 4,
      fullscreenLoading: false
    }
  },
  methods: {
    // 上传文件之前的钩子
    handleBeforeUpload (file) {
      console.log('before')
      if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
        this.$notify.warning({
          title: '警告',
          message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
        })
      }
      let size = file.size / 1024 / 1024 / 2
      if (size > 2) {
        this.$notify.warning({
          title: '警告',
          message: '图片大小必须小于2M'
        })
      }
    },
    // 文件超出个数限制时的钩子
    handleExceed (files, fileList) {

    },
    // 文件列表移除文件时的钩子
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    // 点击文件列表中已上传的文件时的钩子
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    // param是自带参数。 this.$refs.upload.submit() 会自动调用 httpRequest方法.在里面取得file
    httpRequest (param) {
      console.log(param)
      let fileObj = param.file // 相当于input里取得的files
      let fd = new FormData()// FormData 对象
      fd.append('file', fileObj)// 文件对象
      // fd.append('platNum', this.importList.platNum)
      // fd.append('taskName', this.importList.taskName)
      let url = 'http://127.0.0.1:5000/imgToTable/' + this.$route.query.total_name
      // let url = process.env.CMS1_BASE_API + 'cdnDel/uploadExcel'
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      this.fullscreenLoading = true
      this.$axios.post(url, fd, config).then(res => {
        if (res['data'] === 0) {
          this.$message({
            message: 'Successfully!',
            type: 'success'
          })
          this.fullscreenLoading = false
          this.$router.push({
            path: this.$route.path + '/mode5',
            query: {
              total_name: this.$route.query.total_name,
              user_name: this.$route.query.user_name
            }
          })
        } else {
          this.$message.error('Failed!')
          this.fullscreenLoading = false
        }
      })
    },
    uploadFile () {
      this.$refs.upload.submit()
    },
    cancelClick () {
      this.$router.push({
        path: this.$route.path + '/mode5',
        query: {
          total_name: this.$route.query.total_name,
          user_name: this.$route.query.user_name
        }
      })
    }
  }
}
</script>

<style>
.form_position{
 position:absolute;
  left: 800px;
  top: 400px;
}
.main_pic_position{
  position:absolute;
  left: 760px;
}
.pic2_position{
  position:absolute;
  left: 950px;
  top: 300px;
}
.pic1_position{
  position:absolute;
  left: 200px;
}

</style>
