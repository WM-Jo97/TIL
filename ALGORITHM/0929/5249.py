import sys
sys.stdin = open('example_3.text')
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent ,a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for t in range(1,T+1):
    V, E = map(int,input().split())
    parent = [0]*(V+1)

    edges = []
    result = 0

    for i in range(1,V+1):
        parent[i] = i

    for i in range(E):
        n1,n2,w = map(int,input().split())
        edges.append((w,n1,n2))

    edges.sort()

    for edge in edges:
        w, n1, n2 = edge
        if find_parent(parent,n1) != find_parent(parent, n2):
            union_parent(parent, n1,n2)
            result+= w

    print(f'#{t} {result}')
