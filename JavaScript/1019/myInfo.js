const jsonData = {
    coffee : 'Americano',
    iceCream : 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson)

// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)
console.log(jsonToObj.coffee)