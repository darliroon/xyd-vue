<template>
  <div>
    <el-card class="box-card-1">
      <div slot="header" class="clearfix">
        <div class="centerText">About Us</div>
      </div>
      <div class="text item">
        <ul>
          <li class="centerText">Author: 李海涛</li>
          <br>
          <li class="centerText">全栈工程师</li>
          <br>
          <li class="centerText">爆肝</li>
        </ul>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style scoped>
.box-card-1{
  position: absolute;
  top: 250px;
  left: 670px;
  width: 600px;
  height: 350px;
}
.centerText{
  text-align:center;
  font-size: 30px;
}

</style>
