import sys
sys.stdin = open('example_6.text')

def CHECK(arr, QUEEN,count,idx):
    if QUEEN == N:
        count.append(1)
        return count
    else:
        for i in range(N):
            if QUEEN >= 1:
                if i == 0:
                    if i in idx or arr[QUEEN-1][i+1]==1:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        CHECK(arr, QUEEN + 1, count,idx)
                elif i == N-1:
                    if i in idx or arr[QUEEN-1][i-1]==1:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        CHECK(arr,QUEEN+1,count,idx)
                else:
                    if i in idx or arr[QUEEN-1][i-1] or arr[QUEEN-1][i+1]==1:
                        pass
                    else:
                        arr[QUEEN][i] = 1
                        idx.append(i)
                        CHECK(arr, QUEEN + 1, count,idx)

            elif QUEEN == 0:
                arr[QUEEN][i] = 1
                idx.append(i)
                CHECK(arr, QUEEN+1,count,idx)



T = int(input())
for t in range(1,T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    QUEEN = 0
    count = []
    idx =[]
    CHECK(arr,QUEEN,count,idx)

    print(f'#{t} {len(count)}')



