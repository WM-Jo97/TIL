import sys
sys.stdin = open("example3.text")


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int,input().split())
parent = [0]*(N+1)

load = []
result = 0

for i in range(1,N+1):
    parent[i] = i


for _ in range(M):
    x,y,z = map(int,input().split())
    load.append((z,x,y))

load.sort()
total = 0

for x in load:
    cost, a, b = x
    total += cost

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a ,b)
        result += cost

print(total-result)