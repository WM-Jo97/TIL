<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos : {{ allCount }} </h2>
    <h2>Completed Todos : {{ allCompletedCount }} </h2>
    <h2>Uncompleted Todos : {{ unCompeletedCount }} </h2>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed :{
    allCount(){
      return this.$store.getters.getAllCount
    },
    allCompletedCount(){
      return this.$store.getters.getAllCompletedCount
    },
    unCompeletedCount(){
      return this.$store.getters.getUncompletedCount
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
