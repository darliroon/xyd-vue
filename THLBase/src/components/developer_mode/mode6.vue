<template>
  <div class="excel">
<!--    <el-steps :active="active" finish-status="success" align-cente class="process_style" space="300">-->
<!--&lt;!&ndash;      <el-step title="Upload Map Resource" icon="el-icon-picture"></el-step>&ndash;&gt;-->
<!--&lt;!&ndash;      <el-step title="Upload Finger Resource" icon="el-icon-upload"></el-step>&ndash;&gt;-->
<!--      <el-step title="Upload Objects Resource" icon="el-icon-upload"></el-step>-->
<!--      <el-step title="Upload Navi Resource" icon="el-icon-upload"></el-step>-->
<!--      <el-step title="Successfully" icon="el-icon-upload"></el-step>-->
<!--&lt;!&ndash;      &lt;!&ndash;      <el-step title="步骤 10" icon="el-icon-edit" description="这是一段很长很长很长的描述性文字"></el-step>&ndash;&gt;&ndash;&gt;-->
<!--    </el-steps>-->
    <h3 style="position: absolute;left:840px;top:70px;">Upload Objects Resource</h3>
    <el-upload
      class="upload-demo"
      action=""
      :on-change="handleChange"
      :show-file-list="false"
      :auto-upload="false">
      <el-button size="small" type="primary" style="margin-bottom:15px;" class="upload_button_style">Read Excel</el-button>
    </el-upload>
    <el-button size="small" type="primary" class="confirm_button_style" @click="upload_all_info" v-loading.fullscreen.lock="fullscreenLoading">>Upload</el-button>
    <el-button size="small" type="primary" class="skip_button_style" @click="skip_act">Skip</el-button>
    <el-table
      :data="tableData"
      style="width: 100%"
      scripe
      border
      :cell-style="cs"
      max-height="800"
      :header-cell-style="hcs">
      <el-table-column
        type="index"
        :index="indexMethod">
      </el-table-column>
      <el-table-column prop="name" label="name" width="150"></el-table-column>
      <el-table-column prop="coordinatex" label="coordinatex" width="110"></el-table-column>
      <el-table-column prop="coordinatey" label="coordinatey" width="110"></el-table-column>
      <el-table-column prop="coordinatez" label="coordinatez" width="110"></el-table-column>
      <el-table-column prop="label" label="label" width="110"></el-table-column>
      <el-table-column prop="img_url" label="img_url" width="380"></el-table-column>
      <el-table-column prop="details" label="details" width="350"></el-table-column>
      <el-table-column prop="comments" label="comments" width="350"></el-table-column>
      <el-table-column label="OP">
        <template slot-scope="scope">
          <a @click="handleDelete(scope)">删除</a> |
          <a @click="handelEdit(scope)">修改</a>
        </template>
      </el-table-column>
    </el-table>
  </div>
  <!--
  注意：上面代码有以下 2 个需要注意的点
    1. action 属性必须要有，可以为空，但是不能没有，不然控制台会报错
    2. 钩子函数必须是 on-change 这个钩子，只有这个钩子可以添加文件，其他都是上传，具体可以看[elementtui官方文档的介绍](https://element.eleme.io/#/zh-CN/component/upload)
  -->
</template>

<script>
export default {
  data () {
    return {
      tableData: [],
      fileContent: '',
      file: '',
      data: '',
      active: 0,
      fullscreenLoading: false
    }
  },
  methods: {
    // 注意：handleDelete 和 handelEdit 这两个方法其实是无关紧要的，只不过我的处理逻辑中有 修改 和 删除 这两个功能，不写的话，会报错
    handleDelete (item) {
      console.log('handleDelete', item)
    },
    handelEdit (item) {
      console.log('handleDelete', item)
    },
    // 核心部分代码(handleChange 和 importfile)
    handleChange (file, fileList) {
      this.fileContent = file.raw
      const fileName = file.name
      const fileType = fileName.substring(fileName.lastIndexOf('.') + 1)
      if (this.fileContent) {
        if (fileType === 'xlsx' || fileType === 'xls') {
          this.importfile(this.fileContent)
        } else {
          this.$message({
            type: 'warning',
            message: '附件格式错误，请重新上传！'
          })
        }
      } else {
        this.$message({
          type: 'warning',
          message: '请上传附件！'
        })
      }
    },
    importfile (obj) {
      const reader = new FileReader()
      const _this = this
      reader.readAsArrayBuffer(obj)
      reader.onload = function () {
        const buffer = reader.result
        const bytes = new Uint8Array(buffer)
        const length = bytes.byteLength
        let binary = ''
        for (let i = 0; i < length; i++) {
          binary += String.fromCharCode(bytes[i])
        }
        const XLSX = require('xlsx')
        const wb = XLSX.read(binary, {
          type: 'binary'
        })
        const outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
        this.data = [...outdata]
        const arr = []
        this.data.map(v => {
          const obj = {}
          obj.name = v.name
          obj.coordinatex = v.coordinatex.toString()
          obj.coordinatey = v.coordinatey.toString()
          obj.coordinatez = v.coordinatez.toString()
          // obj.coordinate = v.coordinatex.toString() + v.coordinatey.toString() + v.coordinatez.toString()
          obj.label = v.label
          obj.img_url = v.img_url
          obj.details = v.details
          obj.comments = v.comments
          arr.push(obj)
        })
        _this.tableData = _this.tableData.concat(arr)
        // 这里我们需要把这个对象数组传给服务器
      }
    },
    upload_all_info () {
      console.log(this.tableData)
      this.fullscreenLoading = true
      let url = 'http://127.0.0.1:5000/insertManyObjects/' + this.$route.query.total_name
      this.$axios.post(url, this.tableData).then(res => {
        if (res['data'] === 0) {
          this.$message({
            message: 'Successfully!',
            type: 'success'
          })
          this.fullscreenLoading = false
          this.$router.push({
            path: this.$route.path + '/mode7',
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
    skip_act () {
      this.$router.push({
        path: this.$route.path + '/mode7',
        query: {
          total_name: this.$route.query.total_name,
          user_name: this.$route.query.user_name
        }
      })
    },
    hcs () {
      return 'text-align: center;background:rgb(242,242,242);color:rgb(140,138,140)'
    },
    cs () {
      return 'text-align:center'
    },
    indexMethod (index) {
      return index + 1
    }
  }
}
</script>

<style>
.process_style{
  position:absolute;
  left: 700px;
  top: 50px;
}
.confirm_button_style{
  position:absolute;
  left:150px;
  top: 88px;
  width: 100px;
}
.upload_button_style{
  width: 100px;
}
.skip_button_style{
  position:absolute;
  left:260px;
  top: 88px;
  width: 100px;
}
</style>
