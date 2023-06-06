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
      mapZoom: 16
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
        // 初始化地图,设置中心点坐标和地图级别
        this.map.centerAndZoom(new BMapGL.Point(121.220631,31.291873), this.mapZoom)
        // 设置地图显示的城市 此项是必须设置的
        this.map.setCurrentCity('上海')
        // 启用滚轮放大缩小，默认禁用
        this.map.enableScrollWheelZoom(true)
        // 启用地图惯性拖拽，默认禁用
        this.map.enableContinuousZoom(true)
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