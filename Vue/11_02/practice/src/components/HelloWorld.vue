<template>
  <div class="hello">
    <hr>
    <h2>이곳은 HelloWorld 입니다.</h2>
    <h3>{{ staticProps }}</h3>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    staticProps: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
