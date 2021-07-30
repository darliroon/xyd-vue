<template>
  <div>
    <el-button style="position:absolute; left:1698px; top:80px;" type="warning" round @click="uploadButtonClick"
               v-loading.fullscreen.lock="fullscreenLoading">Upload</el-button>
    <el-dropdown @command="handleCommand">
  <span class="el-dropdown-link">
    Fingerprint<i class="el-icon-arrow-down el-icon--right"></i>
  </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="a">MapResource</el-dropdown-item>
        <el-dropdown-item command="b">Navigation</el-dropdown-item>
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
      <el-table-column label="psx" :width="width1">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.psx"></el-input>
          <span v-show="!scope.row.show">{{scope.row.psx}}</span>
        </template>
      </el-table-column>
      <el-table-column label="psy" :width="width1">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.psy"></el-input>
          <span v-show="!scope.row.show">{{scope.row.psy}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="psz" label="psz" :width="width1">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.psz"></el-input>
          <span v-show="!scope.row.show">{{scope.row.psz}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id1" label="id1" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id1"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id1}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap1" label="ap1" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap1"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap1}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id2" label="id2" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id2"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id2}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap2" label="ap2" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap2"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap2}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id3" label="id3" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id3"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id3}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap3" label="ap3" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap3"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap3}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id4" label="id4" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id4"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id4}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap4" label="ap4" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap4"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap4}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id5" label="id5" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id5"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id5}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap5" label="ap5" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap5"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap5}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id6" label="id6" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id6"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id6}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap6" label="ap6" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap6"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap6}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id7" label="id7" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id7"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id7}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap7" label="ap7" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap7"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap7}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id8" label="id8" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id8"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id8}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap8" label="ap8" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap8"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap8}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id9" label="id9" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id9"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id9}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap9" label="ap9" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap9"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap9}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="id10" label="id10" :width="width2">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.id10"></el-input>
          <span v-show="!scope.row.show">{{scope.row.id10}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="ap10" label="ap10" :width="width3">
        <template slot-scope="scope">
          <el-input placeholder="Enter.." v-show="scope.row.show" v-model="scope.row.ap10"></el-input>
          <span v-show="!scope.row.show">{{scope.row.ap10}}</span>
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
      width2: '250',
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
      this.$message('click on item ' + command)
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
      this.$route.query.total_name = 'haitao'
      this.fullscreenLoading = true
      this.$axios.get('http://127.0.0.1:5000/dropFingerTable/' + this.$route.query.total_name).then(res => {
        console.log(res['data'])
        if (res['data'] === 0) {
          this.$axios.post('http://127.0.0.1:5000/newFingerTable', {
            'name': this.$route.query.total_name,
            'sql': 'CREATE TABLE ' + this.$route.query.total_name + ' (' + 'psx int, psy int, psz int, id1 text, ap1 int, id2 text, ap2 int, id3 text, ap3 int, id4 text,' +
              ' ap4 int, id5 text, ap5 int, id6 text, ap6 int, id7 text, ap7 int, id8 text, ap8 int, id9 text, ap9 int, id10 text, ap10 int' + ')'
          }).then(res => {
            console.log(res['data'])
            if (res['data'] === 0) {
              this.$axios.post('http://127.0.0.1:5000/insertManyFingers/' + this.$route.query.total_name, this.tableData).then(res => {
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
    this.$route.query.total_name = 'haitao'
    this.$axios.get('http://127.0.0.1:5000/getDeveloperNewFingersForDeveloper/' + this.$route.query.total_name).then(res => {
      console.log(res['data'])
      let arr = res['data']
      for (let j = 0, len = arr.length; j < len; j++) {
        arr[j].show = false
        this.tableData.push(arr[j])
      }
      // this.table_data.push(res['data'][0])

      // console.log(res['data'][0])
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
