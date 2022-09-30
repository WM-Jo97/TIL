import sys
sys.stdin = open('example_1795.text')

T = int(input())
INF = 1000000000

for t in range(1,T+1):
    N,M,X = map(int,input().split())
    Graph = [[INF]*(N) for _ in range(N)]

    for a in range(N):
        for b in range(1,N):
            if a==b:
                Graph[a][b]=0

    for i in range(M):
        x,y,c = map(int,input().split())
        Graph[x-1][y-1] = c


    for k in range(N):
        for a in range(N):
            for b in range(N):
                Graph[a][b] = min(Graph[a][b], Graph[a][k] + Graph[k][b])

    Start = X
    END = list(range(1,N+1))
    END.remove(X)

    ANS = 0
    for i in range(len(END)):
        TEMP = 0
        TEMP += Graph[END[i]-1][Start-1]
        TEMP += Graph[Start-1][END[i]-1]
        if ANS <= TEMP:
            ANS = TEMP

    print(f'#{t} {ANS}')