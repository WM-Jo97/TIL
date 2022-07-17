# 문자열 포멧팅

## 문자열 포멧팅은
    달력을 출력한다고 가정하면

``` 
    print(2022년 1월)    
    print(2022년 2월)
    print(2022년 3월)   
```
     대신
```
    month = 1
    while month <= 12:
        print(f'2022년 {month0}월')
        month = month+1
```
    로 작성할 수 있음.

## F 스트링
----
    f-sting 포메팅은 %포메팅과 str.format
    방법보다 더 최근에 나온 것

    f-string은 f와 {}만 보면 됨.
        문자열 맨앞에 f를 붙여주고
        중괄호 안에 직접 변수 이름이나 출력하고
        싶은 것을 바로 넣으면 사용가능
    
    형식 : f'문자열 {변수} 문자열'

### f-string과 자리 정렬
 ---
 왼쪽 정렬
 ```
    s1 = 'left'
    result1 = f'{s1:<10>}'
    print(result1)
 ```
 가운데 정렬
 ```
    s2 = 'mid'
    result1 = f'{s2:^10>}'
    print(result2)
 ```
 오른쪽 정렬
 ```
    s3 = 'right'
    result1 = f'{s3:>10>}'
    print(result3)  
 ```  

 F-string은 반드시 마스터해놓자!!