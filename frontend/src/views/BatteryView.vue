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
      <com-table-e-cabinet
        :label="label"
        :dialogForm="dialogForm"
        @saveForm="saveForm"
        @handleClose="handleClose"
        :form="addEdit ? form : editForm"
        :addEdit="addEdit"
      ></com-table-e-cabinet>
      <!--  -->
      <el-input v-model="search" align="right" placeholder="输入地点或机型进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
            !search || data.pos.toLowerCase().includes(search.toLowerCase()) || data.type.toLowerCase().includes(search.toLowerCase())
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
    <com-pagination align="right"></com-pagination>
  </div>
</template>

<script>
import ComTableECabinet from "@/components/ComTableECabinet.vue";
import ComPagination from "@/components/ComPagination.vue";
export default {
  components: {
    ComTableECabinet,
    ComPagination,
  },
  data() {
    return {
      editForm: {},
      addEdit: true,
      dialogForm: false,
      label: {
        id: "电柜ID",
        pos: "位置",
        type: "型号",
        num: "插槽数目",
      },
      form: {
        id: "",
        pos: "",
        type: "",
        num: "",
      },
      tableData: [
        {
          id: "1001",
          pos: "曹安公路4800号",
          type: "哈喽A1000",
          num: "12",
        },
      ],
      search: "",
    };
  },

  methods: {
    clearForm() {
      setTimeout(() => {
        this.form = {
          id: "",
          pos: "",
          type: "",
          num: "",
        };
        this.addEdit = true;
      }, 200);
    },
    saveForm(bool, form) {
      this.dialogForm = bool;
      if (this.addEdit) {
        this.tableData.push(form);
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
      console.log(index, row);
    },
    handleDelete(index, row) {
      this.tableData.splice(index, 1);
      console.log(index, row);
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