import sys
sys.stdin = open('example_3.text')

T = int(input())

for t in range(1,T+1):
    N,A,B = map(int,input().split())

    ans = [1,1] #N이 1일때 X Y
    nxt = [1]
    for i in range(1,N):
        for j in range(len(ans)-1):
            nxt.append(ans[j]+ans[j+1])
        nxt.append(1)
        ans = nxt
        nxt=[1]
    print(f'#{t} {ans[B]}')