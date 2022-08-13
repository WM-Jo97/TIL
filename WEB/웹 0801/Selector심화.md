# 결합자 (Combinators)
    자손 결합자(공백)
        selectorA 하위의 모든 selectorB 요소
    자식 결합자(>)
        selectorA 바로 아래의 selectorB 요소
    일반 형제 결합자(~)
        selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
    인접 형제 결합자(+)
        selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

## CSS 원칙
    모든 요소는 네모(박스모델)이고
    위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다

## Box model
    모든 HTML 요소는 box형태로 되어있음
    하나의 박스는 네 부분(영역)으로 이루어짐
        margin : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다.
        border : 테두리 영역
        padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지는 padding까지 적용
        content : 글이나 이미지 등 요소의 실제 내용

## Box model 구성 (marginm, padding)
    .margin{
        margin-top: 10px;
        margin-right:20px;
        margin-bottom:30px;
        margin-left:40px;
    }

    margin shorthand를 통해서도 표현 가능
    margin 1 : 상하좌우
    margin 2 : 상하, 좌우
    margin 3 : 상, 좌우, 하
    margin 4 : 상, 하, 좌, 우

## Box sizing
    .box{
        width : 100px;
        margin : 10px auto;
        padding : 20px;
        border : 1px solid black:
        background-color : blueviolet;
        color : white;
        text-align : center;
    }

    기본적으로 모든 요소의 box-sizing은 content-box
        padding을 제외한 순수 contents 영역만을 box로 지정
    다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px로 보는 것을 원함
        그 경우 box-sizing을 border-box로 설정

## css 원칙 2
    모든 요소는 네모(박스모델)이고, 좌측 상단에 배치
     display에 따라 크기와 배치가 달라진다.

    대표적으로 활용되는 display
    display : block    ---> 한줄을 다 차지하는 테트리스
        줄바꿈이 일어나는 요소
        화면 크기 전체의 가로 폭을 차지
        블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

    display : inline   ---> 글자처럼 취급
        줄바꿈이 일어나지 않는 행의 일부 요소
        content 너비만큼 가로 폭을 차지한다
        wodth, height, margin-top, margin-bottom을 지정할 수 없다.
        상하 여백은 line-height로 지정한다.

    블록 레벨 요소와 인라인 레벨 요소 구분
    대표적인 블록 레벨 요소
        div/ ul,ol,li / p / hr / form 등
    
    대표적인 인라인 레벨 요소
        span / a/ img / input, label / b,em, i, strong 등

## 속성에 따른 수평 정렬
    margin-right : auto; (오른쪽 정렬)
    
    margin-left : auto; (왼쪽 정렬)

    margin-right : auto;(가운데 정렬)
    margin-left : auto;

    none(다시 보여줄 일 없을 때) <-> hidden(보여줄 일 있을 때)