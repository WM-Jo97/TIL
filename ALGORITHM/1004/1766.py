import sys
sys.stdin = open('example_1766.text')

N, M = map(int,input().split())

arr = []
for i in range(M):
    SECOND, FIRST = map(int,input().split())
    arr.append((SECOND,FIRST))

arr.sort()

for i in range(len(arr)-1):
    if arr[i][1] > arr[i+1][0]:
        arr[i][1] , arr[i+1][0] = arr[i+1][0], arr[i][1]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')