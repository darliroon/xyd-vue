<template>
  <div>
    <el-button style="position:absolute; left:1698px; top:80px;" type="warning" round @click="uploadButtonClick"
               v-loading.fullscreen.lock="fullscreenLoading">Upload</el-button>
    <el-dropdown @command="handleCommand">
  <span class="el-dropdown-link">
    Navigation<i class="el-icon-arrow-down el-icon--right"></i>
  </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="a">MapResource</el-dropdown-item>
        <el-dropdown-item command="b">Fingerprint</el-dropdown-item>
        <el-dropdown-item command="c">MainObjects</el-dropdown-item>
        <!--        <el-dropdown-item command="d" disabled>Fingerprint</el-dropdown-item>-->
        <el-dropdown-item command="e" divided>Return</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <!--    <el-row :gutter="20" style="left:200px;">-->
    <!--    <el-row :gutter="20">-->
    <!--      <el-col :span="6"><el-button>Fingerprint</el-button></el-col>-->
    <!--      <el-col :span="6"><el-button>MainObjects</el-button></el-col>-->
    <!--      <el-col :span="6"><el-button>Navigation</el-button></el-col>-->
    <!--      <el-col :span="6"><el-button>MapResource</el-button></el-col>-->
    <!--    </el-row>-->
    <!--    </el-row>-->
    <el-table
      :data="tableData"
      style="width: 100%;margin-top:20px"
      scripe
      border
      :cell-style="cs"
      max-height="800"
      :header-cell-style="hcs">
      <el-table-column
        type="index"
        :index="indexMethod">
      </el-table-column>
      <el-table-column prop="x1" label="x1" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.x1"></el-input>
          <span v-show="!scope.row.show">{{scope.row.x1}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="y1" label="y1" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.y1"></el-input>
          <span v-show="!scope.row.show">{{scope.row.y1}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="z1" label="z1" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.z1"></el-input>
          <span v-show="!scope.row.show">{{scope.row.z1}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="x2" label="x2" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.x2"></el-input>
          <span v-show="!scope.row.show">{{scope.row.x2}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="y2" label="y2" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.y2"></el-input>
          <span v-show="!scope.row.show">{{scope.row.y2}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="z2" label="z2" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.z2"></el-input>
          <span v-show="!scope.row.show">{{scope.row.z2}}</span>
        </template>
      </el-table-column>
      <el-table-column label="OP" width="260" fixed="right">
        <template slot-scope="scope">
          <el-button @click="scope.row.show =true" type="success">Edit</el-button>
          <el-button @click="scope.row.show =false" type="primary">Save</el-button>
          <el-button @click="deleteButtonClick(scope.$index, scope.row)" type="danger">Del</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  data () {
    return {
      tableData: [
        // {
        //   'psx': 1,
        //   'psy': 2,
        //   'psz': 3,
        //   'id1': 'qwe',
        //   'ap1': 4,
        //   'id2': 'asd',
        //   'ap2': 5,
        //   'id3': 'zxc',
        //   'ap3': 6,
        //   'id4': 'rty',
        //   'ap4': 7,
        //   'id5': 'hgj',
        //   'ap5': 8,
        //   'id6': 'uio',
        //   'ap6': 45,
        //   'id7': 'bvn',
        //   'ap7': 89,
        //   'id8': 'vjd',
        //   'ap8': 78,
        //   'id9': 'bvn',
        //   'ap9': 67,
        //   'id10': 'vbc',
        //   'ap10': 96,
        //   show: false
        // }
      ],
      width1: '100',
      width2: '240',
      width3: '100',
      fullscreenLoading: false
    }
  },
  methods: {
    hcs () {
      return 'text-align: center;background:rgb(242,242,242);color:rgb(140,138,140)'
    },
    cs () {
      return 'text-align:center'
    },
    indexMethod (index) {
      return index + 1
    },
    handleCommand (command) {
      // this.$message('click on item ' + command)
      if (command === 'a') {
        console.log('A happen')
      } else if (command === 'b') {
        console.log('A not happen')
        this.$router.push({
          path: '/developer1/developMode/mode2',
          query: {
            total_name: this.$route.query.total_name,
            user_name: this.$route.query.user_name
          }
        })
      } else if (command === 'c') {
        console.log('...')
      } else {
        this.$router.push({
          path: '/developer1/developMode',
          query: {
            total_name: this.$route.query.total_name,
            user_name: this.$route.query.user_name
          }
        })
      }
    },
    // saveButtonClick () {
    // //
    // },
    deleteButtonClick (index, row) {
      row.show = false
      console.log(index, row)
      this.tableData.splice(index, 1)
    },
    uploadButtonClick () {
      // this.$route.query.total_name = 'haitao'
      this.fullscreenLoading = true
      this.$axios.get('http://127.0.0.1:5000/dropNavTable/' + this.$route.query.total_name).then(res => {
        console.log(res['data'])
        if (res['data'] === 0) {
          this.$axios.post('http://127.0.0.1:5000/newNavTable', {
            'name': this.$route.query.total_name,
            'sql': 'CREATE TABLE ' + this.$route.query.total_name + '(' + 'x1 int, y1 int, z1 int, x2 int, y2 int, z2 int' + ')'
          }).then(res => {
            console.log(res['data'])
            if (res['data'] === 0) {
              this.$axios.post('http://127.0.0.1:5000/insertManyNavs/' + this.$route.query.total_name, this.tableData).then(res => {
                console.log(res)
                if (res['data'] === 0) {
                  console.log('Successfully modify!')
                  this.$message.success('Successfully modify!')
                  this.fullscreenLoading = false
                } else {
                  console.log('Failed!')
                  this.$message.error('Failed!')
                  this.fullscreenLoading = false
                }
              })
            } else {
              console.log('Create NewTable Failed')
              this.$message.error('Failed!')
              this.fullscreenLoading = false
            }
          })
        } else {
          console.log('Drop Fingerprint Failed!')
          this.$message.error('Failed!')
          this.fullscreenLoading = false
        }
      })
    }
  },
  created () {
    // this.$route.query.total_name = 'haitao'
    this.fullscreenLoading = true
    this.$axios.get('http://127.0.0.1:5000/getDeveloperNavs/' + this.$route.query.total_name).then(res => {
      console.log(res['data'])
      let arr = res['data']
      for (let j = 0, len = arr.length; j < len; j++) {
        arr[j].show = false
        // let list = arr[j]['coordinate'].split('&')
        // let dict = {
        //   'name': arr[j]['name'],
        //   'coordinatex': list[0],
        //   'coordinatey': list[1],
        //   'coordinatez': list[2],
        //   'label': arr[j]['label'],
        //   'details': arr[j]['details'],
        //   'comments': arr[j]['comments']
        // }
        // dict.show = false
        this.tableData.push(arr[j])
      }
      this.fullscreenLoading = false
      // this.table_data.push(res['data'][0])
    })
  }
}
</script>

<style>
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}
.el-icon-arrow-down {
  font-size: 12px;
}
</style>
