<template>
  <div class = "border">
    <h1>새롭게 시작하는 새로운 컴포넌트!</h1>
    <MyComponentItem 
        static-props="MyComponent에서 보낸 데이터"
        :dynamic-props = "dynamicProps"
        num-props = "1"
        @give-me-ma-money = "parentGetEvent"
        @child-input = "getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentItem from "@/components/MyComponentItem"

export default {
    name : 'MyComponent',
    components : {
        MyComponentItem,
    },
    data: function(){
        return{
            dynamicProps : '이것은 동적인 프롭스!!@',
        }
    },
    methods: {
        parentGetEvent : function(childdata) {
            console.log(childdata)
            console.log('용돈 ㄴㄴ')
        },
        getDynamicData : function(childInputData) {
            console.log(`사용자가 입력한 값은 ${childInputData} 입니다.`)
        }
    }
}
</script>

<style>
    .border {
        border : solid 1px black;
    }
</style>