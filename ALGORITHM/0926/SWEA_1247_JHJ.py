import sys
sys.stdin = open('example_4.text')

def per(arr,n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in per(arr[:i] + arr[i+1:], n-1):
            result.append([elem]+rest)
    return result

def Check(start,arr_1):
    global ANS, HOME, TOTAL
    if arr_1:
        if ANS > TOTAL:
            return
        else:
            a,b = start
            TEMP = arr_1.pop(0)
            x,y = COSTOMER[TEMP]
            ANS += abs(a-x)+abs(b-y)
            Check((x,y),arr_1)
    else:
        if ANS > TOTAL:
            return
        else:
            a,b = start
            x,y = HOME
            ANS += abs(a-x) + abs(b-y)
            if ANS < TOTAL:
                TOTAL = ANS
            return
    return

T = int(input())

for t in range(1,T+1):
    N = int(input())
    TEMP = list(map(int,input().split()))
    loca_list = []
    for i in range(0,len(TEMP),2):
        loca_list.append((TEMP[i],TEMP[i+1]))

    JOB = loca_list[0]
    HOME = loca_list[1]
    COSTOMER = loca_list[2:]

    arr = list(range(N))
    #print(arr)
    #print(COSTOMER)
    result = per(arr,N)
    #print(result)
    ANS = 0
    TOTAL = 10000
    for i in range(len(result)):
        arr_1 = result[i]
        Check(JOB,arr_1)
        ANS = 0
    print(f'#{t} {TOTAL}')
