import sys
sys.stdin = open('example_3.text')

T = int(input())

for t in range(1,T+1):
    N,A,B = map(int,input().split())

    arr = [0]*(N+1)
    ans = [1,1]
    nxt = [1]
    for i in range(1,N):
        for j in range(len(ans)-1):
            nxt.append(ans[j]+ans[j+1])
        nxt.append(1)
        ans = nxt
        nxt=[1]
    print(f'#{t} {ans[B]}')