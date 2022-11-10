<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <nav>
      <router-link to="/"><button>Home</button></router-link> |
      <router-link :to="{name:'NocolorView'}"><button>Start</button></router-link>
    </nav>
    <router-view/>
  </div>
</template>

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

</style>
