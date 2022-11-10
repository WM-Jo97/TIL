<template>
    <div v-if="videoDetail" id="video">
        <iframe :src="getUrl">
        </iframe>
        <h3>{{ title }}</h3>
        <p>{{ description }}</p>
    </div>
    
</template>

<script>
export default {
  name: 'VideoDetail',
  data(){
    return{
      data : null
    }
  },
  computed: {
    videoDetail(){
        return this.$store.state.detail
    },
    getUrl(){
        return `https://www.youtube.com/embed/${this.$store.state.detail.id.videoId}`
    },
    description(){
        return this.$store.state.detail.snippet.description
    },
    title(){
        return this.$store.state.detail.snippet.title
    },
  }
}
</script>

<style>
  #video {
  padding: 10px;

  }
</style>