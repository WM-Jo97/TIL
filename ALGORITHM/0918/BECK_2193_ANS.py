import sys
sys.stdin = open('example_2.text')

N = int(input())

DP = [0,1,1]

for i in range(3,91):
    result = DP[i-1] +DP[i-2]
    DP.append(result)

print(DP[N])