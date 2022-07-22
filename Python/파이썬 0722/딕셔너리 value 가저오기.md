A라는 딕셔너리가 있을 때 

주로 value 값을 가져오기 위해서는
A['a'] = 'a의 value' 을 이용한다.

하지만 A 딕셔너리 안에 없는 C라는 수를 부르면
A['c'] 

==> Traceback (most recent call last):
        File"<stdin>", line 1, in <module>
    KeyError: 'c'

위와 같은 오류가 발생한다.


이때 get함수를 이용하면 조금 더 발전된 기능도 사용 가능

get(key, default값)

---> 딕셔너리에 key가 있으면 해당 key 에 대한 값을 반환하고,
     key가 없으면 default에 지정한 값을 반환한다.

     default에 값을 설정하지 않으면 아무값도 반환하지 않는다.


딕셔너리.setdefault(key,default) 함수도 존재하는데
    이 함수는 값이 없을 경우 딕셔너리에 키와 벨류를 지정할 수도 있다.

A = { a : 1 , b : 2 } 라는 딕셔너리가 있을 때
A.setdefault(c,3)을 입력하면

A = { a : 1, b : 2, c : 3} 이 된다.

만약 값이 있는데 setdefault를 실행하면?

A.setdefault(a.4)
----> 디폴트 위치의 인자는 무시하고
a의 value인 1이 출력된다.