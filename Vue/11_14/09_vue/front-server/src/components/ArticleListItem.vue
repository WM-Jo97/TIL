<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <router-link :to="{ name : 'DetailView', params : {id : article.id} }">[Detail]</router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props : {
    article : Object
  }
}
</script>

<style>

</style>
