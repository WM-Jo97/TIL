<template>
  <div>
    <h1>Lunch</h1>
    <button @click="selectmenu">Pick Lunch</button>
    <h2>{{pickmenu}}</h2>
    <div v-if="pickmenu" >
      <button @click="picklotto">Lotto 뽑으러 가기</button>
    </div>
    
  </div>
</template>

<script>

export default {
  name: 'LunchView',
  data(){
    return {
      menu : ['비빔냉면', '물냉면', '돈까스', '비빔밥', '순두부찌개' ],
      pickmenu : null
    }
  },
  methods: {
    selectmenu(){
      const rannum = Math.floor(Math.random()*this.menu.length)
      console.log(this.menu[rannum])
      this.pickmenu = this.menu[rannum]
    },
    picklotto(){
      //const sendmenu = this.pickmenu
      this.$router.push({ name:'LottoView' ,params: {menu : this.pickmenu}})
    }
  }
}
</script>
