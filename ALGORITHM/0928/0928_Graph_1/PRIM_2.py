


for _ in range(V):
    u = 0
    minV = 10000
    for i in range(V+1):
        if MST[i] == 1:
            for j in range(V+1):
                if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                    u = j
                    minV =adjM[i][j]

    s += minV

