import sys
sys.stdin=open('5097.text')

T= int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    NUM=list(map(int, input().split()))

    for _ in range(M):
        NUM.append(NUM.pop(0))

    print(f'#{t} {NUM[0]}')