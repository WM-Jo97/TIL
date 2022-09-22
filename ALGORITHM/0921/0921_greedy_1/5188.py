import sys
sys.stdin = open('example_2.text')

def dfs(x,y,temp):
    global ans
    if temp > ans:
        return
    if x == y == N-1:
        if ans > temp:
            ans = temp
        return
    for i,j in [[0,1],[1,0]]:
        if x+i<N and y+j <N:
            dfs(x+i,y+j,temp+arr[x+i][y+j])

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 2* N * 10
    dfs(0,0,arr[0][0])
    print(f'#{t} {ans}')