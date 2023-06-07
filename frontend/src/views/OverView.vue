<template>
  <div>
    <div id="map" style="height: 810px;"></div>
  </div>
</template>

<script>
import { BMPGL } from "@/bmpgl.js"
export default {
  data() {
    return {
      map: '',
      mapZoom: 17
    }
  },
  created() {
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
        this.map.centerAndZoom(new BMapGL.Point(121.220631,31.291873), this.mapZoom)// 初始化地图,设置中心点坐标和地图级别
        this.map.enableScrollWheelZoom(true)// 启用滚轮放大缩小，默认禁用
        this.map.enableContinuousZoom(true)// 启用地图惯性拖拽，默认禁用

        var point = new BMapGL.Point(121.220631,31.291873);
        var marker = new BMapGL.Marker(point); // 创建标注
        this.map.addOverlay(marker); // 将标注添加到地图中
        var opts = {
            width: 200, // 信息窗口宽度
            height: 60, // 信息窗口高度
            title: "下楼做核酸了", // 信息窗口标题
        };
        var infoWindow = new BMapGL.InfoWindow(
            `<p>快点的吧，还有再做三天</p><img src="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4wB6C?ver=dddf" width="50%"
            >`,
            opts
        ); // 创建信息窗口对象
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