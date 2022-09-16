import sys
sys.stdin = open('example_1.text')

def bfs(n,graph,visited):
    Q=[]
    Q.append(n)
    visited[n] = 1
    while Q:
        t = Q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = visited[t]+1
    return(visited)

T = 10
for t in range(1,T+1):
    lenth,start = map(int,input().split())
    NUM = list(map(int,input().split()))
    max_N = max(NUM)     # N개의 방 만들때 중간에 생략된 수가 있을 수있어서 최대값 구해서

    graph = [[] for _ in range(max_N+1)]
    for i in range(len(NUM)//2):
        graph[NUM[2*i]].append(NUM[2*i+1])

    visited = [0 for _ in range(max_N + 1)]
    bfs(start,graph,visited)

    MAX_VIS = max(visited)
    ans = []
    for i in range(len(visited)):
        if visited[i] == MAX_VIS:
            ans.append(i)
    print(f'#{t} {max(ans)}')