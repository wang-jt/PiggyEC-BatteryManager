<template>
  <el-container style="height: 100%">
    <el-aside width="auto">
      <com-aside></com-aside>
    </el-aside>
    <el-container>
      <el-header>
        <com-header></com-header>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import ComAside from "@/components/ComAside.vue";
import ComHeader from "@/components/ComHeader.vue";
export default {
  components: {
    ComAside,
    ComHeader,
  },
};
</script>

<style lang="scss" scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
}
.el-main {
  background-color: #eee;
}

body > .el-container {
  margin-bottom: 20px;
}
</style>