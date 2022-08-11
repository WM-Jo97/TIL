import sys
sys.stdin=open('1210.text')

T= 10 # 테스트 케이스는 10개

for i in range(1,T+1):      # 테스트 케이스 10번 반복
    Case_Num = int(input())  # Case 넘버

    Radder_2D=[]             # Radder_2D = 사다리 2차원 리스트
    for i in range(100):
        Radder=list(map(int,input().split()))
        Radder_2D.append(Radder)               # Radder_2D --> 사다리 모델

    column=0
    for i in range(98):
        if Radder_2D[99][i]==2:
            column+=i
            break
    print(column)
    row=99
    position=Radder_2D[row][column]
    print(position)
    """
    di = [0,0,-1]
    dj = [1,-1,0]                               # 좌, 우만 확인

    count = 0                             # 움직인 횟수 0
    while row!=0:                         # 0을 만나면 멈춤
        for k in range(2):              # 좌, 우 확인
            if 0<column<99:
                nj = column+dj[k]          # dj[0]일때 왼쪽, dj[1]일때 오른쪽
                if Radder_2D[row][nj]!=0:           # row와 column 이 0이 아니면-> 길이 있으면
                    Radder_2D[row][column]=0 # 움직인 후 위치 수정
                    column = nj     # 왼쪽이나 오른쪽으로 움직이기 때문에 움직인 거리
                    row -= 1
                    count+=1
            else:
                row -= 1
                count+=1
    print(count)
    """