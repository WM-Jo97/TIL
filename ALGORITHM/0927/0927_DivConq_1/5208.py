import sys
sys.stdin = open('example_3.text')

def let_go(Location,Battery):
    global Route
    global count
    global ans
    if Location == STATION-1:

        if count < ans:
            ans = count
        return
    elif Battery == 0:
        if ans > count:
            Battery = charger[Location]
            count += 1
            Route.append((Location, Battery))
            let_go(Location + 1, Battery - 1)
            Route.pop(-1)
            count -= 1
            return
        else:
            return
    else:
        if ans > count:
            Route.append((Location,Battery))
            let_go(Location+1,Battery-1)
            Route.pop(-1)
            Battery = charger[Location]
            count += 1
            Route.append((Location,Battery))
            let_go(Location+1,Battery-1)
            Route.pop(-1)
            count -= 1
            return
        else:
            return
T = int(input())

for t in range(1,T+1):
     A = list(map(int,input().split()))
     STATION = A[0]
     charger = A[1:]+[0]
     Route = []
     count = 0
     ans = 100
     let_go(0,charger[0])

     print(f'#{t} {ans}')
