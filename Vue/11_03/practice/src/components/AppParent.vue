<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model ='parentData' @input="sendData" >
    <h3> AppData : {{ appData }} </h3>
    <h3> AppChildData : {{ childData }} </h3>
    <AppChild 
    :app-data="appData"
    :parent-data ="parentData"
    @child-data ="getChild"/>
  </div>
  
</template>

<script>
import AppChild from '@/components/AppChild'
export default {
    name : 'AppParent',
    components : {
        AppChild,
    },
    props:{
        appData : String
    },
    data:function(){
      return {
        parentData : null,
        childData : null,
      }
    },
    methods: {
        getChild : function(data) {
            this.childData = data
            this.$emit('send-child', data)
        },
        sendData : function() {
            this.$emit('parent-data', this.parentData)
        }
    }
}
</script>

<style>

</style>