import sys
sys.stdin = open('example_2.text')

def left_under(arr,y,x):
    Route.append((y, x))
    DISERT.append(arr[y][x])
    if 0<=y+1<N and 0<=x-1<N:
        if arr[y+1][x-1] not in DISERT:
            left_under(arr,y+1,x-1)
            right_under(arr,y+1,x+1)
        else:
            right_under(arr, y + 1, x + 1)
    elif 0<=y+1<N and 0<=x+1<N:
        right_under(arr,y+1,x+1)
    else:
        Route.pop(-1)
        DISERT.pop(-1)
        return
    Route.pop(-1)
    DISERT.pop(-1)
    return

def right_under(arr,y,x):
    Route.append((y, x))
    DISERT.append(arr[y][x])
    if 0 <= y + 1 < N and 0 <= x + 1 < N:
        if arr[y + 1][x + 1] in DISERT or (y+1,x+1) in Route:
            right_upper(arr, y - 1, x + 1)
        else:
            right_under(arr, y + 1, x + 1)

    elif 0 <= y - 1 < N and 0 <= x + 1 < N:
        right_upper(arr, y - 1, x + 1)
    else:
        Route.pop(-1)
        DISERT.pop(-1)
        return
    right_upper(arr, y-1,x+1)

    Route.pop(-1)
    DISERT.pop(-1)
    return

def right_upper(arr,y,x):
    Route.append((y, x))
    DISERT.append(arr[y][x])
    if 0 <= y - 1 < N and 0 <= x + 1 < N:
        if arr[y - 1][x + 1] not in DISERT:
            right_upper(arr, y - 1, x + 1)
            left_upper(arr, y-1, x - 1)
        else:
            left_upper(arr, y - 1, x - 1)
    elif 0 <= y - 1 < N and 0 <= x - 1 < N:
        left_upper(arr, y - 1, x - 1)
    else:
        Route.pop(-1)
        DISERT.pop(-1)
        return
    Route.pop(-1)
    DISERT.pop(-1)
    return

def left_upper(arr,y,x):
    Route.append((y, x))
    DISERT.append(arr[y][x])
    if (y,x) == Route[0]:
        ANS.append(Route)

    if (y,x) == Route[0]:
        duble = []
        for i in DISERT:
            count=0
            for j in range(len(DISERT)):
                if i == DISERT[j]:
                    count += 1
            duble.append(count)
        if duble.count(3)==0:
            TOTAL.append(len(DISERT))
        #print(DISERT)
        Route.pop(-1)
        DISERT.pop(-1)
        return
    if 0 <= y - 1 < N and 0 <= x - 1 < N:
        #print(DISERT)
        #print(Route)
        if arr[y-1][x-1] in DISERT:
            if (y-1,x-1) in Route :
                left_upper(arr, y-1, x-1)
            else:
                Route.pop(-1)
                DISERT.pop(-1)
                return
        else:
            left_upper(arr,y-1,x-1)

    else:
        Route.pop(-1)
        DISERT.pop(-1)
        return
    Route.pop(-1)
    DISERT.pop(-1)
    return

def DFS(arr,y,x):
    Route.append((y,x))
    DISERT.append(arr[y][x])

    if 0<= y+1 < N and 0<=x-1<N:
        left_under(arr,y+1,x-1)
        Route.pop(-1)
        DISERT.pop(-1)
        return
    else:
        Route.pop(-1)
        DISERT.pop(-1)
        return
    Route.pop(-1)
    DISERT.pop(-1)
    return

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))

    start = (0,0)
    Route = []
    DISERT = []
    ANS = []
    TOTAL = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            DFS(arr,i,j)
            Route=[]
    print(max(TOTAL)-1)
