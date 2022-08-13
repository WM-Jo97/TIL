import sys
sys.stdin = open('1210.text')

for _ in range(10) :
    T = int(input())
    list_2 = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100) :
        if list_2[-1][i] == 2 :
            end_col_index = i
            break                   # 도착지점 열 인덱스를 찾아주는 코드
                                    # 도착지점의 row인덱스는 99, col인덱스는 end_col_index


        #오 |왼 | 위 순서
    di = [0, 0, -1]
    dj = [1, -1, 0]
    end_row_index = 99

    while end_row_index >0:
        for k in range(3) : #맨 처음 도착지점 위치 list_2[end_row_index][end_col_index]
            ni = end_row_index + di[k] # ni 행의 이동위치
            nj = end_col_index + dj[k] # nj 열의 이동위치
            if 0 <= ni < 100 and 0 <= nj < 100 and list_2[ni][nj] == 1:
                list_2[end_row_index][end_col_index] = 0 #####!!!!!!!이거때문에 좌우 이동이 계속 반복됨
                end_row_index = ni
                end_col_index = nj




    print(end_row_index, end_col_index)