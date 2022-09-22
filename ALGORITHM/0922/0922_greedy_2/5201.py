import sys
sys.stdin = open('example_2.text')

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    Weight = list(map(int,input().split()))
    Capa = list(map(int,input().split()))

    Total = 0
    for i in range(len(Capa)):
        Truck = 0
        for j in range(len(Weight)):
            if Capa[i] >= Weight[j]:
                if Truck < Weight[j]:
                    Truck = Weight[j]
        if not Truck:
            pass
        else:
            Weight.remove(Truck)
            Total+= Truck

    print(f'#{t} {Total}')