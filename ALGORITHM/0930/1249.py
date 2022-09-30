import sys
sys.stdin = open('example_1249.text')

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


T = int(input())
INF = 1000000000

for t in range(1,T+1):
    N = int(input())
    ARR = []
    for i in range(N):
        TEMP = list(map(int, input()))
        ARR.append(TEMP)
    distance = [[INF]*N for _ in range(N)]

    distance[0][0] = 0
    STOP = 0
    while STOP != N:
        for i in range(N):
            for j in range(N):
                find_route((i,j),ARR)
        STOP+=1

    print(f'#{t} {distance[N-1][N-1]}')

