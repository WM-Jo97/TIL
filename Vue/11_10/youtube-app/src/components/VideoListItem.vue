<template>
  <div @click="goToDetail">
    <ul>
      <li>
        <div>
          <span><img :src="thumbUrl" alt=""></span>
          <h3> {{ videoTitle }} </h3>
        </div>
      </li>
    </ul>

      
  </div>
  
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    result : Object,
  },
  computed: {
    videoTitle(){
      return this.result.snippet.title
    },
    videoDesc(){
      return this.result.snippet.description
    },
    thumbUrl(){
      return this.result.snippet.thumbnails.medium.url
    }
  },
  methods:{
    goToDetail(){
      const data = this.result
      this.$store.dispatch('goToDetail',data)
    }
  }
}
</script>

<style>

</style>