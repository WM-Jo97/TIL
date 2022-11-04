<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model="childData"
    @input="sendData">
    <h3>AppParentData : {{parentData}}</h3>
    <h3>AppData : {{ appData }} </h3>
    <h3>AppChildData : {{ childData }} </h3>
  </div>
</template>

<script>
export default {
    name : 'AppChild',
    props : {
        parentData:String,
        appData : String,
    },
    data:function(){
        return{
            childData : null
        }
    },
    methods : {
        sendData : function() {
            this.$emit('child-data', this.childData)
        }
    }
}
</script>

<style>

</style>