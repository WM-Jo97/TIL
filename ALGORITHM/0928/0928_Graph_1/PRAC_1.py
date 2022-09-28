'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(start ,GRAPH, visited):
    STACK = [start]
    while STACK:
        TEMP = STACK.pop(-1)
        if visited[TEMP] == 1:
            pass
        else:
            visited[TEMP] = 1
            ans.append(TEMP)
            for i in range(len(GRAPH[TEMP])):
                STACK.append(GRAPH[TEMP][i])



NODE_LIST = list(map(int,input().split()))
GRAPH = [[] for _ in range(7+1)]

for i in range(len(NODE_LIST)//2):
     n1 = NODE_LIST[i*2]
     n2 = NODE_LIST[i*2+1]
     GRAPH[n1].append(n2)
     GRAPH[n2].append(n1)

visited = [0]*8
ans = []
dfs(1,GRAPH,visited)


for i in ans:
    print(i,end=' ')
print()