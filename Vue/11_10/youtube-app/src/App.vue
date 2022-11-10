<template>
  <div id="app">
    <SearchBar/>
    <VideoDetail/>
    <VideoList/>
  </div>
</template>

<script>
import VideoList from '@/components/VideoList'
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
export default ({
  name : 'app',
  components: {
    SearchBar,
    VideoList,
    VideoDetail
  },
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
