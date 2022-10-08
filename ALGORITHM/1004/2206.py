import sys
sys.stdin = open('example_2206.text')

def find_route(START, ARR):
    y, x = START
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]

    for i in range(4):
        Dy = y+dy[i]
        Dx = x+dx[i]
        if 0<=Dy<N and 0<=Dx<M and ARR[Dy][Dx] != 1:
            min_value = distance[Dy][Dx]
            if distance[y][x] + ARR[Dy][Dx] <= min_value:
                distance[Dy][Dx] = distance[y][x] + +1
    return

INF = 1000000000

N, M = map(int,input().split())
arr = []
for i in range(N):
    temp = list(map(int,input()))
    arr.append(temp)

ans= INF
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            arr[y][x] = 0

            distance = [[INF] * M for _ in range(N)]
            distance[0][0] = 0
            Stop = 0
            while Stop != N:
                for i in range(N):
                    for j in range(M):
                        find_route((i, j), arr)
                Stop += 1
            if distance[N-1][M-1] < ans:
                ans = distance[N-1][M-1]
            arr[y][x] = 1

if ans>= INF:
    print(-1)
else:
    print(ans+1)


