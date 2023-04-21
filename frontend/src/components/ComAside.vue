<template>
  <el-menu
    default-active="0"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    background-color="#304155"
    text-color="#fff"
    active-text-color="#409EFF"
    style="height: 100%; border: none"
    :collapse="$store.state.isCollapse"
  >
    <h3>{{ $store.state.isCollapse ? "管理" : "牛人后台管理系统" }}</h3>
    <el-menu-item
      @click="clickMenu(item)"
      v-for="(item, index) in menu"
      :key="index"
      :index="index.toString()"
      :disabled="item.title==='其他'?true:false"
    >
      <i :class="item.icon"></i>
      <span slot="title">{{ item.title }}</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          icon: "el-icon-menu",
          title: "首页",
          path: "/home",
        },
        {
          icon: "el-icon-document",
          title: "用户",
          path: "/user",
        },
        {
          icon: "el-icon-setting",
          title: "其他",
          path: "/other",
        }
      ],
    };
  },
  methods: {
    clickMenu(item) {
      this.$store.commit("clickMenu", item);
      this.$router.replace(item.path).catch(err=>err) 
      console.log(item);
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style lang="scss" scoped>
.el-menu-vertical-demo {
  h3 {
    color: #fff;
    margin: 20px 10px;
    text-align: center;
    font-size: 20px;
  }
}
</style>