import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    todos: [
    ]
  },
  getters: {
    allTodosCount(state){
      return state.todos.length
    },
    completedTodosCount(state){
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted == true
      })
      return completedTodos.length
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem){
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index,1)
    },
    UPDATE_TODO_STATUS(state, todoItem){
      //const index = state.todos.indexOf(todoItem)
      //state.todos(index).isCompleted = !state.todos[index].isCompleted
      state.todos = state.todos.map((todo)=>{
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
         }
        return todo
      })
    },
    //LOAD_TODOS(state){
    //  const localStorageTodos = localStorage.getItem('todos')
    //  const parsedTodos = JSON.parse(localStorageTodos)
    //  state.todos = parsedTodos.todos
    //}
  },
  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted : false,
      }
      context.commit('CREATE_TODO',todoItem)
      //context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO',todoItem)
      //context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context,todoItem){
      context.commit('UPDATE_TODO_STATUS',todoItem)
      //context.dispatch('saveTodosToLocalStorage')
    },
    //saveTodosToLocalStorage(context){
    //  const jsonTodos = JSON.stringify(context.state.todos)
    //  localStorage.setItem('todos',jsonTodos)
    //},
    //loadTodos(context){
    //  context.commit('LOAD_TODOS')
    //}
  },
  modules: {
  }
})
