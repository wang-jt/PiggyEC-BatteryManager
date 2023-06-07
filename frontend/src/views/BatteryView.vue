<template>
  <div class="user">
    <div class="add-search">
      <el-button v-if="$root.$guser == 'admin'"
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
      <el-dialog :visible.sync="dialogVisible" title="取用电瓶" width="30%">
        <el-form ref="linkform" :model="linkform" label-width="100px">
          <el-form-item label="选择ECycle">
            <el-select v-model="linkform.ecid" style="width: 200px">
              <el-option
                v-for="ecycle in ecycles.filter(
                (data) =>
                  data.isUsing == '否' && data.type == linkform.type
              )"
                :key="ecycle.id"
                :label="ecycle.id + '-' + ecycle.type"
                :value=ecycle.id
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <el-button @click="handleLinkClose">取 消</el-button>
        <el-button type="primary" @click="handleLinkSuccess">确 定</el-button>
      </el-dialog>
      <!--  -->
      <el-input v-model="search" align="right" placeholder="输入型号进行搜索" />
    </div>
    <el-table
      class="table"
      :data="
        tableData.filter(
          (data) =>
           ( !search || data.size.includes(search) ) && ($root.$guser == 'admin' || data.status.includes('待装配'))
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
          <el-button size="mini" @click="handleLink(scope.$index, scope.row)" v-if="$root.$guser != 'admin'" style="background-color: #7fe8a2; color: #FFFFFF;"
            >取用</el-button
          >
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)" v-if="$root.$guser == 'admin'"
            >编辑</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)" v-if="$root.$guser == 'admin'"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <com-pagination align="right" :total="this.tableData.length"></com-pagination>
  </div>
</template>

<script>
import ComTable from "@/components/ComTableBattery.vue";
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
        size: "类型",
        powerLeft: "剩余电量",
        status: "状态",
        curpos: "当前位置",
      },
      form: {
        id: "",
        size: "",
        powerLeft: "",
        status: "",
        masterSlotId: null,
        curECycleId: null,
      },
      tableData: [
        
      ],
      search: "",
      dialogVisible:false,
      linkform: {
        ecid: null,
        btid: null,
        type: null,
      },
      ecycles: [],
    };
  },
  created() {
    this.tableData = reqAPI('GET',`/battery/getallbattery`, null).tableData;
    console.log(this.tableData);
  },

  methods: {
    clearForm() {
      this.tableData = reqAPI('GET',`/battery/getallbattery`, null).tableData;
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
        reqAPI('POST',`/battery/editbattery/${form.id}`, form);
      } else{
        reqAPI('POST',`/battery/addbattery`, form);
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
      reqAPI('POST',`/battery/deletebattery/${row.id}`, null);
      this.tableData = reqAPI('GET',`/battery/getallbattery`, null).tableData;
    },
    handleLink(index, row) {
      this.linkform.btid = row.id;
      this.linkform.type = row.size;
      this.ecycles = reqAPI('GET',`/ecycle/${this.$root.$guser}`, null).tableData;
      this.dialogVisible = true;
    },
    handleLinkSuccess() {
      reqAPI('POST',`/battery/link,${this.linkform.btid},${this.linkform.ecid}`, null);
      this.dialogVisible = false;
      this.linkform.ecid = null;
      this.tableData = reqAPI('GET',`/battery/getallbattery`, null).tableData;
    },
    handleLinkClose() {
      this.dialogVisible = false;
      this.linkform.ecid = null;
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