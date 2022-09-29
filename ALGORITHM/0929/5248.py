import sys
sys.stdin = open('example_2.text')
def findset(x):
    if x == REP_list[x]:
        return x
    else:
        return findset(REP_list[x])

def union(a,b):
    REP_list[findset(b)] = findset(a)

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    TEM = list(map(int, input().split()))

    REP_list = [i for i in range(N+1)]

    for j in range(len(TEM)//2):
        a, b = TEM[2*j], TEM[2*j + 1]
        union(a,b)
    for k in range(1, N+1):
        REP_list[k] = findset(k)
    print(f'#{t} {len(set(REP_list))-1}')