import sys
sys.stdin = open('example_3.text')

N = int(input())

arr = []
for i in range(N):
    Ti , Pi = map(int,input().split())
    arr.append([Ti,Pi])

DP_table = [0]*(N+1)

max_value = 0

for i in range(N-1,-1,-1):
    time = arr[i][0] + i
    if time <= N:
        DP_table[i] = max(arr[i][1]+DP_table[time],max_value)
        max_value = DP_table[i]

    else:
        DP_table[i] = max_value

print(DP_table[0])