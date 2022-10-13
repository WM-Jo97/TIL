import sys
sys.stdin = open('16236.text')

def find_goal(arr,Shark,start):
    eat = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                if arr[i][j] < Shark:
                    eat.append((i, j))
    if eat:
        num = 10000
        goto = 0
        for i in range(len(eat)):
            x, y = eat[i]
            m, n = start
            temp = abs(x - m) + abs(y - n)
            if temp < num:
                num = temp
                goto = i
        return (eat[goto])

    else:
        return 0

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                start = (i, j)
                return start


def find_route(START,Q):
    global distance
    y, x = START
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]

    for i in range(4):
        Dy = y+dy[i]
        Dx = x+dx[i]
        if 0<=Dy<N and 0<=Dx<N:
            if arr[Dy][Dx] <= Shark:
                min_value = distance[Dy][Dx]
                if distance[y][x] + 1 <= min_value:
                    distance[Dy][Dx] = distance[y][x] + 1
                    if Dy ==
                    Q.append((Dy,Dx))
    return

def Bfs(start):
    Q = []
    Q.append(start)
    x, y = start
    distance[x][y] = 0
    while Q:
        start = Q.pop(0)
        find_route(start,Q)

N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)

INF = 1000000000
distance = [[INF]*N for _ in range(N)]

Shark = 2
Shark_eat = 2
print(arr)
start = find_start(arr)
total = 0
while True:
    if find_goal(arr,Shark,start) != 0:
        x,y = find_goal(arr,Shark,start)
        Bfs(start)
        total += distance[x][y]
        start = x,y
        distance = [[INF] * N for _ in range(N)]

        Shark_eat-=1
        if Shark_eat == 0:
            Shark += 1
            Shark_eat = Shark

    else:
        break

print(distance)
print(total)