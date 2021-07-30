<template>
  <div>
    <el-button size="mini" type="primary" class="button_size">Return</el-button>
    <el-button size="mini" @click="handleAdd()" type="primary" class="button_size">Add</el-button>
    <el-table
      ref="mytable"
      :data="table_data"
      style="width: 100%"
      max-height="3000"
      @selection-change="handleSelectionChange"
      :row-class-name="tableRowClassName"
    >
      <el-table-column v-if="radio" type="index" width="50"></el-table-column>
      <el-table-column v-if="selection" type="selection" width="55"></el-table-column>
      <el-table-column
        align="center"
        v-for="(item,index,key) in table_columns"
        :item="item"
        :key="key"
        :index="index"
        :label="item.label"
      >
        <template slot-scope="scope">
          <el-input
            v-if=" scope.row.edit"
            size="small"
            v-model="scope.row[item.prop]"
            :placeholder="'请输入'+item.label"
          ></el-input>
          <span v-if="  !scope.row.edit">{{scope.row[item.prop]}}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <!-- 全局控制的编辑 -->
          <div v-if="is_edit&&scope.row.add==undefined" style="display: inline-block;">
            <!-- 编辑 -->
            <el-button
              size="mini"
              v-if="!scope.row.edit"
              @click="handleEdit(scope.$index, scope.row)"
              type="primary"
            >Edit</el-button>
            <!-- 保存 -->
            <el-button
              size="mini"
              type="success"
              :plain="true"
              v-if="scope.row.edit"
              @click="handleSave(scope.$index, scope.row)"
            >Save</el-button>
          </div>
          <!-- 添加控制 -->
          <div v-if="scope.row.add!=undefined&&scope.row.add" style="display: inline-block;">
            <!-- 保存 -->
            <el-button
              size="mini"
              type="success"
              :plain="true"
              v-if="scope.row.edit"
              @click="handleSave(scope.$index, scope.row)"
            >Save</el-button>
          </div>
          <!-- 全局控制删除 -->
          <el-button
            size="mini"
            v-if="is_delete&&scope.row.add==undefined"
            :plain="true"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
          >Delete</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  methods: {
    // 隔行变色
    tableRowClassName () {
      // 选取DOM节点
      var trs = this.$refs.mytable.$el
        .getElementsByTagName('tbody')[0]
        .getElementsByTagName('tr')
      for (var i in trs) {
        if (i % 2 === 0) {
          // 当隔行变色未true时改变颜色
          if (this.space_color) {
            trs[i].style.backgroundColor = '#f0f9eb'
          } else {
            trs[i].style.backgroundColor = ''
          }
        }
      }
    },

    // 多选框
    handleSelectionChange (val) {
      this.multipleSelection = val
      console.log('selection:', this.multipleSelection)
    },
    // 编辑
    handleEdit (index, row) {
      console.log(index, row)
      row.edit = true
    },
    // 删除
    handleDelete (index, row) {
      console.log(index, row)

      this.table_data.splice(index, 1)

      this.$message({
        message: '删除成功！',
        type: 'success'
      })
    },
    // 保存
    handleSave (index, row) {
      console.log(index, row)
      row.edit = false

      delete this.table_data[index].add

      this.$message({
        message: '保存成功！',
        type: 'success'
      })
    },
    handleAdd () {
      var addDataJson = {}
      for (var key in this.new_date_json) {
        if (key === 'edit') {
          delete addDataJson[key]
        } else if (key === 'add') {
          delete addDataJson[key]
        } else {
          addDataJson[key] = ''
        }
      }
      addDataJson.edit = true
      addDataJson.add = true
      this.table_data.push(addDataJson)
    },
    // 初始化编辑属性
    initEditAttribute () {
      // var self = this
      // var edit = self.edit

      var dataArray = [
        // {
        //   date: '2016-05-03',
        //   name: '王小虎',
        //   province: '上海',
        //   city: '普陀区',
        //   address: '上海市普陀区金沙江路 1518 弄',
        //   zip: 200333,
        //   sex: 18
        // },
        // {
        //   date: '2016-05-02',
        //   sex: 18,
        //   name: '王小虎',
        //   province: '上海',
        //   city: '普陀区',
        //   address: '上海市普陀区金沙江路 1518 弄',
        //   zip: 200333
        // },
        // {
        //   date: '2016-05-04',
        //   name: '王小虎',
        //   sex: 18,
        //   province: '上海',
        //   city: '普陀区',
        //   address: '上海市普陀区金沙江路 1518 弄',
        //   zip: 200333
        // }
      ]

      if (dataArray.length > 0) {
        // 添加编辑事件
        for (var index in dataArray) {
          dataArray[index]['edit'] = false
          this.table_data.push(dataArray[index])
        }

        if (Object.keys(this.new_date_json).length === 0) {
          // 新增时，初始化数据结构
          this.initAddDataJson(dataArray[0])
        }
      }
      console.log('this.tableData:', this.table_data)
    },
    initAddDataJson (dataArray) {
      // 新增时，初始化数据结构
      var dataJson = dataArray
      var newDateJson = {}
      for (var key in dataJson) {
        if (key === 'edit') {
          newDateJson[key] = 'true'
        } else {
          newDateJson[key] = ''
        }
      }
      newDateJson['add'] = true
      this.new_date_json = newDateJson
    }
  },
  mounted: function () {
    this.initEditAttribute()
    // 确保方法在页面渲染后调用
    this.$nextTick(function () {
      /// //方法
      this.tableRowClassName()
    })
  },
  watch: {
    space_color: function () {
      // 监听数据变化
      this.$nextTick(function () {
        /// //方法
        this.tableRowClassName()
      })
    },
    table_data: function () {
      // 监听数据变化f
      this.$nextTick(function () {
        /// //方法
        this.tableRowClassName()
      })
    }
  },
  data () {
    return {
      new_date_json: {}, // 数据结构
      multipleSelection: [], // 复选框，数据
      is_edit: true, // 是否可编辑
      is_delete: true, // 是否可删除
      selection: true, // 是否需要复选框
      radio: false, // 单选变色
      space_color: true, // 隔行变色
      // 表头信息
      table_columns: [
        {
          prop: 'psx',
          label: 'psx',
          width: '60'
        },
        {
          prop: 'psy',
          label: 'psy',
          width: '60'
        },
        {
          prop: 'psz',
          label: 'psz',
          width: '60'
        },
        {
          prop: 'id1',
          label: 'id1',
          width: '300'
        },
        {
          prop: 'ap1',
          label: 'ap1',
          width: '60'
        },
        {
          prop: 'id2',
          label: 'id2',
          width: '150'
        },
        {
          prop: 'ap2',
          label: 'ap2',
          width: '60'
        },
        {
          prop: 'id3',
          label: 'id3',
          width: '150'
        },
        {
          prop: 'ap3',
          label: 'ap3',
          width: '60'
        },
        {
          prop: 'id4',
          label: 'id4',
          width: '150'
        },
        {
          prop: 'ap4',
          label: 'ap4',
          width: '60'
        },
        {
          prop: 'id5',
          label: 'id5',
          width: '150'
        },
        {
          prop: 'ap5',
          label: 'ap5',
          width: '60'
        },
        {
          prop: 'id6',
          label: 'id6',
          width: '150'
        },
        {
          prop: 'ap6',
          label: 'ap6',
          width: '60'
        },
        {
          prop: 'id7',
          label: 'id7',
          width: '150'
        },
        {
          prop: 'ap7',
          label: 'ap7',
          width: '60'
        },
        {
          prop: 'id8',
          label: 'id8',
          width: '150'
        },
        {
          prop: 'ap8',
          label: 'ap8',
          width: '60'
        },
        {
          prop: 'id9',
          label: 'id9',
          width: '150'
        },
        {
          prop: 'ap9',
          label: 'ap9',
          width: '60'
        },
        {
          prop: 'id10',
          label: 'id10',
          width: '150'
        },
        {
          prop: 'ap10',
          label: 'ap10',
          width: '60'
        }
      ],
      // 表格数据
      table_data: [{
        'psx': 1,
        'psy': 2,
        'psz': 3,
        'id1': 'ajdf',
        'ap1': 4,
        'id2': 'jlfds',
        'ap2': 5,
        'id3': 'ouewr',
        'ap3': 6,
        'id4': 'uioe',
        'ap4': 8,
        'id5': 'ldscn',
        'ap5': 9,
        'id6': 'cnl',
        'ap6': 10,
        'id7': 'cnvn',
        'ap7': 11,
        'id8': 'bvan',
        'ap8': 12,
        'id9': 'cbnc',
        'ap9': 13,
        'id10': 'clndv',
        'ap10': 14
      }]
    }
  },
  created () {
    this.$route.query.total_name = 'haitao'
    this.$axios.get('http://127.0.0.1:5000/getDeveloperNewFingersForDeveloper/' + this.$route.query.total_name).then(res => {
      console.log(res['data'])
      let arr = res['data']
      // this.table_data.push(arr[0])
      // this.table_data.push(arr[1])
      // this.table_data.push(arr[2])
      // this.table_data.push(arr[3])
      // this.table_data.push(arr[4])
      // this.table_data.push(arr[5])
      for (let j = 0, len = arr.length; j < len; j++) {
        this.table_data.push(arr[j])
      }
      // this.table_data.push(res['data'][0])

      // console.log(res['data'][0])
    })
  }
}
</script>
<style scoped>
.button_size{
  width:80px;
}

</style>
