<template>
  <div>
    <VideoListItem
      v-for="(result,index) in results"
      :key="index"
      :result="result"
    />
  </div>
  
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name : 'VideoList',
  components: {
    VideoListItem
  },
  computed: {
    results(){
      return this.$store.state.result
    }
  }
}
</script>

<style>

</style>