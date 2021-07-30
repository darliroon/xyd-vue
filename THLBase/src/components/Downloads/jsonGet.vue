<template>
  <div>
    <!--    <el-dialog-->
    <!--      title="提示"-->
    <!--      :visible.sync="dialogVisible"-->
    <!--      width="30%">-->
    <!--      <span>Do you confrim to delete?</span>-->
    <!--      <span slot="footer" class="dialog-footer">-->
    <!--        <el-button @click="dialogCancel">Cancel</el-button>-->
    <!--        <el-button type="primary" @click="dialogConfirm">Confirm</el-button>-->
    <!--      </span>-->
    <!--    </el-dialog>-->
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu default-active="1-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">导航一</span>
        </template>
        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">My Resource</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>
    </el-menu>
    <el-table
      :data="tableData"
      style="width: 30%;position:absolute;left:250px;top:150px;"
      scripe
      border
      :cell-style="cs"
      max-height="800"
      :header-cell-style="hcs">>
      <el-table-column
        label="label"
        width="180"
        type="index"
        :index="indexMethod">
      </el-table-column>
      <el-table-column
        label="Source Name"
        width="180">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <!--            <p>姓名: {{ scope.row.name }}</p>-->
            <!--            <p>住址: {{ scope.row.address }}</p>-->
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.name }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="OP">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="handleEdit(scope.$index, scope.row)">Download</el-button>
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="danger"-->
<!--            @click="handleDelete(scope.$index, scope.row)">Del</el-button>-->
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [],
      isCollapse: true
    }
  },
  methods: {
    handleEdit (index, row) {
      this.$axios.get('http://127.0.0.1:5000/getDeveloperNewFingersForDeveloperJson/' + row.name).then(res => {
        console.log(res['data'])
      })
    },
    handleDelete (index, row) {
      // this.$confirm('This will delete the resource permanently! If Continue?', 'Warn', {
      //   confirmButtonText: 'Confirm',
      //   cancelButtonText: 'Cancel',
      //   type: 'warning'
      // }).then(res => {
      //   if (res === 'confirm') {
      //     console.log('This is confirm')
      //     this.$axios.get('http://127.0.0.1:5000/dropFingerTable/' + row.name).then(res => {
      //       console.log('FingerDrop: ' + res['data'])
      //     })
      //     this.$axios.get('http://127.0.0.1:5000/dropObjectTable/' + row.name).then(res => {
      //       console.log('ObjectDrop' + res['data'])
      //     })
      //     this.$axios.get('http://127.0.0.1:5000/dropNavTable/' + row.name).then(res => {
      //       console.log('NavDrop' + res['data'])
      //     })
      //     this.$axios.get('http://127.0.0.1:5000/dropImgTable/' + row.name).then(res => {
      //       console.log('ImgDrop' + res['data'])
      //     })
      //     this.$axios.get('http://127.0.0.1:5000/dmRemoveHold/' + this.$route.query.user_name + '/' + row.name).then(res => {
      //       console.log('HoldDrop' + res['data'])
      //     })
      //     this.tableData.splice(index, 1)
      //     this.$message.info('Your data has been delete')
      //   }
      // }).catch(err => {
      //   console.log(err)
      //   console.log('this is cancel')
      // })
      // console.log(index, row)
      // console.log(row.name)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
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
  },
  created () {
    this.$axios.get('http://127.0.0.1:5000/getAHolds').then(res => {
      console.log(res['data'])
      let arr = res['data']
      for (let j = 0, len = arr.length; j < len; j++) {
        this.tableData.push({
          'name': arr[j][0]
        })
      }
      // console.log(res['data'].split(','))
      // let arr = res['data'].split(',')
      // for (let j = 0, len = arr.length; j < len; j++) {
      //   this.tableData.push({
      //     'name': arr[j]
      //   })
      // }
      // console.log(this.tableData)
    })
  }
}
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>
