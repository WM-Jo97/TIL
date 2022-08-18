import sys
sys.stdin=open('prac.text')
edge_list = list(map(int,input().split(',')))
E = len(edge_list) // 2
V= 7
# 인접 정점
graph = [[0]* (V+1) for _ in range(V+1)]

for idx in range(E):
    #Graph[시작점][끝점]
    #
    frm = edge_list[idx*2]
    to = edge_list[idx*2 +1]
    graph[frm][to] = 1
    graph[to][frm] = 1

visited = [False] * (V+1)
'''
now = 1
stack = [now]
result = [now]
while stack:
    # 1. 방문한다
        visited[now] = 1
    # 2. 인접 정점을 확인한다.
        for nxt in range(V+1):
    # 3. 인접 정점을 이미 방문했는지 확인한다.
            if graph[now][nxt] == 1 and visited[nxt] == 0:
    # 4. 이동한다.
    # 4-1 이전 경로를 stack에 넣는다
                stack.append(now)
    # 4-2 방문 정점을 변경한다.
                now = nxt
                result.append(nxt)
                break
        else: # 모든 정점이 방문되었다면 stack에서 pop
            now = stack.pop()

print('-'.join(map(str, result)))
'''
result = []
# 재귀함수

def DFS(now):
    #1. 방문표시
    visited[now] = 1
    result.append(now)
    #2. 인접정점 확인
    for nxt in range(V+1):
        if graph[now][nxt] == 1 and visited[nxt] == 0:
    #3. 이동 가능하다면 이동
            DFS(nxt)
    return result
print(DFS(1))