import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    result : [

    ],
    detail : null
  },
  getters: {
  },
  mutations: {
    SEARCH(state,response){
      state.result= response.data.items
    },
    DETAIL(state,data){
      state.detail = data
    }
  },
  actions: {
    search(context, searchword){
      axios.get(`https://www.googleapis.com/youtube/v3/search?key=AIzaSyCNVjy9R0rsOE105h5Uaz5liCMdPL2x0r8&part=snippet&type=video&q=${searchword}`)
      .then((response)=>{
        context.commit('SEARCH', response)
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    goToDetail(context, data){
      console.log(data)
      context.commit('DETAIL',data)
    }
  },
  modules: {
  }
})
