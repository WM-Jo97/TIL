const products = [
    {name : 'cucumber' , type : 'vegetable'},
    {name : 'carrot', type : 'vegitable'},
    {name : 'apple', type : 'fruit' },
    {name : 'orange', type : 'fruit'}
]

const newArry = products.filter((products) => {
    return products.type === 'fruit'
})

console.log(newArry)