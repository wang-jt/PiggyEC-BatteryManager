<template>
  <div class="user">
    <div class="add-search">
      <el-button
        type="primary"
        @click="dialogForm = true"
        icon="el-icon-circle-plus-outline"
        >添加</el-button
      >
      <!--  -->
      <com-table
        :label="label"
        :dialogForm="dialogForm"
        @saveForm="saveForm"
        @handleClose="handleClose"
        :form="addEdit ? form : editForm"
        :addEdit="addEdit"
      ></com-table>
      <!--  -->
      <el-input v-model="search" align="right" placeholder="输入电柜名/位置名/型号进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
            !search || data.name.includes(search)
        )
      "
      style="width: 100%"
    >
      <el-table-column
        v-for="(val, key) in label"
        :key="key"
        :label="val"
        :prop="key"
      >
      </el-table-column>
      <el-table-column align="right">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleShow(scope.$index, scope.row)" style="background-color: #409EFF; color: #FFFFFF;">
            查看</el-button
          >
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
            >编辑</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :visible.sync="dialogVisible" title="插槽详情" width="30%">
      <el-table :data="slotData" style="width: 100%">
        <el-table-column prop="id" label="ID"></el-table-column>
        <el-table-column prop="type" label="类型"></el-table-column>
        <el-table-column prop="maxNum" label="最大电瓶容量"></el-table-column>
        <el-table-column prop="usedNum" label="当前电瓶容量"></el-table-column>
      </el-table>
    </el-dialog>
    <com-pagination align="right" :total="this.tableData.length"></com-pagination>
  </div>
</template>

<script>
import ComTable from "@/components/ComTableCabinet.vue";
import ComPagination from "@/components/ComPagination.vue";
import { reqAPI } from "@/request";
export default {
  components: {
    ComTable,
    ComPagination,
  },
  data() {
    return {
      editForm: {},
      addEdit: true,
      dialogForm: false,
      label: {
        id: "编号",
        name: "名称",
        pos: "地址",
        type: "型号",
        maxSlotNum: "最大插槽数",
        companyName: "所属公司",
        locx: "经度",
        locy: "纬度",
      },
      form: {
        id: "",
        name: "",
        pos: "",
        type: "",
        maxSlotNum: "",
        companyId: "",
        locx: "",
        locy: "",
      },
      tableData: [
        
      ],
      search: "",
      slotData: [],
      dialogVisible: false,
    };
  },
  created() {
    this.tableData = reqAPI('GET',`/cabinet/getallcabinet`, null).tableData;
    console.log(this.tableData);
  },
  methods: {
    clearForm() {
      this.tableData = reqAPI('GET',`/cabinet/getallcabinet`, null).tableData;
      setTimeout(() => {
        this.form = {
        id: "",
        type: "",
        parameter: "",
        ownerId: "",
      },
        this.addEdit = true;
      }, 200);
    },
    saveForm(bool, form, isAdd) {
      this.dialogForm = bool;
      if (isAdd == false) {
        reqAPI('POST',`/cabinet/editcabinet/${form.id}`, form);
      } else{
        reqAPI('POST',`/cabinet/addcabinet`, form);
      }
      this.clearForm();
    },
    handleClose(bool) {
      this.dialogForm = bool;
      this.clearForm();
    },
    handleEdit(index, row) {
      this.dialogForm = true;
      this.addEdit = false;
      this.editForm = row;
    },
    handleDelete(index, row) {
      console.log('handledelete', row.id);
      reqAPI('POST',`/cabinet/deletecabinet/${row.id}`, null);
      this.tableData = reqAPI('GET',`/cabinet/getallcabinet`, null).tableData;
    },
    handleShow(index, row){
      this.slotData = reqAPI('GET',`/slot/getcabinetslot/${row.id}`, null).tableData;
      this.dialogVisible = true;
    } 
  },
};
</script>

<style lang="scss" scoped>
.user {
  .add-search {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    .el-input {
      width: 20%;
    }
  }
  .table {
    height: 590px;
    overflow: hidden;
  }
}
</style>