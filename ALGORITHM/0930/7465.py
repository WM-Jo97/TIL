import sys
sys.stdin = open('example_7465.text')

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    parent = [0] * (N+1)

    for i in range(1,N+1):
        parent[i] = i

    for i in range(M):
        a, b = map(int,input().split())
        union(parent,a,b)

    arr = []
    for i in range(1,N+1):
        arr.append(find_parent(parent,i))

    SET_ARR = set(arr)
    print(f'#{t} {len(SET_ARR)}')

