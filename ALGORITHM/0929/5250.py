import sys
sys.stdin = open('example_4.text')

INF = 1000000000

def get_smallest_route(now):
    y,x = now
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            Dx = x + dx[i]
            Dy = y + dy[i]
            min_value = distance[Dy][Dx]
            if ARR[Dy][Dx] - ARR[y][x] > 0:
                if distance[y][x]+(ARR[Dy][Dx]-ARR[y][x])+1 <= min_value:
                    distance[Dy][Dx] = distance[y][x]+(ARR[Dy][Dx]-ARR[y][x])+1

            else:
                if distance[y][x]+1 <= min_value:
                    distance[Dy][Dx] = distance[y][x]+1
    return


T = int(input())

for t in range(1,T+1):
    N = int(input())
    ARR = []
    for i in range(N):
        TEMP = list(map(int,input().split()))
        ARR.append(TEMP)

    visited = [[0]*N for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]

    distance[0][0] = 0
    for i in range(N):
        for j in range(N):
            get_smallest_route((i,j))

    print(distance)
    print(f'#{t} {distance[N-1][N-1]}')