import sys
sys.stdin = open('1974.text')

T=int(input())

for t in range(1,T+1):
    arr=[]
    for i in range(9):
        numbers=list(map(int,input().split()))
        arr.append(numbers)
    ### 2차원 리스트로 배열을 만듭니다.

    inspect_v=1
    for i in range(9):
        dub_v = 1
        plus_v = 0
        for j in range(9):
            dub_v =dub_v*arr[i][j]
            plus_v = plus_v+arr[i][j]
        if dub_v!= 362880 or plus_v!=45:
             inspect_v=0
    #inspect_v 는 가로 요소들을 검사합니다. 모든 수의 합과 모든 수의 곱이 같으려면 중복없이 1~9까지 있어야 합니다.

    inspect_h=1
    for i in range(9):
        dub_h = 1
        plus_h = 0
        for j in range(9):
            dub_h = dub_h*arr[j][i]
            plus_h = plus_h+arr[j][i]

        if dub_h!= 362880 or plus_h!=45:
             inspect_h=0
    # inspect_h 는 세로 요소들을 검사합니다. 모든 수의 합과 모든 수의 곱이 같으려면 중복없이 1~9까지 있어야 합니다.

    inspect_sq=1
    for b in range(3):
        dub_sq = 1
        plus_sq = 0
        for n in range(3):
            for m in range(3):
                dub_sq=dub_sq*arr[b*3+n][m]
                plus_sq=plus_sq+arr[b*3+n][m]
        if dub_sq!=362880 or plus_sq!=45:
            inspect_sq=0
    # inspect_sq는 3*3 정사각형을 검사합니다.

    sudoku=0
    if inspect_sq==1 and inspect_h==1 and inspect_v==1:
        sudoku=1
    # sudoku 는 가로, 세로, 정방형 요소가 모두 문제가 없을 때 1을 출력합니다.

    print(f'#{t} {sudoku}')
