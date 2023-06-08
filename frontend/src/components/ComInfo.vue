<template>
  <div>
    <div id="map" style="height: 810px;"></div>
  </div>
</template>

<script>
import { BMPGL } from "@/bmpgl.js"
import { reqAPI } from "@/request"
export default {
  props: {
    data:{
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      map: '',
      mapZoom: 17,
    }
  },
  watch: {
    data: {
      handler() {
        this.initMap();
      },
      deep: true,
    },
  },
  created() {
    console.log('created cominfo!', this.data);
    this.$nextTick(() => {
      this.initMap()
    })
  },
  methods: {
  	// 初始化
  	initMap() {
      console.log('initMap')
      BMPGL().then((BMapGL) => {
        this.map = new BMapGL.Map('map')
        var item = this.data;
        this.map.centerAndZoom(new BMapGL.Point(parseFloat(item.locx),parseFloat(item.locy)), this.mapZoom)// 初始化地图,设置中心点坐标和地图级别
        this.map.enableScrollWheelZoom(true)// 启用滚轮放大缩小，默认禁用
        this.map.enableContinuousZoom(true)// 启用地图惯性拖拽，默认禁用
        var point = new BMapGL.Point(parseFloat(item.locx),parseFloat(item.locy));
        var marker = new BMapGL.Marker(point); // 创建标注
        this.map.addOverlay(marker); // 将标注添加到地图中
        var opts = {
            width: 200, // 信息窗口宽度
            height: item.contain.length*30, // 信息窗口高度
            title: item.id + '-' + item.name, // 信息窗口标题
            'background-color': 'red',
        };
        var infoDesc = '<div>';
        item.contain.forEach((slot) => {
            infoDesc += `<div><span>${slot.type}</span> 当前状态:${slot.usedNum}/${slot.maxNum}</div>`
          } );
        infoDesc += '</div>';
        var infoWindow = new BMapGL.InfoWindow(infoDesc,opts); // 创建信息窗口对象
        this.map.openInfoWindow(infoWindow, point);
        this.map.addEventListener("click", (e) => {
          console.log(e)
          this.map.openInfoWindow(infoWindow, point);
        });
      })
  }
}
}

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