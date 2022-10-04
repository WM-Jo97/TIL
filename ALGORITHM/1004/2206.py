import sys
sys.stdin = open('example_2206.text')

def find_route(START, ARR):
    y, x = START
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]

    for i in range(4):
        Dy = y+dy[i]
        Dx = x+dx[i]
        if 0<=Dy<N and 0<=Dx<N:
            min_value = distance[Dy][Dx]
            if distance[y][x] + ARR[Dy][Dx] <= min_value:
                distance[Dy][Dx] = distance[y][x] + ARR[Dy][Dx]
    return

INF = 1000000000

N, M = map(int,input().split())
arr = []
for i in range(N):
    temp = list(map(int,input()))
    arr.append(temp)

print(arr)

distance = [[INF]*M for _ in range(M)]

distance[0][0] = 0
Stop = 0
while Stop != N:
    for i in range(N):
        for j in range(M):
            find_route((i,j),arr)
    Stop+=1

print(distance)