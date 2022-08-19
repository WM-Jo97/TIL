import sys
sys.stdin=open('55789.text')

T=int(input())

for t in range(1,T+1):
    N, Q = map(int,input().split())

    Arr = [0 for i in range(N)]
    for i in range(Q):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            Arr[j]=i+1

    print(f'#{t}',end=' ')
    for i in Arr:
        print(i, end=' ')
    print()