// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log(nums[i])
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

/* 
(a) = let 과 const 로 변수를 생성할 수 있지만 const 를 사용할 경우 재할당이 불가능하기 때문에 i가 변할 수 없음
	    const를 let으로 바꿔주면 i가 변할때마다 i를 재할당할 수 있으므로 let으로 바꿔줘야 함,
*/


// 2번
for (num in nums) {
  num = parseInt(num)
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

// string을 num 으로 바꿔주는 parseInt()를 이용하여 변환