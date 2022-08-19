import sys
sys.stdin=open('1966.text')

T=int(input())

for t in range(1,T+1):
    N = int(input())

    Num = list(map(int,input().split()))
    for i in range(N-1,0,-1):
        for i in range(i):
            if Num[i+1] < Num[i]:
                Num[i],Num[i+1] = Num[i+1], Num[i]
    print(f'#{t}',end=' ')
    for i in Num:
        print(i, end=' ')
    print()