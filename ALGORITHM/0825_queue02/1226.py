import sys
sys.stdin=open('1226.text')

def BFS(Start) :
    visited = [[0]*(N) for _ in range(N)]
    Q=[]
    Q.append(Start)
    visited[Start[0]][Start[1]] = 1
    while Q:
        t=Q.pop(0)
        di = [1,0,0,-1]
        dj = [0,1,-1,0]
        for k in range(4):
            x = t[1] + di[k]
            y = t[0] + dj[k]
            if N>x>=0 and N>y>=0:
                if Arr[y][x] == 0 and visited[y][x] ==0:
                    Q.append([y,x])
                    visited[y][x] = visited[t[0]][t[1]]+1

                elif Arr[y][x] == 3:
                    Q.append([y,x])
                    visited[y][x] = visited[t[0]][t[1]]+1
                    return 1

    return 0


T = 10
N = 16
for t in range(1,T+1):
    t=int(input())
    Arr=[]
    for i in range(N):
        TEMP = list(map(int,input()))
        Arr.append(TEMP)

    Start = []
    for i in range(N):
        for j in range(N):
            if Arr[i][j] == 2:
                Start.append(i)
                Start.append(j)

    print(f'#{t} {BFS(Start)}')
