import sys
sys.stdin = open('example_6.text')

def CHECK(QUEEN,arr,IDX,location):
    if QUEEN == N:
        #print(location)
        #print(arr)
        global COUNT
        COUNT += 1
        return
    else:
        if QUEEN == 0:
            for i in range(N):
                location.append((QUEEN,i))
                IDX.append(i)
                for j in range(N):
                    if 0<= QUEEN+j < N and 0<= i+j < N:
                        arr[QUEEN+j][i+j] += 1
                    if 0<= QUEEN+j < N and 0<= i-j < N:
                        arr[QUEEN+j][i-j] += 1

                CHECK(QUEEN+1,arr,IDX,location)
                IDX.pop(0)
                arr = [[0]*N for _ in range(N)]
                location = []
        else:
            for i in range(N):
                if i not in IDX and arr[QUEEN][i] == 0:
                    location.append((QUEEN,i))
                    IDX.append(i)
                    for j in range(N-QUEEN):
                        if 0 <= QUEEN + j < N and 0 <= i + j < N:
                            arr[QUEEN + j][i + j] += 1
                        if 0 <= QUEEN + j < N and 0 <= i - j < N:
                            arr[QUEEN + j][i - j] += 1

                    CHECK(QUEEN + 1, arr, IDX,location)

                    for j in range(N-QUEEN):
                        if 0 <= QUEEN + j < N and 0 <= i + j < N:
                            arr[QUEEN+j][i+j] -= 1
                        if 0 <= QUEEN + j < N and 0 <= i - j < N:
                            arr[QUEEN+j][i-j] -= 1
                    IDX.pop(-1)
                    location.pop(-1)

            return



N = int(input())

arr = [[0]*N for _ in range(N)]

QUEEN = 0
IDX =[]
ROUTE = []
location = []
COUNT = 0
CHECK(QUEEN,arr,IDX,location)
print(COUNT)
