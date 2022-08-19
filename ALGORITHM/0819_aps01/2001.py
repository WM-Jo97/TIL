import sys
sys.stdin=open('2001.text')

T=int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    Arr = [[0]*N for i in range(N)]
    B = []
    for i in range(N):
        A= list(map(int,input().split()))
        for j in range(N):
            Arr[i][j]=A[j]


    Total_list = []
    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            Total = 0
            for y in range(i, i + M):
                for x in range(j,j+M):
                    Total+= Arr[y][x]
            Total_list.append(Total)

    Max_total=0
    for i in Total_list:
        if i > Max_total:
            Max_total = i

    print(f'#{t} {Max_total}')