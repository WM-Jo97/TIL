import sys
sys.stdin = open('example_6.text')

def CHECK(arr, QUEEN,count,idx,Q):
    if QUEEN == N:
        count.append(1)
        return count
    else:
        for i in range(N):
            if QUEEN >= 1:
                if i == 0:
                    #print(Q)
                    #print(idx)
                    if i in idx or (QUEEN,i) in Q:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        for j in range(N - QUEEN):
                                Q.append((QUEEN + j, i + j))
                                Q.append((QUEEN + j, i - j))
                        CHECK(arr, QUEEN + 1, count,idx,Q)
                        for _ in range(2*(N-QUEEN)):
                            Q.pop(-1)
                        idx.pop(-1)
                elif i == N-1:
                    #print(Q)
                    #print(idx)
                    if i in idx or (QUEEN,i) in Q:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        for j in range(N - QUEEN):
                                Q.append((QUEEN + j, i + j))
                                Q.append((QUEEN + j, i - j))
                        CHECK(arr,QUEEN+1,count,idx,Q)
                        for _ in range(2*(N-QUEEN)):
                            Q.pop(-1)
                        idx.pop(-1)
                else:
                    #print(Q)
                    #print(idx)
                    if i in idx or (QUEEN,i) in Q:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        for j in range(N - QUEEN):
                                Q.append((QUEEN + j, i + j))
                                Q.append((QUEEN + j, i - j))
                        CHECK(arr, QUEEN + 1, count,idx,Q)
                        for _ in range(2*(N-QUEEN)):
                            Q.pop(-1)
                        idx.pop(-1)


            elif QUEEN == 0:
                arr[QUEEN][i] = 1
                idx.append(i)
                for j in range(N-QUEEN):
                        Q.append((QUEEN+j,i+j))
                        Q.append((QUEEN+j,i-j))
                CHECK(arr, QUEEN+1,count,idx,Q)
                idx.pop(-1)
                Q=[]


T = int(input())
for t in range(1,T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    QUEEN = 0
    count = []
    idx =[]
    Q = []
    CHECK(arr,QUEEN,count,idx,Q)

    print(f'#{t} {len(count)}')



