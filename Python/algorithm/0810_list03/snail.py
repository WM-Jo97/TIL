import sys

sys.stdin = open('snail.text')

Test_case = int(input())

for t in range(1,Test_case+1):
    N = int(input())
    arr_2D=[]
    for i in range(N):
        arr=list(0 for _ in range(N))
        arr_2D.append(arr)               # 먼저 2차 리스트로 필요한 만큼의 방을 미리 만들어 줍니다.


    count=0                              # 숫자가 점점 늘어나야 하기 때문에 count로 간단히 표현했습니다.
    for m in range(N):                   # 1사이클에 좌에서 우로 , 위에서 아래로, 우에서 좌로, 아래에서 위로 를 시행하고 반복합니다.
                                         # 시행 횟수가N인 이유는 여유롭게 시행하더라도 해당 방이 비어있지 않으면 아무일도 없기 때문입니다. 필요시 더 연산을 줄일 수 있습니다.
        for j in range(N):
            if arr_2D[m][j]==0:          # 해당 방이 비어있지 않으면 아무일도 하지 않습니다.
                count+=1                 # 좌에서 우로 이동할 경우 행을 고정되고 열만 움직입니다.
                arr_2D[m][j]=count

        for i in range(N):               # 위에서 아래로 움직일때는 행이 고정이고 열이 움직입니다.
            if arr_2D[i][N-1-m]==0:      # 한줄 씩 줄여나가면서 돌리려면 m을 빼주면 됩니다.
                count+=1
                arr_2D[i][N-1-m]=count

        for i in range(N-1,-1,-1):      # 우에서 좌로 이동할 때는 1번 for문에서 형식은 같지만 N-1부터 -1씩 역으로 움직입니다.
            if arr_2D[N-1-m][i]==0:
                count+=1
                arr_2D[N-1-m][i]=count

        for i in range(N-1,-1,-1):      # 아래에서 위로 움직일때는 2번 FOR문에서 N-1부터 -1씩 역으로 움직입니다.
            if arr_2D[i][m]==0:
                count+=1
                arr_2D[i][m]=count

    print(f'#{t}')

    for i in range(N):                      # 테스트 케이스 결과가 리스트 형식이 아니기때문에 형식을 맞춰줍니다.
        for j in range(N):
            print(arr_2D[i][j],end=' ')
        print()





