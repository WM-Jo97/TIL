import sys
sys.stdin=open('5102.text')

def BFS(Arr, Start, Goal, V):
    visited = [0]*(V+1)
    Q = []
    Q.append(Start)
    visited[Start]=1
    while Q:
        t = Q.pop(0)

        if t == Goal:
            #return visited[Goal]-1
            return visited
        for i in Arr[t]:
            if visited[i]==0:
                Q.append(i)
                visited[i] = visited[t]+1
    return 0

T=int(input())

for t in range(1,T+1):
    V, E = map(int,input().split())
    Arr=[[] for _ in range(V+1)]

    for _ in range(E):
        A, B = map(int,input().split())
        Arr[A].append(B)
        Arr[B].append(A)
    print(Arr)

    Start, Goal = map(int,input().split())
    #print(Start, Goal)

    print(f'#{t} {BFS(Arr,Start,Goal,V)}')