# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#### 스택을 사용한 DFS

import sys
sys.stdin=open('')

Points, Line = map(int,input().split())
arr = list(map(int,input().split()))
# [1,2,1,3..... ]

adj_arr = list([]for _ in range(Points+1)
for i in range(0, len(arr), 2):
    adj_arr[arr[i]].append(arr[i])

visited = [0 for _ in range(V+1)]
stack = []

def dfs(v):
    visited[v] = 1
    print(v)
    while True:
        for node in adj_arr[v]:
            if not visited[node]:
                stack.append(v)
                v = node
                visited[v] = 1
                print(v)
                break

        else:
            if stack:
                v = stack.pop()

            else:
                break

### 재귀함수를 이용한 DFS
def recursive_dfs(v):
    visited[v] = 1
    for node in adj_arr[v]:
        if not visited[node]:
            recursive_dfs(node)

            