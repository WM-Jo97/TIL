<template>
  <div id="app">
    <hr>
    <h1>Cat Image</h1>
    <button @click="getCat">Get Cat</button>
    <p>{{ catImage }}</p>
    <div v-show="catImage">
      <img :src="catImage" alt="cat image">
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  methods :{
    getCat(){
      this.$store.dispatch('getCatImage')
      console.log('업데이트되었습니다.')
    }
  },
  computed: {
    catImage(){
      return this.$store.getters.catImage
    }
  }
}
</script>

<style>
#app {
 
}
</style>
