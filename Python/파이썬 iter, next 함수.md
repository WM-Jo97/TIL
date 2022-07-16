# Iter() 함수와 Next() 함수

## Iterable 한 객체와 Iterator 객체
----

### Iterable 하다 = 반복 가능하다

    - 반복 가능한 객체
        string, list, tuple,dict,set,range()
        파일, class로 컬렉션 데이터로 정의된 객체

        '반복 가능한' 객체는 한 시점에 해당 
        element(또는 member) 하나하나를 
        리턴할 수 있으며 
        "for member in iterable_객체"
        로 처리가능

### Iterator란?
----
    Iterable 한 객체가 Iter()함수를 통하여
    "Iterator 객체"로 생성된 것.

    --> Iter() 함수는 적용 시 데이터타입이
    iterator라는 새로운 타입으로 생성됨.

### Iterator 특성
---
    iter() 함수로 만든 iterator 객체는 
    한번에 하나하나씩 element 혹은 member를
    순서대로 엑세스할 수 있는 객체.

    for문에서는 set 또는 ranga()와 같이 
    형 변환없이 자체적으로는 인덱싱이 불가능한
    데이터 타입도 있으므로, 불편함

    Iterator는 순서대로 자료를 가져온 이후에
    그 데이터는 폐기해버리기 때문에, 메모리 사용에 제약이 따르는 경우 데이터처리에 효과적    

``` 
    #사용예제

    x = ['Python', 'Java', 'C']
    iter_x = iter(x)
    for data in iter_x :
        print(data0)

결과 :  Python
        Java
        C
```

    주의 : Iterator 객체는 일반적인 데이터 타입과 
    달리, 인덱싱 또는 len()과 같은 기능은 제공되지 않음.

    -> Iterator는 해당 문을 벗어나면 재사용 불가