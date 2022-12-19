import sys
sys.stdin = open('example1.text')

N, M = map(int,input().split())
# print( N, M)

graph = [[] for _ in range(N)]

for i in range(N):
    route = list(map(int,input().split()))
    for j in range(len(route)):
        if route[j] == 1:
            graph[i].append(j)
print(graph)


plan = list(map(int, input().split()))
print(plan)


Queue = []

for i in range(len(plan)):
    Queue.append()