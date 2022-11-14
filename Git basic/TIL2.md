Python 기본문법2

1. 제어문

 -> 특정 상황에 따라 코드를 선택적으로 실행하거나 반복 실행하기 위해 사용
    제어문은 순서도(Flowchart)로 표현 가능

  1) 조건문
    참/ 거짓에 따라 분기가 나뉨
    if 조건 == True:
        분기 1
    else:
        분기 2

    ㄱ) 복수 조건문
        복수의 조건문은 elif를 이용해서 표현
        if 조건:
            분기 1
        elif 조건:
            분기 2
        elif 조건:
            분기 3
        else:
            분기 4

    ㄴ) 중첩 조건문
        조건문 안데 다른 조건문을 중첩해서 사용할 수 있음
        if 조건:
            if 조건:
                분기 1-1
            else:
                분기 1-2
        eles:
            분기 2
    
    ㄷ) 조건 표현식
        조건에 따라 값을 정할 때 활용
        삼항 연산자로도 불림
        'true인 경우 값 if 조건 else false인 경우 값'
        
        ex) X= A
        Y = A if type(X)==int else Y = B
        => Y = B

  2) 반복문
    특정 조건을 만족할 때까지 반복

    ㄱ) while문 : 종료 조건에 해당하는 코드를 통해 종료

    ㄴ) for문 : 반복 가능한 객체롤 모두 순회하면 자동 종료

        -> break, continue, for-else 등을 통해 제어 가능

        *List Comprehension : 표현식과 제어문을 통해 리스트를 간결하게 생성
            ex) [code for 변수 in iterable if 조건식]

    ㄷ) 반복문 제어
      * break : 반복문을 종료
      * continue : 이후 코드 블록은 수행하지 않고 다음 반복을 수행
      * for-else : 끝까지 반복문을 실행한 후 else문 실행
        (break를 통해 중간에 종료되면 else문은 실행되지 않음)
      * pass : 아무것도 하지 않음

2. 함수

  -> 함수는 Decomposition(분해), Abstracion(추상화)가 가장 큰 키워드
     Decomposition : 기능을 분해하고 재사용 가능하게 하기
     Abstraction : 복잡한 내부 정보를 모르더라도 사용 가능하게 하기


  1) 함수의 종류

    * 내장함수 : 파이썬에 기본 내장된 함수
    * 외장함수 : import문을 통해 외부 라이브러리에서 불러온 함수
    * 사용자 정의 함수 : 사용자가 직접 만든 함수               

  2) 함수의 정의
    
    * 함수(Function)
     - 특정한 기능을 하는 코드의 조각
     - 특정 코드를 매번 다시 작성하지 않고 필요시에만 호출하여 간편하게 사용
    
    * 기본 구조
     def name(data, parameters):
        ~~~~
        ~~~~
        return answer

    * 선언과 호출 (define & call)
     - 함수의 선언은 def 키워드를 활용함
     - 들여쓰기를 통해 Function body를 작성
     - 함수는 parameter를 넘겨줄 수 있음
     - 함수는 동작후에 return을 통해 결괏값을 전달함
  
  3) 함수의 결과값(Outout)
    
    *Void function
      명시적인 return 값이 없는 경우, None을 반환하고 종료
    
    *Value returning function
      함수 실행 후, return문을 통해 값 반환
      return을 하게 되면, 값 반환 후 함수가 바로 종료

    *print vs return
      print함수와 return의 차이점
      -> print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
      -> 데이터 처리를 위해서는 return 사용

  4) 함수의 입력(Input)
    
    *Parameter 와 Argument
     - Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
     - Argument : 함수를 호출할 때, 넣어주는 값
       ->함수 호출 시 함수의 parameter를 통해 전달되는 값
         Argument는 소괄호 안에 할당 func_name(argument)
         * 필수 Argument : 반드시 전달되어야 하는 argument
         * 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달

        Argument는 위치에 따라, 직접 값을 지정하여, default 값을 미리 지정해서 사용

  5) 가변인자 (*args)

    *가변인자 : 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
      -> 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

    *패킹, 언패킹
     -> 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
     -> 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
     -> 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
     -> 언패킹시 왼쪽의 변수에 * 를 붙이면 할당하고 남은 요소를 리스트에 담을 수 있음

     * 는 스퀀스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자

  6) 가변 키워드 인자 (**kwargs)

    * 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    * **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현


Python Scope
  
1. Python의 범위(Scope)
  
  함수는 코드 내부에 local scope를 생성
  그 이외의 공간은 global scope 로 구분

  scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
  
  variale 
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

2. Lifecycle (변수 수명주기)
  
  built-in scope
   - 파이썬이 실행된 이후부터 영원히 유지
  global scope 
   - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  local scope
   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

3. 이름 검색 규칙 (Name Resolution)
  
  LEGB Rule
    - Local scope : 지역 범위 (현재 작업중인 범위)
    - Enclosed scope : 지역 범위 한 단계 위 범위
    - Global scope : 최상단에 위치한 범위
    - Built-in scope : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)

  global 문
    - 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
        global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
        global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함.

  nonlocal
    - global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
        nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
        nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/ 함수등으로 정의되지 않아야 함.
    - global과는 달리 이미 존재하는 이름과의 연결만 가능함

4. 함수의 범위 주의
  
  - 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
  - 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색
      변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
      값을 할당하는 경우, 해당 scope의 이름공간에 새롭게 생성됨
      단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용
  - 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
      단, 코드가 복잡해지면 변수의 변경을 추적하기 어렵고, 예기치 못한 오류 발생
      가급적 사용하지 않는 것을 권장

5. 함수 응용
  
  - map : 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수 적용하고, 
          그 결과를 map Object로 반환
  - filter : 순회 간으한 데이터 구조의 모든 요소에 함수를 적용하고, 결과가
             True인 것들을 filter Object로 반환

  - zip : 복수의 iterable을 모아 튜플을 원소로 하는 zip objet를 반환

  - lambda : lambda[parameter] : 표현식
             람다 함수 : 표현식을 계산한 결과값을 반환하는 함수로, 
                        이름이 없는 함수여서 익명함수로도 불림
             특징 : return문을 가질 수 없음
                    간편 조건문 외 조건문이나 반복문을 가질 수 없음
             장점 : 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
                    def를 사용할 수 없는 곳에서도 사용 가능
  - 재귀 함수(recursive function)
      * 자기 자신을 호출하는 함수
      * 1개 이상의 종료되는 상황을 주고 수렴하도록 작성
      * 재귀 함수는 base case에 도달할 때까지 함수를 호출, 메모리 스택이 넘치면 프로그램 중지
      * 파이썬의 최대 재귀 깊이는 1000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

6. 모듈 
  
  1) 모듈과 패키지
    
    모듈 : 다양한 기능을 하나의 파일로
      -> 특정 기능을 하는 코드를 파이썬 파일 단위로 작성
    
    패키지 : 다양한 파일을 하나의 폴더로
      -> 특정 기능과 관련된 여러 모듈의 집합
      -> 패키지 안에는 또 다른 서브 패키지를 포하

    라이브러리 : 다양한 패키지를 하나의 묶음으로

    이 모든것을 관리하는 관리자 : pip
    패키지의 활용 공간 : 가상환경

  2)  
