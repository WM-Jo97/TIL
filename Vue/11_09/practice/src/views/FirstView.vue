<template>
  <div>
    <HelloWorld
     msg = '첫번째 메세지입니다.'/>
  </div>
  
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name : 'FisrtView',
  components: {
    HelloWorld,
  },
}
</script>

<style>

</style>