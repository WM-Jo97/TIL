# 2. CSS
    CSS는 스타일을 지정하기 위한 언어

CSS는 선택자와 선언, 속성, 값으로 이루어져 있다.

    1. CSS구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
    2. 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
    3. 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
        속성(Property) : 어떤 스타일 기능을 변경할지 결정
        값 (Value) : 어떻게 스타일 기능을 변경할지 결정

CSS 정의 방법
    인라인 (inline) -> 인라인을 쓰게되면 실수가 잦아짐
    내부 참조 (embedding) - <style> -> 코드가 너무 길어짐
    외부 참조 (link file) - 분리된 CSS 파일 -> 가장 많이 쓰는 방식

## CSS Selector
    기본 선택자
        전체 선택자, 요소 선택자
        클래스 선택자, 아이디 선택자, 속성 선택자

    결합자 (Combinators)
        자손 결합자, 자식 결합자
        일반 형제 결합자, 인접 형제 결합자
    
    의사 클래스/요소 (Pseudo Class)
        링크, 동적 의사 클래스
        구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

    * : 전체 선택자
    h2 : 요소 선택자
    .green : 클래스 선택자
    #purpel : id 선택자
    .box > p : 자식 선택자
    .box p : 자손 선택자

## CSS 적용 우선순위 (cascading order)
    CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.
        1. 중요도 (Importance) -> 사용 시 주의
            !important
        2. 우선순위 (Specifictiy)
            인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
        3. CSS 파일 로딩 순서

## CSS 상속
    CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
        속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
        상속 되는것 예시
            Text 관련 요소 (font, color, text-align), opacity, visibility 등
        상속 되지 않는 것 예시
            Box model 관련 요소 (width, height, margin, padding, border, box-sizing, display),
            position 관련 요소 (position, top/right/bottom/left, z-index) 등

##  CSS 기본 스타일
    PX(픽셀) : 모니터 해상도의 한 화소인 픽셀 기준
               픽셀의 크기는 변하지 않기 때문에 고정적인 단위
    % : 백분율 단위, 가변적인 레이아웃에서 주로 사용
    
    em : (바로위, 부모 요소에 대한) 상속의 영향을 받음
    배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

    rem : (바로위, 부모요소에 대한) 상속의 영향을 받지 않음
          최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

    viewport : 웹 페이지에 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 양약 (디바이스 화면)
               디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
               vw, vh, vmin, vmax

    --> px는 브라우저의 크기를 변경해도 그대로  <---> vw는 브라우저의 크기에 따라 크기가 변함

## 색상 단위
    색상 키워드 (background-color : red;)
        대소문자를 구분하지 않음
        red, blue, black 과 같은 특정 색을 직접 글자로 나타냄

    RGB 색상 (background-color: rgb(0,255,0);)
        16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
        # + 16진수 표기법 (color : #000;) 
                          (color : #000000;)
        rgb() 함수형 표기법 (rgb(0, 0 ,0);)
        rgba() 표기법 (a는 투명도 alpha) (rgba(0,0,0,0.5))

    HSL 색상 (background-color: hsl(0,100%,50%);)
        색상, 채도, 명도를 통해 특정 색을 표현하는 방식

        hsl() 표기법 : hsl(0,100%,50%);
        hsla() 표기법 : hsla(120, 100% 0.5)
    
# Selector 심화
    결합자 (Combinatiors)
        자손 결합자(공백)
             selectorA 하위의 모든 selectorB
        
        자식 결합자 (>)
            selectorA 바로 아래의 selectorB 

        일반 형제 결합자(~)
            selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소를 모두 선택

        인접 형제 결합자(+)
            selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택