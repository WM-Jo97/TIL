import sys
sys.stdin=open('example.text')

def BFS(Graph, start, N):
    visited=[0]*(N+1)
    Q = []
    visited[start] = 1
    Q.append(start)
    while Q:
        t = Q.pop(0)

        for i in Graph[t]:
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[t]+1

    return visited

N, M = map(int,input().split())

Graph = [[] for _ in range(N+1)]

for i in range(M):
    A,B=map(int, input().split())
    Graph[A].append(B)
    Graph[B].append(A)

TEM = BFS(Graph,1,N)
ANS = []
ANS.append(TEM.index(max(TEM)))
ANS.append(max(TEM)-1)
ANS.append(TEM.count(max(TEM)))

for i in ANS:
    print(i, end=' ')
print()