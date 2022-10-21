let line = 5
let result = ""


// 5층을 찍고, 2씩 증가 = 별의 갯수
for (let i = 1; i < line * 2; i+= 2) {
    // 공백찍기
    for (let j = 1; j<(line*2 -i) / 2; j++) {
        result += " "
    }
    for (let k = 1; k<=i ; k++) {
        result += "*"
    }
    // 줄바꿈
    result += "\n"
}

console.log(result)
