import sys
sys.stdin = open('16236.text')

import sys
input = sys.stdin.readline

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                start = (i, j)
                return start
    return

def find_route(START,Q):
    y, x = START
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    for q in range(4):
        Dy = y+dy[q]
        Dx = x+dx[q]
        if 0<=Dy<N and 0<=Dx<N:
            if arr[Dy][Dx] <= Shark:
                min_value = distance[Dy][Dx]
                if distance[y][x] + 1 <= min_value:
                    distance[Dy][Dx] = distance[y][x] + 1
                    Q.append((Dy,Dx))
    return

def Bfs(start):
    Q = []
    Q.append(start)
    a, b = start
    distance[a][b] = 0
    while Q:
        start = Q.pop(0)
        if find_route(start,Q) == 0:
            return

N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

INF = 1000000000
distance = [[INF]*N for _ in range(N)]

Shark = 2
Shark_eat = 2
start = find_start(arr)
total = 0

while True:
    n, m = start
    arr[n][m] = 0
    Bfs(start)
    NUM_LIST = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                if arr[i][j] < Shark:
                    NUM_LIST.append((i,j))
    if NUM_LIST:
        min_value = 10000
        goal = 0
        for t in range(len(NUM_LIST)):
            s, g = NUM_LIST[t]
            if min_value > distance[s][g]:
                min_value = distance[s][g]
                goal = (s,g)
        if goal != 0:
            a,b = goal
            total += distance[a][b]
            start = goal
        else:
            break
        distance = [[INF] * N for _ in range(N)]
        Shark_eat -= 1
        if Shark_eat == 0:
            Shark += 1
            Shark_eat = Shark
    else:
        break

print(total)