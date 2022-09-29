import sys
sys.stdin = open('example_5.text')

T = int(input())
INF = 1000000000

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(N):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now]+j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost


for t in range(1,T+1):
    N,M = map(int,input().split())
    start = 0
    graph = [[] for i in range(N)]
    visited = [0]*(N+1)
    distance = [INF]*(N+1)

    for _ in range(M):
        a, b, c = map(int,input().split())
        graph[a].append((b,c))

    print(graph)


    dijkstra(start)

    print(distance)
    print(f'#{t} {distance[N]}')

