<template>
  <el-pagination
    background
    layout="total,prev, pager, next,jumper"
    :total="total"
    :page-size="10"
  ></el-pagination>
</template>

<script>

export default {
  props: {
    total: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      
    };
  },
  methods: {
    
  },
};
</script>

<style lang="scss">
</style>