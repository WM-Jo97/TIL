import sys
input = sys.stdin.readline

N = int(input())
t,p = [],[]
dp = [0] * (N+1)

for i in range(N):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

M = 0
for i in range(N):
    M = max(M,dp[i])
    if i+t[i] > N :
        continue
    dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
print(max(dp))