import sys
sys.stdin = open('example_4.text')

N = int(input())
arr = list(map(int,input().split()))
arr.reverse()

DP_table = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if arr[j] < arr[i]:
            DP_table[i] = max(DP_table[i],DP_table[j]+1)

print(DP_table)
print(N-max(DP_table))