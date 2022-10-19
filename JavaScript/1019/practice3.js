const numbers = [90, 80, 70, 100]

const sumNum = numbers.reduce((result,number) => {return result + number }, 0)
const avgNum = numbers.reduce((result,number) => {return result + number }, 0)/numbers.length


console.log(sumNum)
console.log(avgNum)