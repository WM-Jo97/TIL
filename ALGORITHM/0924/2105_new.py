import sys
sys.stdin = open('example_2.text')

def START(arr,y,x):
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


def left_under(arr,y,x):
    if (y,x) in Route or arr[y][x] in DISERT:
        return

    else:
        Route.append((y, x))
        DISERT.append(arr[y][x])
        if 0<=y+1<N and 0<=x-1<N:
            left_under(arr,y+1,x-1)
            if 0 <= y + 1 < N and 0 <= x + 1 < N:
                right_under(arr,y+1,x+1)
            Route.pop(-1)
            DISERT.pop(-1)
            return
        elif 0 <= y + 1 < N and 0 <= x + 1 < N:
            right_under(arr, y + 1, x + 1)
            Route.pop(-1)
            DISERT.pop(-1)
            return
        else:
            Route.pop(-1)
            DISERT.pop(-1)
            return

def right_under(arr,y,x):
    if (y,x) in Route or arr[y][x] in DISERT:
        return

    else:
        Route.append((y, x))
        DISERT.append(arr[y][x])
        if 0 <= y + 1 < N and 0 <= x + 1 < N:
            right_under(arr, y+1, x+1)
            if 0<=y-1<N and 0<=x+1<N:
                right_upper(arr, y - 1, x + 1)
            Route.pop(-1)
            DISERT.pop(-1)
            return

        elif 0 <= y - 1 < N and 0 <= x + 1 < N:
            right_upper(arr, y - 1, x + 1)
            Route.pop(-1)
            DISERT.pop(-1)
            return
        else:
            Route.pop(-1)
            DISERT.pop(-1)
            return

def right_upper(arr,y,x):
    if (y,x) in Route or arr[y][x] in DISERT:
        return

    else:
        Route.append((y, x))
        DISERT.append(arr[y][x])
        if 0 <= y - 1 < N and 0 <= x + 1 < N:
            right_upper(arr, y - 1, x + 1)
            if 0 <= y - 1 < N and 0 <= x - 1 < N:
                left_upper(arr, y-1, x - 1)
            Route.pop(-1)
            DISERT.pop(-1)
            return

        elif 0 <= y - 1 < N and 0 <= x - 1 < N:
            left_upper(arr, y - 1, x - 1)
            Route.pop(-1)
            DISERT.pop(-1)
            return
        else:
            Route.pop(-1)
            DISERT.pop(-1)
            return

def left_upper(arr,y,x):
    if (y,x) in Route or arr[y][x] in DISERT:
        if (y,x) == Route[0]:
            ANS.append((len(DISERT)))
            #print(DISERT)
            return
        else:
            return
    else:
        Route.append((y, x))
        DISERT.append(arr[y][x])
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            left_upper(arr, y-1, x-1)
            Route.pop(-1)
            DISERT.pop(-1)
            return
        else:
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
            START(arr,i,j)
            Route=[]

    if ANS:
        print(f'#{t} {max(ANS)}')
    else:
        print(f'#{t} -1')

