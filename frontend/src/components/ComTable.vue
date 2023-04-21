<template>
  <el-dialog
    :title="addEdit ? '添加用户' : '编辑用户'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item :label="label.name">
        <el-input v-model="form.name" style="width: 200px"></el-input>
      </el-form-item>
      <el-form-item :label="label.age">
        <el-input v-model="form.age" style="width: 200px"></el-input>
      </el-form-item>
      <el-form-item :label="label.sex">
        <el-radio-group v-model="form.sex" style="width: 200px">
          <el-radio label="男"></el-radio>
          <el-radio label="女"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item :label="label.date">
        <el-date-picker
          type="date"
          value-format="yyyy-MM-dd"
          placeholder="选择日期"
          v-model="form.date"
          formt
          style="width: 200px"
        ></el-date-picker>
      </el-form-item>
      <el-form-item :label="label.address">
        <el-input v-model="form.address" style="width: 500px"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="handleClose">取 消</el-button>
      <el-button type="primary" @click="saveForm">确 定</el-button>
    </div>
  </el-dialog>
</template>
<script>
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
    return {};
  },
  methods: {
    handleClose() {
      this.$emit("handleClose", false);
    },
    saveForm() {
      this.$emit("saveForm", false, this.form);
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