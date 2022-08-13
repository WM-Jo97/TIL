# Box model
    Nomal flow 
        위에서 아래로, 왼쪽에서 오른쪽으로 쌓임

    모든 HTML요소는 BOX 형태로 이루어져 있음
    하나의 박스는 네부분으로 나누어짐
        margin
        border
        padding
        content

## Box model 구성
    .margin {
        margin-top : 10px;
        margin-rihgt : 20px;
        margin-bottom : 30px;
        margin-left : 40px;
    }

    .margin-padding {
        margin: 10px;
        padding : 30px;
    }

    .border {
        border-width : 2px;
        border-style : dashed;
        border-color : black;
    }

## shorthand를 통해서도 표현 가능

    .margin-1 {
        margin-10px;
    }
    --> 상하좌우 10px

    .margin-2 {
        margin: 10px 20px;
    }
    --> 상하 10px 좌우 20px

    .margin-3 {
        margin : 10px 20px 30px;
    }
    --> 상 10px 하 20px 좌우 30px

    .margin-4 {
        margin : 10px 20px 30px 40px;
    }
    --> 상 : 10px 우 : 20px 하 : 30px 좌 :40px;

## Border shorthand
    .border {
        border-width : 2px;
        border-style : dashed;
        border-color : black;
    }

    .border {
        border : 2px dashed black;
    }