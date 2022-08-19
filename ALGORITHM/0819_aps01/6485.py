T=int(input())

for t in range(1,T+1):
    N = int(input())
    Bus=[0 for _ in range(5001)]
    for _ in range(N):
        A,B = map(int, input().split())
        for i in range(A,B+1):
            Bus[i] += 1

    P=int(input())
    print(f'#{t}',end=' ')
    for _ in range(P):
        C = int(input())
        print(Bus[C], end=' ')
    print()

