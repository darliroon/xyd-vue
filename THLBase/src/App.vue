<template>
  <div id="app">
<!--    <div class="home">-->
<!--      <vue-canvas-nest :config="{color:'255,0,0', count: 88}" :el="'#area'">-->
<!--      </vue-canvas-nest>-->
<!--      <div id="area" class="background">里面是背景上面的内容</div>-->
<!--    </div>-->
    <el-container>
      <el-header>
        <el-menu
          :default-active="activeIndex"
          class="my-el-menu"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="/index" class="submenu-title">Home</el-menu-item>
<!--          <el-menu-item index="/index" class="submenu-title">    </el-menu-item>-->
          <el-submenu index="2">
            <template slot="title">
                <span class="submenu-title">
                  Develop
                </span>
            </template>
            <el-menu-item index="/developer1">Modify</el-menu-item>
            <el-menu-item index="/developer2">Build New</el-menu-item>
          </el-submenu>
<!--          <el-menu-item index="/index" class="submenu-title">    </el-menu-item>-->
          <el-submenu index="3">
            <template slot="title">
                <span class="submenu-title">
                  Monitor
                </span>
            </template>
            <el-menu-item index="/monitor1">Monitor1</el-menu-item>
            <el-menu-item index="/monitor2">Monitor2</el-menu-item>
          </el-submenu>
<!--          <el-menu-item index="/index" class="submenu-title">    </el-menu-item>-->
          <el-submenu index="4">
            <template slot="title">
                <span class="submenu-title">
                  Downloads
                </span>
            </template>
            <el-menu-item index="/jsonGet">jresource</el-menu-item>
            <el-menu-item index="/Downloads2">APP</el-menu-item>
          </el-submenu>
<!--          <el-menu-item index="/index" class="submenu-title">    </el-menu-item>-->
          <el-submenu index="5">
            <template slot="title">
                <span class="submenu-title">
                  Register
                </span>
            </template>
            <el-menu-item index="/Register1">re1</el-menu-item>
            <el-menu-item index="/Register2">re2</el-menu-item>
          </el-submenu>
<!--          <el-menu-item index="/index" class="submenu-title">    </el-menu-item>-->
<!--          <el-menu-item index="/diffexp" class="submenu-title">Differential Expression</el-menu-item>-->
<!--          <el-menu-item index="/targets" class="submenu-title">miRNA Targets</el-menu-item>-->
<!--          <el-menu-item index="/enrichment" class="submenu-title">Enrichment Analysis</el-menu-item>-->
          <el-menu-item index="/about" class="submenu-title">About</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import vueCanvasNest from 'vue-canvas-nest'
export default {
  name: 'App',
  data () {
    return {
      activeIndex: this.$route.path
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      this.$router.push(key)
    }
  },
  components: {vueCanvasNest}
}
</script>

<style>
#app {
}
.submenu-title{
  font-size: 18px !important;
}

</style>
