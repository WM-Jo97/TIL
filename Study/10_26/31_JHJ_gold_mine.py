import sys
sys.stdin = open('example_1.text')

T = int(input())
N, M = map(int,input().split())
TEMP = list(map(int, input().split()))
arr = []

for i in range(N):
    Temp = TEMP[i*M:(i*M)+M]
    arr.append(Temp)

print(arr)

Dp_table = [[0]*M for _ in range(N)]
for i in range(N):
    Dp_table[i][0] = arr[i][0]

print(Dp_table)
for j in range(1, M):
    for i in range(N):
        dy = [-1,0,1]
        for x in range(3):
            DY = i+dy[x]
            if 0<=DY<N:
                Dp_table[i][j] = max(Dp_table[i][j], arr[i][j]+Dp_table[DY][j-1])

print(Dp_table)