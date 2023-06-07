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
        <div class="num">
          <el-card
            v-for="(item, index) in countData"
            :key="index"
            shadow="always"
            body-style="padding: 0;display: flex;"
          >
            <i
              :class="'el-icon-' + item.icon"
              :style="'background:' + item.color"
            ></i>
            <ul>
              <li>
                ￥<span>{{ item.value }}</span>
              </li>
              <li>{{ item.name }}</li>
            </ul>
          </el-card>
        </div>
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
        name: "品牌",
        todayBuy: "今日购买",
        monthBuy: "本月购买",
        totalBuy: "总购买",
      },
      tableData: [
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
        {
          name: "巴黎世家",
          todayBuy: 1450,
          monthBuy: 7500,
          totalBuy: 85000,
        },
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
    };
  },
  created() {
    this.userinfo = reqAPI('GET',`/getUserInfo/${this.$root.$guser}`, null).userInfo;
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
        data: ["猜想", "预期", "实际"],
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
        name: "月份",
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
          "1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月",
        ],
      },

      yAxis: {
        name: "人次",
        type: "value",
        min: 0, // 配置 Y 轴刻度最小值
        max: 4000, // 配置 Y 轴刻度最大值
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
          name: "猜想",
          data: [454, 226, 891, 978, 901, 581, 400, 543, 272, 955, 1294, 1581],
          type: "line",
          symbolSize: function (value) {
            // 点的大小跟随数值增加而变大
            return value / 150;
          },
          symbol: "circle",
          itemStyle: {
            normal: {
              label: {
                show: true,
              },
              lineStyle: {
                color: "rgba(0,0,0,0)", // 折线颜色设置为0，即只显示点，不显示折线
              },
            },
          },
        },

        {
          name: "预期",
          data: [
            2455, 2534, 2360, 2301, 2861, 2181, 1944, 2197, 1745, 1810, 2283,
            2298,
          ],
          type: "line",
          symbolSize: 8, //设置折线上圆点大小
          itemStyle: {
            normal: {
              label: {
                show: true, // 在折线拐点上显示数据
              },
              lineStyle: {
                width: 3, // 设置虚线宽度
                type: "dotted", // 虚线'dotted' 实线'solid'
              },
            },
          },
        },

        {
          name: "实际",
          data: [
            1107, 1352, 1740, 1968, 1647, 1570, 1343, 1757, 2547, 2762, 3170,
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
        text: "营业总收入季度分布图",
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
        data: ["一季度", "二季度", "三季度", "四季度"],
      },
      dataset: {
        source: [
          ["quarter", "一季度", "二季度", "三季度", "四季度"],
          ["完美世界", 25.74, 25.7, 29.18, 21.58],
        ],
      },
      series: [
        {
          name: "完美世界",
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
        text: "本月售卖情况",
      },
      color: ["#9462e5", "#e1bb22"],
      tooltip: {},
      legend: {
        data: ["销量", "退货"],
      },
      xAxis: {
        data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
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
          name: "销量",
          type: "bar",
          data: [550, 120, 336, 110, 430, 420],
        },
        {
          name: "退货",
          type: "bar",
          data: [155, 20, 36, 30, 90, 140],
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