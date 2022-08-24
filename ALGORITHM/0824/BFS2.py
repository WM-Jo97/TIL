def bfs(v,N,t): #v 시작, N마지막 정점, t 찾는 정점
    visited = [] * (N+1)
    q = []
    q.append(v)
    visited[v]=1
    while q:
        v=q.pop(0)
        if v == t:
            return 1 #목표발견
        for w in adjList:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v]+1

        return 0

T=1
for _ in range(T):
    tc, E = map(int,input().split())
    arr = list(map(int,input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a,b = arr[i*2], arr[i*2 +1]
        adjList[a].append(b)

    bfs(0,99)

    """
    1 16
    0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
    """