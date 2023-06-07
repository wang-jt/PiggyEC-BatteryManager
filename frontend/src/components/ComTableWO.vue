<template>
  <el-dialog
    :title="'发起工单'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="标题">
        <el-input v-model="form.title" style="width: 300px"></el-input>
      </el-form-item>
      <el-form-item label="内容">
        <el-input v-model="form.content" style="width: 400px"></el-input>
      </el-form-item>
      <el-form-item label="发起者">
        <el-select v-model="form.ownerId" style="width: 200px">
          <el-option  
            v-for="user in users"
            :key="user.id"
            :label="user.name"
            :value=user.id
          ></el-option>
        </el-select>
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
    return {
      users:[],
      isDisabled: false,
    };
  },
  created(){
    this.users = [{id: this.$root.$guserid, name: this.$root.$guser}];
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