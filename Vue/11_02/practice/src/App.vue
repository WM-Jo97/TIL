<template>
  <div id="app">
    <h1>이곳은 App.vue 입니다.</h1>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld 
      static-props = 'SSAFY 여러분을 응원합니다!'
    />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
