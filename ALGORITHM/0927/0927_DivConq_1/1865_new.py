import sys
sys.stdin = open('example_4.text')

def dfs(idx, p):
    global maxP
    if idx == n:
        if maxP < p:
            maxP = p
        return
    elif maxP >= p:
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx + 1, p * percent[idx][i]/100)
            visited[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    percent = [list(map(int, input().split()))for _ in range(n)]
    maxP = 0
    visited = [0] * n
    dfs(0,1)   # 0% 부터 시작하면 계속 0임 ^^
    print(f'#{tc} {maxP*100:.6f}')