import sys
sys.stdin=open('5105.text')

def BFS(Start) :
    visited = [[0]*(N) for _ in range(N)]
    Q=[]
    Q.append(Start)
    visited[Start[0]][Start[1]] = 1
    while Q:
        t=Q.pop(0)
        di = [1,0,0,-1]
        dj = [0,1,-1,0]                                            #BFS, DFS + 델타 ==> 같이 사용하는 문제가 많음
        for k in range(4):                                         (BFS, DFS) + 델타 + 재귀함수
            x = t[1] + di[k]
            y = t[0] + dj[k]
            if N>x>=0 and N>y>=0:
                if Arr[y][x] == 0 and visited[y][x] ==0:
                    Q.append([y,x])
                    visited[y][x] = visited[t[0]][t[1]]+1

                elif Arr[y][x] == 3:
                    Q.append([y,x])
                    visited[y][x] = visited[t[0]][t[1]]+1
                    max_ret=0
                    for i in visited:
                        if max(i)> max_ret:
                            max_ret=max(i)

                    #return max_ret-2
                    return visited
    return 0
T=int(input())

for t in range(1,T+1):
    N = int(input())
    Arr = []
    for i in range(N):
        A = list(map(int,input()))
        Arr.append(A)

    Start=[]
    for i in range(N):
        for j in range(N):
            if Arr[i][j]==2:
                Start.append(i)
                Start.append(j)

    #print(f'#{t} {BFS(Start)}')
    for i in BFS(Start):
        print(i)
    print()

