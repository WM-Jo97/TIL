# For문

    -> Dictionary 는 iterable
    
    for문과 딕셔너리 함께 사용하기
        for 키 변수 in 딕셔너리 :

```
grades = {'peter':  80, 'jake': 90}
for key in grades:
    print(key,':',grades[key])

# enumerate함수
    -> 단어 뜻은 열거하다.
        List, Tuple, String 등의 자료형을 받아서
        인덱스 값을 포함하는 enumerate 객체를 돌려준다

    -> 반복문을 사용할 때 리스트의 순서값, 즉 인덱스의 정보가 필요한 경우
        enumerate함수는 리스트의 원소에 순서값을 부여해주는 함수.

**    
enumerate 함수는 그냥 print 값을 찍으면 나오지 않음.
list(enumerate)를 하면 순서와 값이 나오는 것 확인 가능
```
