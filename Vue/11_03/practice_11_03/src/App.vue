<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div id="shadow">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div id="table">
        <table class="tab">
          <tr>
            <td v-for="(time, index) in times.slice(0,8)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>
            </td>
          </tr>
          <tr>
            <td v-for="(time, index) in times.slice(8,16)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>         
            </td>
          </tr>
          <tr>
            <td v-for="(time, index) in times.slice(16,24)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>
            </td>
          </tr>
          <tr>
            <td v-for="(time, index) in times.slice(24,32)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>
            </td>
          </tr>
          <tr>
            <td v-for="(time, index) in times.slice(32,40)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>
            </td>
          </tr>
          <tr>
            <td v-for="(time, index) in times.slice(40,48)" :key=index>
              <button :id=time class="light" @click="click_btn">{{time}}</button>
            </td>
          </tr>
        </table>
      </div>
      <hr>
      <h3> 선택시간 : <span v-for="(time,index) in selected_time" :key=index> {{ time }} </span> </h3>
    </div>
  </div>
  
    
</template>

<script>

export default {
  name: 'App',
  data : function(){
    return{
      times : ['00:00','00:30','01:00','01:30','02:00','02:30','03:00','03:30',
      '04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30',
      '10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00',
      '14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30',
      '19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00',
      '23:30'],
      selected_time : []
    }
  },
  methods: {
    click_btn :function(data){
      if(this.selected_time.includes(data.target.innerText)){
        const i = this.selected_time.indexOf(data.target.innerText)
        this.selected_time.splice(i,1)
        data.target.className='light'
      }else{
        if(this.selected_time.length<5){
          this.selected_time.push(data.target.innerText)
          data.target.className='blue'
        }else{
          alert("시간을 5개 이상 선택했습니다.")
        }
      }
      
      console.log(data.target)
      data.target.class = "b_tn"
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
#table {
  margin: 0 auto;
}
.tab{
  margin: 0 auto;
}
.light{
  background-color: white;
  border: none;
}
.blue{
  border: none;
  background-color: #658dc63d;
  color: #0f4c81;
}
#shadow{
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  width: 30%;
  margin: 0 auto;
  padding: 1%;
}
</style>
