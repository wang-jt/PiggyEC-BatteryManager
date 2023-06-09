<template>
  <div class="home">
    <el-row :gutter="20">
      <!--  -->
      <el-col :span="8">
        <el-card shadow="hover">
          <div slot="header" class="user-info">
            <img class="user-img" src="@/assets/user.png" />
            <ul>
              <li>{{ $root.$guser }}</li>
              <li v-if="$root.$guser === 'admin'">管理员</li>
              <li v-else>用户</li>
            </ul>
          </div>
          <ul class="login-info">
            <li>性别：<span>{{ userinfo.gender }}</span></li>
            <li>年龄：<span>{{ userinfo.age }}</span></li>
          </ul>
        </el-card>
        <el-card class="table" shadow="always">
          <el-table :data="tableData" style="width: 100%">
            <el-table-column
              v-for="(val, key) in label"
              :key="key"
              :prop="key"
              :label="val"
            >
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
      <!--  -->
      <el-col :span="16">
        
        <el-card style="width: 100%; height: 300px; margin-bottom: 20px">
          <div id="line"></div>
        </el-card>
        <div class="bar-pie">
          <el-card style="width: 49%; height: 300px">
            <div id="bar"></div>
          </el-card>
          <el-card style="width: 49%; height: 300px">
            <div id="pie"></div>
          </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { reqAPI } from "@/request";
import * as echarts from "echarts";

export default {
  data() {
    return {
      userinfo: null,
      label: {
        id: "租赁电瓶",
        pos: "所属车辆",
        size: "型号",
        powerLeft: "剩余电量",
      },
      tableData: [
        
      ],
      countData: [
        {
          name: "今日支付订单",
          value: "1234",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "今日收藏订单",
          value: "210",
          icon: "star-on",
          color: "#ffb980",
        },
        {
          name: "今日未支付订单",
          value: "1234",
          icon: "s-goods",
          color: "#5ab1ef",
        },
        {
          name: "本月支付订单",
          value: "1234",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "本月收藏订单",
          value: "210",
          icon: "star-on",
          color: "#ffb980",
        },
        {
          name: "本月未支付订单",
          value: "1234",
          icon: "s-goods",
          color: "#5ab1ef",
        },
      ],
      data: null,
      slotData: [],
    };
  },
  created() {
    this.userinfo = reqAPI('GET',`/getUserInfo/${this.$root.$guser}`, null).userInfo;
    this.tableData = reqAPI('GET',`/getallmybattery/${this.$root.$guser}`, null).tableData;
    this.data = reqAPI('GET', '/cabinet/getallcabinet', null).tableData;
    this.data.forEach((item) => {
      item.usedNum = 0;
      item.contain = reqAPI('GET', `/slot/getcabinetslot/${item.id}`, null).tableData
      item.contain.forEach((i) => {
        i.name = i.id + '号槽';
        item.usedNum += i.usedNum;
        this.slotData.push(i);
      })
    })
    //console.log('slotdata',this.slotData)
  },
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    var bar = echarts.init(document.getElementById("bar"));
    var pie = echarts.init(document.getElementById("pie"));
    var line = echarts.init(document.getElementById("line"));
    // 绘制图表
    line.setOption({
      title: {
        text: "共享电柜使用人次表",
        // subtext: 'Demo 虚构数据',
        x: "center",
      },
      legend: {
        // 图例配置选项
        orient: "horizontal", //图例布局方式：水平 'horizontal' 、垂直 'vertical'
        x: "left", // 横向放置位置，选项：'center'、'left'、'right'、'number'（横向值 px）
        y: "top", // 纵向放置位置，选项：'top'、'bottom'、'center'、'number'（纵向值 px）
        data: ["实际"],
      },
      grid: {
        // 图表距离边框的距离，可用百分比和数字（px）配置
        top: "20%",
        left: "3%",
        right: "10%",
        bottom: "5%",
        containLabel: true,
      },

      tooltip: {
        // tooltip 用于控制鼠标滑过或点击时的提示框（下一章展开讲）
        trigger: "axis",
        axisPointer: {
          // 坐标轴指示器配置项。
          type: "cross", // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
          axis: "auto", // 指示器的坐标轴。
          snap: true, // 坐标轴指示器是否自动吸附到点上
        },
        showContent: true,
      },
      toolbox: {
        // 右上角的工具框（下一章展开讲）
        feature: {
          saveAsImage: {}, //下载按钮
        },
      },

      xAxis: {
        name: "日期",
        type: "category",
        axisLine: {
          lineStyle: {
            // X 轴颜色配置
            color: "#3366CC",
          },
        },
        axisLabel: {
          rotate: 45, // X 轴标签文字旋转角度
          interval: 0, //设置 X 轴数据间隔几个显示一个，为0表示都显示
        },
        boundaryGap: false, //数据从 Y 轴起始
        data: [
          "6.1",
          "6.2",
          "6.3",
          "6.4",
          "6.5",
          "6.6",
          "6.7",
          "6.8",
        ],
      },

      yAxis: {
        name: "人次",
        type: "value",
        min: 0, // 配置 Y 轴刻度最小值
        max: 30, // 配置 Y 轴刻度最大值
        splitNumber: 7, // 配置 Y 轴数值间隔
        axisLine: {
          lineStyle: {
            // Y 轴颜色配置
            color: "#3366CC",
          },
        },
      },

      series: [
        {
          name: "实际",
          data: [
            11, 13, 17, 19, 16, 15, 13, 17, 25, 27, 3170,
            3665,
          ],
          type: "line",
          symbol: "circle", // 实心圆点
          smooth: 0.5, // 设置折线弧度
        },
      ],
      color: ["#3366CC", "#FFCC99", "#99CC33"], // 三个折线的颜色
    });
    pie.setOption({
      title: {
        left: "center",
        text: "可用电瓶分布图",
        textStyle: {
          color: "#6d6",
        },
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      tooltip: {},
      legend: {
        left: "left",
        top: "10",
        orient: "vertical",
        data: this.data.map((item) => item.name),
      },
      dataset: {
        source: [
          ['quarter'].concat(this.data.map((item) => item.name)),
          ["value"].concat(this.data.map((item) => item.usedNum)),
        ],
      },
      series: [
        {
          name: "电柜",
          type: "pie",
          seriesLayoutBy: "row",
          encode: {
            itemName: 0, //数据项名称，在legend中展示
            value: 1,
          },
          label: {
            show: true,
          },
          // roseType: "area", //设置玫瑰图
        },
      ],
    });
    bar.setOption({
      title: {
        text: "重点电柜插槽情况表",
      },
      color: ["#9462e5", "#e1bb22"],
      tooltip: {},
      legend: {
        data: ["已使用", "未使用"],
      },
      xAxis: {
        data: this.slotData.map((item) => item.name),
      },
      yAxis: {
        axisLine: {
          show: true, //显示y轴最左边边框线
        },
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      series: [
        {
          name: "已使用",
          type: "bar",
          data: this.slotData.map((item) => item.usedNum),
        },
        {
          name: "未使用",
          type: "bar",
          data: this.slotData.map((item) => item.maxNum - item.usedNum),
        },
      ],
    });
    window.addEventListener("resize", function () {
      // 让我们的图表调用 resize这个方法
      bar.resize();
      line.resize();
      pie.resize();
    });
  },
};
</script>

<style lang="scss" scoped>
.home {
  width: 100%;
  height: 100%;
  .user-info {
    display: flex;
    align-items: center;
    .user-img {
      width: 150px;
      height: 150px;
      border-radius: 100%;
      margin-right: 40px;
    }
    & li:nth-child(1) {
      font-size: 30px;
    }
    & li:nth-child(2) {
      margin-top: 10px;
      font-size: 16px;
      color: rgb(153, 153, 153);
    }
  }
  .login-info {
    font-size: 14px;
    color: rgb(153, 153, 153);
    li {
      margin: 5px;
      span {
        margin-left: 50px;
      }
    }
  }
  .table {
    margin-top: 30px;
  }
  .num {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    .el-card {
      width: 32%;
      height: 90px;
      margin-bottom: 20px;
      border: none;
      i {
        width: 90px;
        height: 100%;
        line-height: 90px;
        text-align: center;
        font-size: 30px;
        color: #fff;
      }
      ul {
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-left: 20px;
        li:nth-child(1) {
          font-size: 30px;
          color: #000;
          margin-bottom: 5px;
        }
        li:nth-child(2) {
          font-size: 15px;
          color: rgb(148, 148, 148);
        }
      }
    }
  }
  #line {
    width: 100%;
    height: 280px;
  }
  .bar-pie {
    width: 100%;
    display: flex;
    justify-content: space-between;

    #pie {
      width: 100%;
      height: 280px;
    }
    #bar {
      width: 100%;
      height: 280px;
    }
  }
}
</style>