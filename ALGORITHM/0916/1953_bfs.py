import sys
sys.stdin = open('example_3.text')

def bfs(R,C,L):
    visited = [[0] * M for _ in range(N)]
    Q = [(R,C)]
    visited[R][C] = 1
    while Q:
        y,x = Q.pop(0)
        T = arr[y][x]
        Temp = dict_1.get(T)
        for i in range(len(Temp)):
            yi, xi = Temp[i]
            di = y+yi
            dj = x+xi
            if 0<=di<N and 0<=dj<M:
                if arr[di][dj] !=0 and visited[di][dj] == 0:
                    T_1 = arr[di][dj]
                    Temp_1 = dict_1.get(T_1)
                    check=[]
                    for i in range(len(Temp_1)):
                        yi_2, xi_2 = Temp_1[i]
                        di_1 = di+yi_2
                        dj_1 = dj+xi_2
                        if 0 <= di_1 < N and 0 <= dj_1 < M:
                            if arr[di_1][dj_1]!=0:
                                check.append(1)
                    if check:
                        Q.append((di,dj))
                        visited[di][dj] = visited[y][x]+1

    return visited

T = int(input())
for t in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = []
    for i in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)

    dict_1 = {
        1 : [(1,0),(-1,0),(0,1),(0,-1)],
        2 : [(-1,0),(1,0)],
        3 : [(0,1),(0,-1)],
        4 : [(-1,0),(0,1)],
        5 : [(0,1),(1,0)],
        6 : [(0,-1),(1,0)],
        7 : [(0,-1),(-1,0)],
    }

    visited = [[0]*M for _ in range(N)]

    ANS = bfs(R,C,L)

    print(arr)
    COUNT = 0
    for i in range(N):
        for j in range(M):
            if ANS[i][j]!=0 and ANS[i][j] <= L:
                COUNT+=1

    print(COUNT)

