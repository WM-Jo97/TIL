<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <h3>ParentData : {{ parentData }}</h3>
    <h3>ChildData : {{ childData }} </h3>
    <AppParent :app-data ="appData"
    @parent-data = getParentData
    @send-child = getChild
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data:function(){
    return {
      appData : null,
      parentData : null,
      childData : null
    }
  },
  methods:{
    getParentData : function(data){
      this.parentData = data
    },
    getChild : function(data){
      this.childData = data
    }
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
