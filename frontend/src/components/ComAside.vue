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
    <h3>{{ $root.$guser ? "电柜管理者模式" : "共享电柜管理系统" }}</h3>
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
          title: "主页",
          path: "/home",
        },
        {
          icon: "el-icon-menu",
          title: "信息总览",
          path: "/overview",
        },
        {
          icon: "el-icon-document",
          title: "可用电瓶查询",
          path: "/available",
        },
        {
          icon: "el-icon-setting",
          title: "归还点位查询",
          path: "/return",
        },
        {
          icon: "el-icon-setting",
          title: "我的车库",
          path: "/user",
        },
        {
          icon: "el-icon-setting",
          title: "我的工单",
          path: "/order",
        }
      ],
    };
  },
  created(){
    if(this.$root.$guser === 'admin'){
      this.menu.push({
        icon: "el-icon-setting",
        title: "电柜管理",
        path: "/cabinet",
      })
      this.menu.push({
        icon: "el-icon-setting",
        title: "公司管理",
        path: "/company",
      })
      this.menu.forEach((item) => {
      if (item.title === "归还点位查询") {
        item.title = "点位管理";
      }
      if (item.title === "可用电瓶查询") {
        item.title = "电瓶管理";
      }
      if (item.title === "我的车库") {
        item.title = "车辆管理";
      }
      if (item.title === "我的工单") {
        item.title = "工单管理";
      }
    });

    
    }
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