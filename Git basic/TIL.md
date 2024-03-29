

<details>
<summary>토글 접기/펼치기</summary>
<div markdown="1">

안녕

</div>
</details>

Python Basic 
    1) Python 특징
    * 인터프리터 언어 -> 컴파일러 언어에 비해 상대적으로 속도는 느리지만 프로그래밍이 용이함
    * 타 언어에 비해 문법이 간결하고 유연
    2) 객체 지향 프로그래밍
      -> 프로그래밍에는 객체지향과 절차 지향 프로그래밍이 존재함.
         일반적으로 실생활에 쓰는 모든 것을 객체라고 하며, 객체지향 프로그래밍이란
         프로그램에 필요한 객체를 파악하고, 각각의 객체들의 역할이 무엇인지 정의하여 객체들 간의 
         상호작용을 통해 프로그램을 만드는 것.

         객체(Object)는 클래스라는 틀에서 생겨난 실체(Instance)임

         객체지향 프로그램은 객체와 객체간의 연결로 이루어져있으며, 객체 안에 자료구조와 알고리즘 있음.

       * 객체 지향 vs 절차 지향 프로그래밍
        -> 객체 지향 : 누가 어떤 일을 할 것 인가?
             * 대형 프로그래밍은 많은 기능을 수반하므로 객체 지향에 적합
  
           절차 지향 : 어떤 절차를 통해 일을 할 것 인가?
             * 소형 프로그래밍의 경우 적은 기능을 수반하므로 프로그래밍이 용이한 절차 지향이 적합
  
       * 객체지향 프로그래밍 특징
        1. 추상화
          * 객체들의 공통적 특징을 도출하는 것
          * 객체 지향적 관점에서는 클래스를 정의하는 것 : 추상화
        2. 캡슐화 
          * 구현되는 부분을 외부에 드러내지 않도록 정보를 은닉
          * 객체가 독립적 역할을 할 수 있도록 데이터와 기능을 하나로 묶어 관리
          * 외부와 상호작용할 때 메소드를 활용
        3. 상속성
          * 하나의 클래스가 가진 특성을 다른 클래스가 그대로 물려받을 수 있음
          * 이미 작성된 클래스를 받아 새로운 클래스를 생성
          * 기존 코드를 재활용하여 생산력 향상
        4. 다형성
          * 약간 다른 방법으로 동작하는 함수를 동일한 이름으로 호출
          * 동일한 명령의 해석을 연결된 객체에 의존
          * 오버라이딩(Overriding) : 부모클래스의 메소드와 같은 이름을 사용하며 매개변수도 같되 내부 소스를 재정의하는 것
          * 오버로딩(Overloading) : 같은 이름의 함수를 여러 개 정의한 후 매개변수를 다르게 하여 같은 이름을 경우에 따라 호출하여 사용하는 것
        5. 동적바인딩
          * 함수를 호출하면 동적 바인딩을 통해 파생 클래스에 오버라이딩된 함수가 실행
          * 프로그래밍의 유연성을 높여주며 파생 클래스에서 재정의한 함수의 호출을 보장
      
      -> 객체 지향 프로그래밍의 장점
        1. 소프트웨어 생산성 향상
        2. 현실 세계에 대한 모델링 용이
        3. 보안성 향상

      -> 객체 지향 프로그래밍의 단점
        1. 느린 실행 속도 (캡슐화와 격리구조 때문에 절차지향에 비해 느림)
        2. 객체지향에서는 모든 것을 객체로 생각하므로 메모리와 연산에 비용 소모
        3. 설계 시 작은 규모의 프로젝트의 경우 절차지향에 비해 복잡


Python 기본 문법
    1. 들여쓰기(Space Sensitive)
      -> 문장을 구분할 때, 중괄호대신 들여쓰기 사용
         들여쓰기는 4칸 띄우기 혹은 Tap
         Tap과 4칸 띄워쓰기 혼용금지, 한가지 종류로만 사용
         원칙적으로는 공백(빈칸)을 권장
    
    2. 주석 (Comment)
      -> 코드를 보다 이해하기 쉽게하여 분석 및 수정이 용이
         주석은 코드에 영향을 줒 않으며, 개발 간 편의를 위해 사용
        한줄 주석 : #
        여러줄 주석 : ''' ~~ '''

        주석 단축키 : 컨트롤 + /
    
    3. 변수(Variable)
      -> 데이터를 저장하기 위해 사용
         변수를 사용하면 복잡한 값을 쉽게 사용할 수 있음
         동일 변수에 다른 데이터를 언제든 할당(저장) 가능
        
        변수의 할당 => 변수(Variable) = 값 (Value)
        
        각 변수의 값을 바꿔서 저장 -> pythonic한 방법 => x, y = y, x

        식별자
          변수 이름 규칙
           1. 식별자의 이름은 영문 알파벳 , 언더스코어(_) , 숫자로 구성
           2. 첫 글자에 숫자가 올 수 없음
           3. 길이 제한이 없고 대소문자를 구분
           4. 파이썬에 미리 예약된 예약어는 사용 불가
           5. 내장 함수나 모듈 등의 이름도 사용하지 않아야 함

    4. 연산자
      -> 기본적인 사칙연산에 사용
          + : 덧셈
          - : 뺄셈
          * : 곱셈
          / : 나눗셈
          // : 몫
          ** : 제곱
          % : 나머지

    5. 자료형 
      -> Python에서 사용할 수 있는 데이터의 Type
         
         (Data Type)  _ Boolean Type    _ Int
                     |                 |
                     |_ Numeric Type __|_ Float
                     |                 |
                     |_ String Type    |_ Complex

      1) Numeric Type (수치형 자료형)
        ㄱ) Int (정수)
            -> 진수표현 가능 (2진수 : 0b, 8진수 : 0o , 16진수 : 0x )
        ㄴ) Float (실수 자료형)
            -> 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
            (3.2 - 3.1 = 0.100000000000009)

            -> 부동소수점 때문 (Floating point rounding error)
             * 컴퓨터는 2진수를 사용하여 10진수 0.1은 2진수로 표현하면 01.00011001100110.... 으로
             * 무한대로 반복, 무한대 숫자를 그대로 저장할 수 없어 근사값만 표시
             * 매우 작은 수를 이용하여 비교하거나 math 모듈을 이용하여 해결 가능

      2) String Type (문자열 자료형)
        -> 모든 문자는 Str tpye
           작은 따옴표 ' 또는 큰 따옴표 " 를 이용하여 표기
           '우리는 "하나"' 또는 "우리는 '하나'" 와 같이 중첩하여 사용 가능
        
        * Escape sequence
          역슬래시 \ 뒤에 특정 문자가 와서 기능을 하는 문자
            \n : 줄바꿈
            \t : 탭
            \r : 캐리지 리턴
            \0 : null
            \\ : \
            \' : '
            \" : "
        
        * 문자열 연산
          "A" + "B" = "AB"
          "A" * 3 = "AAA"

        * f-string : print(f'Hello, {name}! 성적은 {score}')
            -> name = A , score = 80 일 때, 츨력값은 Hello, A! 성적은 80

      3) None
        -> 값이 없음을 표현하기 위해 None 타입 존재
           일반적으로 반환 값이 없는 함수에서 사용하기도 함

      4) Boolean 
        -> True 와 False를 값으로 가지며 참과 거짓을 표현
        
        * 비교 연산자
          < , > : 초과, 미만
          <=, >= : 이상, 이하
          == : 동일
          != : 같지 않음
          is : 객체 아이덴티티 (OPP)
          is not : 객체 아이덴티티가 아닌 경우 
        
        * 논리 연산자
          and = 둘 모두 True일 때, True
          or = 둘 중 하나만 True 면 True
          Not = True -> False , False -> True
          -> not, and, or 순으로 우선순위가 높음

        * Falsy : False는 아니지만 False로 취급되는 값
          -> 0, 0.0 , () , [], {}, None, ""
    
    6. 컨테이너
      -> 여러 개의 값을 담을 수 있는 객체, 서로 다른 자료형을 저장할 수 있음
         컨테이너는 순서가 있는 Ordered Data 와 순서가 없는 Unordered Data로 구분
         (순서가 있다 = 정렬되어 있다는 의미는 아님)

        컨테이너 분류                        __ 리스트
                                           |
                     __ 시퀀스형 (순서 o) __|__ 튜플
                    |                      |
        Container   |                      |__ 레인지
                    |
                    |__ 비시퀀스형 (순서 x) ____ 세트
                                            |
                                            |__ 딕셔너리
      
      1) 시퀀스형
        ㄱ) 리스트 : 여러 개의 값을 순서가 있는 구조로 저장하고싶을 때 사용
            -> 어떤 자료형도 저장 가능, 생성된 후 내용 변경 가능
               인덱스를 이용해 데이터에 접근 가능
        ㄴ) 튜플 : 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
            -> 리스트와 달리 담고 있는 값은 변경 불가능, 인덱스로 접근은 가능
               단일 항목의 경우 : 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙임
               복수 항목의 경우 : 마지막에 쉼표는 없어도 되지만, 넣는 것을 권장
               튜플 대입 -> x,y = 1, 2 라는 변수 선언은 실제로는 튜플로 처리
                           x,y = (1, 2)

        ㄷ) 레인지 : 숫자의 시퀀스를 나타내기 위해 사용, 주로 반복문과 함께 사용
            -> range(n) : 0~ n-1 까지의 숫자
               range(n,m) : n ~ m-1 까지의 숫자
               range(n, m, s) : n ~ m-1 까지 s씩 증가

        * 슬라이싱 연산자 : 시퀀스를 특정 단위로 슬라이싱 가능
          * 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음
          * 리스트, 튜플, range, 문자열에 사용가능
          * [n : m] -> n번쨰 ~ m-1 번째
          * [n : m : k] -> n ~ m-1 까지 k간격으로 슬라이싱

      2) 비시퀀스형
        ㄱ) 셋 : 중복되는 요소 없이, 순서에 상관없는 데이터의 묶음
                 순서가 없으므로 인덱스를 통한 접근 불가능
                 수학에서 집합을 표현한 컨데이너
                 담고있는 요소를 삽입, 변경, 삭제 가능 (mutable 자료형)

            * 셋 연산자 
              * | : 합집합
              * & : 교집협
              * - : 차집합
              * ^ : 대칭차집합 
        ㄴ) 딕셔너리 : 키 - 값 (key - value) 쌍으로 이루어진 자료형
            key 는 변경 불가능한 (immutable) 자료형만 활용 가능
            * string, integer, float, boolean, tuple, range

            value 는 모든 데이터 사용 가능

    7. 형변환
      -> 파이썬에서 데이터 형태는 서로 변환할 수 있음
        1) 암시적 형변환 : 사용자가 의도하지 않고 파이썬 내부적으로 자료형을 변환 (bool, int, float)
                    
        2) 명시적 형변환 : 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 (int, float, str )