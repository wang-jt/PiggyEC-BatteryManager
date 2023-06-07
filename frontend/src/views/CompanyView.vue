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
      <el-input v-model="search" align="right" placeholder="输入公司名进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
            !search || data.type.includes(search)
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
    <com-pagination align="right" :total="this.tableData.length"></com-pagination>
  </div>
</template>

<script>
import ComTable from "@/components/ComTableCompany.vue";
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
        address: "地址",
      },
      form: {
        id: "",
        name: "",
        address: "",
      },
      tableData: [
        
      ],
      search: "",
    };
  },
  created() {
    this.tableData = reqAPI('GET',`/company/getallcompany`, null).tableData;
    console.log(this.tableData);
  },

  methods: {
    clearForm() {
      this.tableData = reqAPI('GET',`/company/getallcompany`, null).tableData;
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
        reqAPI('POST',`/company/editcompany/${form.id}`, form);
      } else{
        reqAPI('POST',`/company/addcompany`, form);
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
      reqAPI('POST',`/company/deletecompany/${row.id}`, null);
      this.tableData = reqAPI('GET',`/company/getallcompany`, null).tableData;
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