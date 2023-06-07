<template>
  <el-dialog
    :title="addEdit ? '添加电瓶' : '编辑电瓶'"
    width="700px"
    :visible.sync="dialogForm"
    :before-close="handleClose"
  >
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="类型">
      <el-input v-model="form.size" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="剩余电量">
      <el-input v-model="form.powerLeft" style="width: 200px"></el-input>
    </el-form-item>
    <el-form-item label="母插槽">
      <el-select v-model="form.masterSlotId" style="width: 200px">
        <el-option
          v-for="slot in slots.filter(
          (data) =>
            !form.size || data.type.includes(form.size)
        )"
          :key="slot.id"
          :label="slot.name"
          :value=slot.id
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
      slots:[],
      isDisabled: false,
    };
  },
  created(){
    const res = reqAPI('GET',`/slot/getallslot`, null);
    this.slots = res.tableData;
    console.log('获取到的company为',this.slots);  
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