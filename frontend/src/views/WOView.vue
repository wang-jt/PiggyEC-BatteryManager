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
      <el-input v-model="search" align="right" placeholder="输入标题或内容进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
            !search || data.title.toLowerCase().includes(search.toLowerCase())
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
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <com-pagination align="right" :total="this.tableData.length"></com-pagination>
  </div>
</template>

<script>
import ComTable from "@/components/ComTableWO.vue";
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
        id: "工单编号",
        title: "工单标题",
        content: "工单内容",
        ownerId: "工单发起者ID",
        ownerName: "工单发起者名",
      },
      form: {
        id: "",
        title: "",
        content: "",
        ownerId: "",
      },
      tableData: [
        
      ],
      search: "",
    };
  },
  created() {
    this.tableData = reqAPI('GET',`/workorder/getallworkorder/${this.$root.$guser}`, null).tableData;
    console.log(this.tableData);
  },

  methods: {
    clearForm() {
      this.tableData = reqAPI('GET',`/workorder/getallworkorder/${this.$root.$guser}`, null).tableData;
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
      console.log('addecycle', form);
      reqAPI('POST',`/workorder/addworkorder`, form);
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
      reqAPI('POST',`/workorder/deleteworkorder/${row.id}`, null);
      this.tableData = reqAPI('GET',`/workorder/getallworkorder/${this.$root.$guser}`, null).tableData;
    },
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