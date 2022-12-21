import sys
sys.stdin = open('example4.text')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [0]*(N+1)

edges = []
result = 0
for i in range(1,N+1):
    parent[i] = i

x= []
y= []
z= []

for i in range(1, N+1):
    DATA = list(map(int,input().split()))
    x.append((DATA[0],i))
    y.append((DATA[1],i))
    z.append((DATA[2],i))

x.sort()
y.sort()
z.sort()

for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)