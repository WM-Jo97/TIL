<template>
  <div>
    <h1> {{ menu }}먹고 로또 추첨하기 </h1>
    <button @click="lotto">Pick Numbers</button>
    <p>{{lottonum}}</p>
    <router-link to="/">처음으로</router-link>
  </div>
  
</template>

<script>
export default {
  name : 'LottoView',
  data(){
    return{
        menu : this.$route.params.menu,
        lottonum : null
    }
  },
  methods:{
    lotto(){
      function lottonumber(){
        let lotto = []
        for(let i=0; i<6; i++){
          let n = Math.floor(Math.random()*45)+1;
          lotto.push(n)
        }
        lotto.sort(function(a,b){
          return a-b
        })
        return lotto
      }
      const lotton = lottonumber()
      this.lottonum = lotton
    },
  }
}
</script>

<style>

</style>