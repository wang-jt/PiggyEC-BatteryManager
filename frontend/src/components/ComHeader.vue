<template>
  <div class="com-header">
    <i
      :class="$store.state.isCollapse ? 'el-icon-s-fold' : 'el-icon-s-unfold'"
      @click="clickCollapse"
    ></i>
    <com-tag></com-tag>
    <el-dropdown>
      <img src="@/assets/user.png" />
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-user-solid">
          <span @click="personclick">个人中心</span>
        </el-dropdown-item>
        <el-dropdown-item icon="el-icon-error">
          <span @click="loginout">退出</span>
        </el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import ComTag from './ComTag.vue';
export default {
   components:{
    ComTag
   },
  methods: {
    clickCollapse() {
      this.$store.commit("clickCollapse");
    },
    personclick() {
      console.log('personclick');
      //this.$router.push("/person");
    },
    loginout() {
      console.log('loginout');
      this.$router.push("/login");
    },
  },
};
</script>

<style lang="scss" scoped>
.com-header {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  i {
    color: #000;
    font-size: 30px;
  }
  img {
    width: 40px;
    height: 40px;
    border-radius: 100%;
    border: 1px solid #fff;
  }
}
</style>