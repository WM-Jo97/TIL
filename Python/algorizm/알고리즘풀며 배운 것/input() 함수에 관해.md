# input() 함수 주의사항

## iuput() 함수는 
다음 줄로 넘어가는 기능이 있다.

----
    ex) 1
        2
        3

    을 입력한다고 가정하면

``` 
    print(input())
    print(input())
    print(input())
```
위 코드만으로

    1
    2
    3

을 얻어낼 수 있다.

가령

    1  ---> T (테스트 횟수)
    2  ---> 리스트 A의 요소 갯수
    1 2---> 리스트 A의 요소
    3  ---> 리스트 B의 요소 갯수
    1 2 3 --> 리스트 B의 요소
처럼 리스트를 만드는 코드를 짜고 싶다면

```
T=int(input())

for i in range(1,T+1):
    num= input()
    A = list(input().split())
    print(A) 
```
으로 간단하게 만들 수 있음.

