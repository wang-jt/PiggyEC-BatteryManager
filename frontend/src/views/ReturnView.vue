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
      <el-dialog :visible.sync="dialogVisible2" title="归还电瓶" width="30%">
        <el-form ref="linkform" :model="linkform" label-width="100px">
          <el-form-item label="选择ECycle">
            <el-select v-model="linkform.ecid" style="width: 200px">
              <el-option
                v-for="ecycle in ecycles.filter(
                (data) =>
                  data.isUsing == '是' && data.parameter == linkform.type
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
          <el-button size="mini" @click="handleLink(scope.$index, scope.row)" v-if="$root.$guser != 'admin'" style="background-color: #ee6267; color: #FFFFFF;"
            >归还</el-button
          >
          <el-button size="mini" @click="handleShow(scope.$index, scope.row)" style="background-color: #409EFF; color: #FFFFFF;">
            查看</el-button
          >
          <el-button size="mini" @click="" style="background-color: #7fe8a2; color: #FFFFFF;">
            定位</el-button
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
    <el-dialog :visible.sync="dialogVisible" title="电瓶详情" width="30%">
      <el-table :data="slotData" style="width: 100%">
        <el-table-column prop="id" label="ID"></el-table-column>
        <el-table-column prop="size" label=" "></el-table-column>
        <el-table-column prop="powerLeft" label="剩余电量"></el-table-column>
        <el-table-column prop="status" label="状态"></el-table-column>
      </el-table>
    </el-dialog>
    <com-pagination align="right" :total="this.tableData.length"></com-pagination>
  </div>
</template>

<script>
import ComTable from "@/components/ComTableSlot.vue";
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
        type: "类型",
        maxNum: "最大电瓶容量",
        usedNum: "当前电瓶容量",
        masterName: "所属电柜名",
      },
      form: {
        id: "",
        type: "",
        maxNum: "",
        usedNum: "",
        pos: "",
        masterName: "",
      },
      tableData: [
        
      ],
      search: "",
      slotData: [],
      dialogVisible: false,
      dialogVisible2: false,
      linkform: {
        ecid: null,
        btid: null,
        type: null,
        stid: null,
      },
      ecycles: [],
    };
  },
  created() {
    this.tableData = reqAPI('GET',`/slot/getallslot`, null).tableData;
    console.log(this.tableData);
  },
  methods: {
    clearForm() {
      this.tableData = reqAPI('GET',`/slot/getallslot`, null).tableData;
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
        reqAPI('POST',`/slot/editslot/${form.id}`, form);
      } else{
        reqAPI('POST',`/slot/addslot`, form);
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
      reqAPI('POST',`/slot/deleteslot/${row.id}`, null);
      this.tableData = reqAPI('GET',`/slot/getallslot`, null).tableData;
    },
    handleShow(index, row){
      this.slotData = reqAPI('GET',`/battery/getslotbattery/${row.id}`, null).tableData;
      this.dialogVisible = true;
    },
    handleLink(index, row) {
      this.linkform.stid = row.id;
      this.linkform.type = row.type;
      this.ecycles = reqAPI('GET',`/ecycle/${this.$root.$guser}`, null).tableData;
      this.dialogVisible2 = true;
    },
    handleLinkSuccess() {
      this.linkform.btid = reqAPI('GET',`/getecycle/${this.linkform.ecid}`, null).tableData.btid;
      console.log('success', this.linkform.btid);
      reqAPI('POST',`/battery/unlink,${this.linkform.btid},${this.linkform.stid}`, null);
      this.dialogVisible2 = false;
      this.linkform.stid = null; this.linkform.btid = null; this.linkform.type = null; this.linkform.ecid = null;
      this.tableData = reqAPI('GET',`/slot/getallslot`, null).tableData;
    },
    handleLinkClose() {
      this.dialogVisible2 = false;
      this.linkform.stid = null; this.linkform.btid = null; this.linkform.type = null; this.linkform.ecid = null;
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