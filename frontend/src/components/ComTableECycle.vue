<template>
  <el-dialog
    :title="addEdit ? '添加电动自行车' : '编辑电动自行车'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="类型">
        <el-input v-model="form.type" style="width: 200px"></el-input>
      </el-form-item>
      <el-form-item label="参数">
        <el-input v-model="form.parameter" style="width: 200px"></el-input>
      </el-form-item>
      <el-form-item label="所属者">
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
      users:[],
      isDisabled: false,
    };
  },
  created(){
    const res = reqAPI('GET',`/getUsers/${this.$root.$guser}`, null);
    this.users = this.$root.$guser === 'admin' ? res.tableData : [{id: this.$root.$guserid, name: this.$root.$guser}];
    console.log('获取到的users为',this.users);
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