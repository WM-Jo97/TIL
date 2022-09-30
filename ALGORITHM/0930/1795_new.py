import sys
sys.stdin = open('example_1795.text')
import heapq
T = int(input())
INF = 1000000000

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in Graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

for t in range(1,T+1):
    N,M,X = map(int,input().split())

    Graph = [[] for i in range(N+1)]
    distance = [INF]*(N+1)

    for i in range(M):
        x,y,c = map(int,input().split())
        Graph[x].append((y,c))

    start = X

    dijkstra(start)
    memo = []
    for x in range(len(distance)):
        memo.append(distance[x])
    distance = [INF] * (N + 1)

    ANS = 0
    for j in range(1,N+1):
        dijkstra(j)
        TOTAL = distance[start]+memo[j]
        if TOTAL > ANS:
            ANS = TOTAL
        distance = [INF] * (N + 1)

    print(f'#{t} {ANS}')
