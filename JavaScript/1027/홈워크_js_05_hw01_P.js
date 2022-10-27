axios
.(a)('https://api.example.com/data')

.(b)(function (response) {
	console.log((c))
})

a = get
b = then
c = response.data

동기함수로 함수를 작성하면 함수가 완료될때까지 동작이 멈추지만
비동기 함수를 이용하면 웹api에 동작을 보내놓고 다른 작업을 한 후
비동기 함수의 동작이 완료되면 표시하는 것이 가능해진다.