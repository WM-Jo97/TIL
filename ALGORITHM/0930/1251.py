import sys
sys.stdin = open('example_1251.text')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for t in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    NODE = []
    for i in range(N):
        TEMP = (Y[i],X[i])
        NODE.append(TEMP)

    edges = []
    for i in range(len(NODE)-1):
        for j in range(i+1,len(NODE)):
            temp = (((NODE[j][0]-NODE[i][0])**2+(NODE[j][1]-NODE[i][1])**2)*E,i,j)
            edges.append(temp)


    parent = [0]*(N)
    result = 0

    for i in range(N):
        parent[i] = i

    edges.sort()
    for edge in edges:
        cost, a, b = edge

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost

    print(f'#{t} {round(result)}')