import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos : [
      
    ]
  },
  getters: {
    getTodos(state){
      return state.todos
    },
    getAllCount(state){
      return state.todos.length
    },
    getAllCompletedCount(state){
      const completed = state.todos.filter((todo)=>{
        return todo.isCompleted == true
      })
      return completed.length
    },
    getUncompletedCount(state){
      const uncompleted = state.todos.filter((todo)=>{
        return todo.isCompleted == false
      })
      return uncompleted.length
    }
  },
  mutations: {
    CREATE_TODO(state,todoItem){
      state.todos.push(todoItem)
    },
    DELETE_TODO(state,todoItem){
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state,todoItem){
      const index = state.todos.indexOf(todoItem)
      if(state.todos[index].isCompleted){
        state.todos[index].isCompleted = false
      }else{
        state.todos[index].isCompleted = true
      }
    }
  },
  actions: {
    createTodo(context, todoTitle){
      const todoItem = {
        title : todoTitle,
        isCompleted : false,
      }
      context.commit('CREATE_TODO',todoItem)
    },
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO',todoItem)
    },
    updateTodoStatus(context, todoItem){
      context.commit('UPDATE_TODO_STATUS',todoItem)
    },
    saveLocalStorage(context){
      const jsonData = JSON.stringify(context.state.todos)
      localStorage.setItem('todos',jsonData)
    },
    loadLocalStorage({ commit }){
      const jsonData = localStorage.getItem('todos')
      const data = JSON.parse(jsonData)
      commit('LOAD_TODOS',data)
    }
    
  },
  modules: {
  }
})
