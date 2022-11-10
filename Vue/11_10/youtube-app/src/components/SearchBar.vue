<template>
  <div>
    <h1> Youtube 영상을 검색해보자 </h1>
    <input type="text"
     v-model="searchword"
     @keyup.enter="search"
    >
  </div>
  
</template>

<script>
//import VideoList from '@/components/VideoList.vue'
export default {
  name : 'SearchBar',
  components: {
    //VideoList,
  },
  data(){
    return{
      searchword : null,
    }
  },
  methods:{
    search(){
      if(this.searchword){
        this.$store.dispatch('search',this.searchword)
      }
      this.searchword = null
    }
  }
}
</script>

<style>

</style>