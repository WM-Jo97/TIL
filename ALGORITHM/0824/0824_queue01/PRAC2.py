def bfs(v, N):
    visited = [0]*(N+1)
    q=[]
    q.append(v)
    visited[v]=1
    while q:
        v= q.pop(0)
        print(f'-{v}',end='')
        for w in adjList[v]:
            if visited[w]==0:
                q.append(w)
                visited[w]=visited[v]+1


A=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
N=max(A)+1
adjList=[[] for i in range(N)]

for i in range(0,len(A)-1,2):
    a,b = A[i], A[i+1]
    adjList[a].append(b)
    adjList[b].append(a)
print(adjList)

bfs(1,N)