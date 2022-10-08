import sys
sys.stdin = open('11660.text')

from sys import stdin

N, M = map(int,stdin.readline().split())
Arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
SUM_DATE = [[0]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        SUM_DATE[i][j] = SUM_DATE[i][j-1]+SUM_DATE[i-1][j] -SUM_DATE[i-1][j-1] + Arr[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int,stdin.readline().split())

    print(SUM_DATE[x2][y2] - SUM_DATE[x1-1][y2] - SUM_DATE[x2][y1-1] + SUM_DATE[x1-1][y1-1])
