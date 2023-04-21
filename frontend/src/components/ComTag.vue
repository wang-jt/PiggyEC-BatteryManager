<template>
  <div class="tag">
    <el-tag
      v-for="(tag, index) in tags"
      :key="index"
      :closable="tag.title !== '首页' ? true : false"
      :type="tag.title === '首页' ? 'success' : 'warning'"
      @close="closeTag(tag, index)"
      @click="clickTag(tag.path)"
    >
      {{ tag.title }}
    </el-tag>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {};
  },
  methods: {
    closeTag(tag, index) {
      var length = this.tags.length - 1;
      this.$store.commit("closeTag", tag);
      if (tag.path !== this.$route.path) {
        return;
      }
      if (length === index) {
        console.log("length === index" + length);
        this.$router.replace(this.tags[index - 1].path).catch((err) => err);
      } else {
        this.$router.replace(this.tags[index].path).catch((err) => err);
        console.log("length !== index" + length);
      }
    },
    clickTag(path) {
      this.$router.replace(path).catch((err) => err);
    },
  },
  computed: {
    ...mapState({
      tags: (state) => state.tagList,
    }),
  },
};
</script>

<style lang="scss" scoped>
.tag {
  width: 100%;
  .el-tag {
    margin-left: 8px;
  }
}
</style>
