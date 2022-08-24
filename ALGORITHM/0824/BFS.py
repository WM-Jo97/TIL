def bfs(v, N):
    visited = [0]*(N+1)
    q=[]
    q.append(v)
    visited[v]=1
    while q:
        v= q.pop(0)
        print(v)
        for w in adjList[v]:
            if visited[w]==0:
                q.append(w)
                visited[w]=visited[v]+1



V,E = map(int,input().split())
N = V+1
adjList= [[] for _ in range(N)]
for _ in range(E):
    a,b  = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

bfs(0,V)

"""
6 8
0 1 
0 2
1 3
1 4
2 4
3 5
4 5
5 6
"""