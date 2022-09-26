import sys
sys.stdin = open('example_6.text')

def CHECK(QUEEN,ROUTE,IDX,location):
    if QUEEN == N:
        print(location)
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
                        ROUTE.append((QUEEN+j, i+j))
                    if 0<= QUEEN+j < N and 0<= i-j < N:
                        ROUTE.append((QUEEN+j, i-j))
                Set_Route = set(ROUTE)
                ROUTE = list(Set_Route)
                CHECK(QUEEN+1,ROUTE,IDX,location)
                IDX.pop(0)
                ROUTE=[]
                location = []
        else:
            for i in range(N):
                if i not in IDX and (QUEEN,i) not in ROUTE:
                    location.append((QUEEN,i))
                    IDX.append(i)
                    for j in range(N-QUEEN):
                        if 0 <= QUEEN + j < N and 0 <= i + j < N and (QUEEN+j,i+j) not in ROUTE:
                            ROUTE.append((QUEEN + j, i + j))
                        if 0 <= QUEEN + j < N and 0 <= i - j < N and (QUEEN+j,i-j) not in ROUTE:
                            ROUTE.append((QUEEN + j, i - j))

                    CHECK(QUEEN + 1, ROUTE, IDX,location)

                    for j in range(N-QUEEN):
                        if 0 <= QUEEN + j < N and 0 <= i + j < N and (QUEEN+j,i+j) in ROUTE:
                            ROUTE.remove((QUEEN+j,i+j))
                        if 0 <= QUEEN + j < N and 0 <= i - j < N and (QUEEN+j,i-j) in ROUTE:
                            ROUTE.remove((QUEEN+j,i-j))
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
CHECK(QUEEN,ROUTE,IDX,location)
print(COUNT)
