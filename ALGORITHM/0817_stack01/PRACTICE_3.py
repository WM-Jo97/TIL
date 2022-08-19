import sys
sys.stdin=open('PRACTICE_3.text')

def DFS(v):
    top = -1

    print(v+1)  # 방문
    visited[v] = 1 # 시작점 방문

    while True:
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            # push(v);
                stack[top] = v
                v = w               # v <- w (w에 방문)
                print(v+1)  # 방문
                visited[w] = 1      # visited[w] <- true;
                break

        else:                       # w가 없으면
            if top!=-1:             #스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1

            else:                   #스택이 비어있으면
                break


Point, Line = map(int,input().split())
Num_list=list(map(int,input().split()))

for i in range(len(Num_list)):
    Num_list[i]=Num_list[i]-1

N = Point+1
adjList = [[] for _ in range(N)]

for i in range(0,len(Num_list),2):
    x, y = Num_list[i], Num_list[i+1]
    adjList[x].append(y)
    adjList[y].append(x)

visited = [0]*N
stack= [0]*N

DFS(0)