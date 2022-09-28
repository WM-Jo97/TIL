'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def Bfs(start ,GRAPH, visited):
    Q = [start]
    while Q:
        TEMP = Q.pop(0)
        if visited[TEMP] == 1:
            pass
        else:
            visited[TEMP] = 1
            ans.append(TEMP)
            for i in range(len(GRAPH[TEMP])):
                Q.append(GRAPH[TEMP][i])


NODE_LIST = list(map(int,input().split()))
GRAPH = [[] for _ in range(7+1)]

for i in range(len(NODE_LIST)//2):
     n1 = NODE_LIST[i*2]
     n2 = NODE_LIST[i*2+1]
     GRAPH[n1].append(n2)
     GRAPH[n2].append(n1)

visited = [0]*8
ans = []
Bfs(1,GRAPH,visited)


for i in ans:
    print(i,end=' ')
print()