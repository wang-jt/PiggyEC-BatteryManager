<template>
  <el-dialog
    :title="addEdit ? '添加公司' : '编辑公司'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="名称">
      <el-input v-model="form.name" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="地址">
      <el-input v-model="form.address" style="width: 400px"></el-input>
    </el-form-item>
  </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="handleClose">取 消</el-button>
      <el-button type="primary" @click="saveForm">确 定</el-button>
    </div>
  </el-dialog>
</template>
<script>
import { reqAPI } from '@/request';

export default {
  props: {
    form: {
      type: Object,
      default: Object,
    },
    dialogForm: {
      type: Boolean,
      default: false,
    },
    label: {
      type: Object,
      default: Object,
    },
    addEdit: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      companies:[],
      isDisabled: false,
    };
  },
  created(){
  },
  methods: {
    handleClose() {
      this.$emit("handleClose", false);
    },
    saveForm() {
      this.$emit("saveForm", false, this.form, this.addEdit);
    },
  },
};
</script>

<style lang="scss" scoped>
.el-form {
  display: flex;
  flex-wrap: wrap;
}
</style>