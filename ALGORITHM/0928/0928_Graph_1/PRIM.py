def prim1(r, V):
    MST = [0]*(V+1)               #MST 포함여부
    key = [10000]*(V+1)           # 가중치의 최대값 이상으로 초기화,
    key[r] = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i]<minV:
                u = i
                minV = key[i]

        MST[u] = 1

        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v],adjM[u][v])
    return sum(key)

V,E = map(int, input().split())
arr = list(map(int,input().split()))

#인접행렬 준비
adjM = [[0]*(V+1) for _ in range(V+1)]
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2],arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1

    adjList[n1].append(n2)
    adjList[n2].append(n1)


    prim1()