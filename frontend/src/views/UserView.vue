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
      <el-input v-model="search" align="right" placeholder="输入姓名进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
            !search || data.name.toLowerCase().includes(search.toLowerCase())
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
import ComTable from "@/components/ComTable.vue";
import ComPagination from "@/components/ComPagination.vue";
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
        name: "姓名",
        age: "年龄",
        sex: "性别",
        date: "日期",
        address: "地址",
      },
      form: {
        name: "",
        age: "",
        sex: "",
        date: "",
        address: "",
      },
      tableData: [
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
        {
          name: "冯秀英",
          age: 25,
          sex: "女",
          date: "1994-10-25",
          address: "山西省-运城市-临猗县",
        },
        {
          name: "龙伟",
          age: 35,
          sex: "男",
          date: "1985-10-25",
          address: "云南省-玉溪市-红塔区",
        },
        {
          name: "谭杰",
          age: 15,
          sex: "男",
          date: "2003-06-13",
          address: "江西省-九江市-都昌县",
        },
        {
          name: "夏丽",
          age: 7,
          sex: "女",
          date: "2015-01-25",
          address: "上海-上海市-奉贤区",
        },
      ],
      search: "",
    };
  },

  methods: {
    clearForm() {
      setTimeout(() => {
        this.form = {
          name: "",
          age: "",
          sex: "",
          date: "",
          address: "",
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