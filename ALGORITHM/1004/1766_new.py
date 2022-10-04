import sys
import heapq

num_problem, num_compare = map(int, input().split())
problem_list = [[] for i in range(num_problem + 1)]
indegree = [0 for i in range(num_problem + 1)]
heap = []
result = []


#Graph Information
for i in range(num_compare):
    A, B = map(int, input().split())
    problem_list[A].append(B)
    indegree[B] += 1


#Make First heap
for i in range(1, num_problem + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)


#Make Topological Sort Loop
while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in problem_list[temp]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)

for i in result:
    print(i, end=' ')