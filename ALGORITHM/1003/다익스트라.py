
N = 4
M = 4
M_list = [(20,1,3),(10,2,3),(5,1,2),(40,2,4)]


INF = 1000000000
graph = [INF]*N
parent = [0]*N
for i in range(N):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])

    return x

def union(parent,a,b):
    if parent[a] != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

def dijkstra(x):
