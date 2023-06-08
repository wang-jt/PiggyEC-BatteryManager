<template>
  <div>
    <div id="map" style="height: 810px;"></div>
  </div>
</template>

<script>
import { BMPGL } from "@/bmpgl.js"
import { reqAPI } from "@/request"
export default {
  data() {
    return {
      map: '',
      mapZoom: 17,
      data: [],
    }
  },
  created() {
    this.data = reqAPI('GET', '/cabinet/getallcabinet', null).tableData;
    this.data.forEach((item) => {
      item.contain = reqAPI('GET', `/slot/getcabinetslot/${item.id}`, null).tableData
    })
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
        this.data.forEach((item) => {
          var point = new BMapGL.Point(parseFloat(item.locx),parseFloat(item.locy));
          var myicon = new BMapGL.Icon('/1.png', new BMapGL.Size(40, 40));
          var marker = new BMapGL.Marker(point, {icon: myicon}); // 创建标注
          this.map.addOverlay(marker); // 将标注添加到地图中

          var labeldesc = '';
          var i = 0;
          item.contain.forEach((slot) => {
            labeldesc = `电瓶类型：${slot.type} 可用:${slot.usedNum}/${slot.maxNum}`
            const label = new BMapGL.Label(labeldesc, {
              position: point, // 文本绑定的点位位置
              offset: new BMap.Size(-60, -40 - 18*i) // 文本位置移动
            })
            label.setStyle({
              display: 'block',
              border: '0px',
              backgroundColor: '#ffffff'
            })
            this.map.addOverlay(label)
            i = i + 1;
          });

          
        })
          /*
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
          */
        
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