import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isCollapse: false,
    tagList: [{
      icon: "el-icon-menu",
      title: "首页",
      path: "/home"
    }]
  },
  getters: {},
  mutations: {
    clickCollapse(state) {
      state.isCollapse = !state.isCollapse
    },
    clickMenu(state, tag) {
      if (tag.title !== '首页') {
        const result = state.tagList.findIndex(item => item.title === tag.title)
        if (result === -1) {
          state.tagList.push(tag)
        }
      }
    },
    closeTag(state, tag) {
      const result = state.tagList.findIndex(item => item.title === tag.title)
      console.log(result)
      state.tagList.splice(result, 1)
    }
  },
  actions: {},
  modules: {}
})