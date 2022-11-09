import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    catImg : null,
  },
  getters: {
    catImage(state){
      return state.catImg
    }
  },
  mutations: {
    SAVE_CAT_IMAGE(state,catImg){
      state.catImg = catImg
    }
  },
  actions: {
    getCatImage(context){
      const catUrl = "https://api.thecatapi.com/v1/images/search"
      axios({
        url: catUrl,
        method : 'get',
      })
      .then(response => {
        const catImg = response.data[0].url
        context.commit('SAVE_CAT_IMAGE', catImg)
      })
      .catch(error=>{
        console.log(error)
      })
    }
  },
  modules: {
  }
})
