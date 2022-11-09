<template>
    <div> 
      <span 
        @click="updateTodoStatus"
        :class="{ 'is-completed' : todo.isCompleted }"
      > {{ todo.title }} </span>
      <button @click="deleteTodo">x</button>
    </div>
</template>

<script>
export default {
    name : 'TodoListItem',
    props: {
        todo : Object,
    },
    methods:{
        deleteTodo(){
            //console.log(this.todo)
            this.$store.dispatch('deleteTodo', this.todo)
        },
        updateTodoStatus(){
            this.$store.dispatch('updateTodoStatus', this.todo)
        }
    }
}
</script>

<style>
    .is-completed{
        text-decoration: line-through;
    }
</style>