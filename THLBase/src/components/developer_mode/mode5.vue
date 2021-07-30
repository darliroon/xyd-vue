<template>
  <div class="excel">
    <h3 style="position: absolute;left:800px;top:70px;">Upload Fingerprint Resource</h3>
    <el-upload
      class="upload-demo"
      action=""
      :on-change="handleChange"
      :show-file-list="false"
      :auto-upload="false">
      <el-button size="small" type="primary" style="margin-bottom:15px;" class="upload_button_style">Read Excel</el-button>
    </el-upload>
    <el-button size="small" type="primary" class="confirm_button_style" @click="upload_all_info" v-loading.fullscreen.lock="fullscreenLoading">Upload</el-button>
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
      <el-table-column prop="psx" label="psx" width="50"></el-table-column>
      <el-table-column prop="psy" label="psy" width="50"></el-table-column>
      <el-table-column prop="psz" label="psz" width="50"></el-table-column>
      <el-table-column prop="id1" label="id1" width="150"></el-table-column>
      <el-table-column prop="ap1" label="ap1" width="60"></el-table-column>
      <el-table-column prop="id2" label="id2" width="150"></el-table-column>
      <el-table-column prop="ap2" label="ap2" width="60"></el-table-column>
      <el-table-column prop="id3" label="id3" width="150"></el-table-column>
      <el-table-column prop="ap3" label="ap3" width="60"></el-table-column>
      <el-table-column prop="id4" label="id4" width="150"></el-table-column>
      <el-table-column prop="ap4" label="ap4" width="60"></el-table-column>
      <el-table-column prop="id5" label="id5" width="150"></el-table-column>
      <el-table-column prop="ap5" label="ap5" width="60"></el-table-column>
      <el-table-column prop="id6" label="id6" width="150"></el-table-column>
      <el-table-column prop="ap6" label="ap6" width="60"></el-table-column>
      <el-table-column prop="id7" label="id7" width="150"></el-table-column>
      <el-table-column prop="ap7" label="ap7" width="60"></el-table-column>
      <el-table-column prop="id8" label="id8" width="150"></el-table-column>
      <el-table-column prop="ap8" label="ap8" width="60"></el-table-column>
      <el-table-column prop="id9" label="id9" width="150"></el-table-column>
      <el-table-column prop="ap9" label="ap9" width="60"></el-table-column>
      <el-table-column prop="id10" label="id10" width="150"></el-table-column>
      <el-table-column prop="ap10" label="ap10" width="60"></el-table-column>
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
      active: 5,
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
          obj.psx = v.psx
          obj.psy = v.psy
          obj.psz = v.psz
          obj.id1 = v.id1
          obj.ap1 = v.ap1
          obj.id2 = v.id2
          obj.ap2 = v.ap2
          obj.id3 = v.id3
          obj.ap3 = v.ap3
          obj.id4 = v.id4
          obj.ap4 = v.ap4
          obj.id5 = v.id5
          obj.ap5 = v.ap5
          obj.id6 = v.id6
          obj.ap6 = v.ap6
          obj.id7 = v.id7
          obj.ap7 = v.ap7
          obj.id8 = v.id8
          obj.ap8 = v.ap8
          obj.id9 = v.id9
          obj.ap9 = v.ap9
          obj.id10 = v.id10
          obj.ap10 = v.ap10
          arr.push(obj)
        })
        _this.tableData = _this.tableData.concat(arr)
        console.log(_this.tableData)
        console.log(typeof _this.tableData[0])
        console.log(typeof _this.tableData[0].psx)
        console.log(typeof _this.tableData[0].id1)
        console.log(typeof _this.tableData[0].ap1)
        console.log(JSON.stringify(_this.tableData))
        console.log(typeof JSON.stringify(_this.tableData))
        // 这里我们需要把这个对象数组传给服务器
      }
    },
    upload_all_info () {
      console.log(this.tableData)
      this.fullscreenLoading = true
      let url = 'http://127.0.0.1:5000/insertManyFingers/' + this.$route.query.total_name
      this.$axios.post(url, this.tableData).then(res => {
        if (res['data'] === 0) {
          this.$message({
            message: 'Successfully!',
            type: 'success'
          })
          this.fullscreenLoading = false
          this.$router.push({
            path: this.$route.path + '/mode6',
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
        path: this.$route.path + '/mode6',
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
  left: 1000px;
  top: 500px;
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
