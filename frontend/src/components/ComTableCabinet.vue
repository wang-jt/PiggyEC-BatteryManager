<template>
  <el-dialog
    :title="addEdit ? '添加共享电柜' : '编辑共享电柜'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="名称">
      <el-input v-model="form.name" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="类型">
      <el-input v-model="form.type" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="位置">
      <el-input v-model="form.pos" style="width: 400px"></el-input>
    </el-form-item>
    <el-form-item label="最大槽数">
      <el-input v-model="form.maxSlotNum" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="所属公司">
      <el-select v-model="form.companyId" style="width: 200px">
        <el-option
          v-for="company in companies"
          :key="company.id"
          :label="company.name"
          :value=company.id
        ></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="横坐标">
      <el-input v-model="form.locx" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="纵坐标">
      <el-input v-model="form.locy" style="width: 200px"></el-input>
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
    const res = reqAPI('GET',`/company/getallcompany`, null);
    this.companies = res.tableData;
    console.log('获取到的company为',this.companies);  
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