import sys
sys.stdin = open('example.text')

from itertools import combinations

def BFS(Arr,Arr_check,N,M,Graph):
    di = (0, 1, -1, 0)
    dj = (1, 0, 0, -1)
    Zero_list=[]
    visited = [[0] * M for _ in range(N)]
    Q = []

    for i in range(len(Graph)):
        Q.append(Graph[i])
        visited[Graph[i][0]][Graph[i][1]] = 1
        while Q :
            t = Q.pop(0)
            X = t[1]
            Y = t[0]
            for j in range(4):
                BX = X+di[j]
                BY = Y+dj[j]
                if 0 <= BX < M and 0<= BY < N:
                    if Arr_check[BY][BX] == 0 and not visited[BY][BX]:
                        Q.append([BY,BX])
                        Arr_check[BY][BX] = 2
                        visited[BY][BX] = 1
    count=0
    for x in range(N):
        for y in range(M):
            if Arr_check[x][y]==0:
                count+=1

    return count

N, M = map(int,input().split())

Arr = []

for i in range(N):
    A = list(map(int,input().split()))
    Arr.append(A)

Graph = []
for i in range(N):
    for j in range(M):
        if Arr[i][j]== 2:
            Graph.append([i,j])

blank_list = []
for i in range(N):
    for j in range(M):
        if Arr[i][j] == 0:
            blank_list.append([i,j])

n = len(blank_list)

Combi = list(combinations(blank_list,3))
Arr_check = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        Arr_check[i][j] = Arr[i][j]

max_Safe=[]
for i in range(len(Combi)):
    Saftzone = []
    for j in range(len(Combi[i])):
        Arr_check[Combi[i][j][0]][Combi[i][j][1]] = 1
    Saftzone.append(BFS(Arr,Arr_check,N,M,Graph))
    max_Safe.append(max(Saftzone))

    for i in range(N):
        for j in range(M):
            Arr_check[i][j] = Arr[i][j]

print(max(max_Safe))



"""
for i in range(1<<n):
    for j in range(n):
        Num_list = []
        if i & (1<<j):
            print(blank_list[j], end=', ')
    print()
print()
"""