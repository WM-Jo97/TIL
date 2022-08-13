# CSS layout techniques

## css 원칙
    모든 요소는 네모(박스모델)이고 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다

## Float
    박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping하도록 함
    요소가 nomal flow를 벗어나도록 함

## Float 속성
    none : rlqhsrkqt
    left : 요소를 왼쪽으로 띄움
    right : 오소를 오른쪽으로 띄움


## Flexbox 
    Float 가 과거에 많이 활용한 방법인 반면 최근에는 Flexbox 사용
    행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

    축 
        main axis (메인 축)
            (꼬치라고 생각할 수 있음)
        cross axis (교차 축)
            (꼬치와 수직이 되는 축)

    구성요소
        Flex Contaniner (부모 요소)
        Flex Item (자식 요소)
    
    Ie 부분지원 -> 인터넷 익스플로어에 부분적으로만 지원도미

    FLEX는 정렬을 원하는 아이템에 설정하는 것이 아니라
    부모요소인 Container에 적용해야함

    Inline-flex -> 컨테이너들을 수평으로 놓을 수 있도록 해줌

## Flex 속성

    배치 설정
        flex-direction
        flex-wrap
    공간 나누기
        justify-content(main axis)
        align-content (cross axis)
    정렬
        align-items (모든 아이템을 cross axis 기준으로)
        align-self (개별 아이템)

### flex-wrap
    아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치하기 위해 끼워 맞추는 대신
    wrap을 사용하면 줄바꿈 가능

    wrap-reverse를 이용해 상하 전환 가능

### justify-content
    Main axis를 기준으로 공간 배분
    1) flex-start -> 왼쪽 정렬
    2) flex-end -> 오른쪽 정렬
    3) center -> 가운데 정렬
    4) space-between -> 늘여쓰기
    5) space-around -> 1:2:2:1 형식
    6) space-evenly -> 공백 같게

### align-content
    Cross axis를 기준으로 공간배분
    justify와 기본적으로 같고 축만 바뀜

## flex - item

### 기타 속성
    flex-grow -> 남은 영역을 아이템에 분배
    order : 배치 순서
    