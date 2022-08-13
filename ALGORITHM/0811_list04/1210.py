import sys
sys.stdin=open('1210.text')

T= 10 # 테스트 케이스는 10개

for t in range(1,T+1):      # 테스트 케이스 10번 반복
    Case_Num = int(input())  # Case 넘버

    Radder_2D=[]             # Radder_2D = 사다리 2차원 리스트
    for i in range(100):
        Radder=list(map(int,input().split()))
        Radder_2D.append(Radder)               # Radder_2D --> 사다리 모델

    column=0
    for i in range(100):
        if Radder_2D[99][i]==2:
            column+=i
            break


    di = [0,0,-1]
    dj = [1,-1,0]      # 좌, 우만 확인

    row = 99
    while row>0:                         # 0을 만나면 멈춤
        for k in range(3):
            ni = row+di[k]
            nj = column+dj[k]
            if 0<=nj<100 and 0<=ni<100 and Radder_2D[ni][nj]==1:
                Radder_2D[row][column]=0
                row = ni
                column = nj


    print(f'#{t} {column}')
