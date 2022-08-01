# CSS position
    문서 상에서 요소의 위치를 지정
    static


    1. relative : 상대 위치
        자기 자신의 static 위치를 기주능로 이동 (normal flow 유지)
        레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)

    2. absolute : 절대 위치
        요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (nomal flow에서 벗어남)
        static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)

    3. fixed : 고정 위치
        요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (nomal flow에서 벗어남)
        부모 요소와 관곙벗이 viewport를 기준으로 이동
            스크롤 시에도 항상 같은곳에 위치

    4. sticky : 스크롤에 따라 static -> fixed 로 변경
        속성을 적용한 박스는 평소에 문서 안에서 position : static 상태와 같이 일반적인 흐름에 따르지만
        스크롤 위치가 임계점에 이르면 position : fixed와 같이 박스를 화면에 고정할 수 있는 속성

## CSS 원칙 1,2 : Normal flow
    모든 요소는 네모(박스모델), 좌측 상단에 배치
    display에 따라 크기와 배치가 달라짐

## CSS 원칙 3
    position으로 위치의 기준을 변경
        relative : 본인의 원래 위치
        absolute : 특정 부모의 위치
        fixed : 화면의 위치
        sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경



우선순위, 실습 꼭 해보기!

상속부분

