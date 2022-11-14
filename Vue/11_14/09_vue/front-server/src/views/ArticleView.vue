<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name : 'CreateView' }">Create</router-link>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList
  },
  computed:{
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>
