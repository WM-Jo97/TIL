import sys
sys.stdin = open('example_1.text')

T = int(input())

for t in range(1,T+1):
    PRICE = list(map(int, input().split()))
    Plan = list(map(int, input().split()))

    CHECK = [0] * 12

    for i in range(len(Plan)):
        if Plan[i]*PRICE[0] >= PRICE[1]:
            Plan[i] = PRICE[1]
        else:
            Plan[i] = Plan[i]*PRICE[0]

    Total = [0]*12
    for i in range(len(Plan)):
        if i == 0:
            if Plan[i] >= PRICE[2]:
                Total[i] = PRICE[2]
            else:
                Total[i] = Plan[i]
        elif i == 1:
            if Plan[i] + Plan[i-1] >= PRICE[2]:
                Total[i] = PRICE[2]
            else:
                Total[i] = Total[i-1] + Plan[i]
        elif i == 2:
            if Plan[i] + Plan[i-1] + Plan[i-2] >= PRICE[2]:
                Total[i] = PRICE[2]
            else:
                Total[i] = Total[i-1] + Plan[i]
        else:
            if Plan[i] + Plan[i-1] + Plan[i-2] >= PRICE[2]:
                if Total[i-3] + PRICE[2] <= Total[i-1] + Plan[i]:
                    Total[i] = Total[i-3]+PRICE[2]
                else:
                    Total[i] = Total[i-1]+Plan[i]
            else:
                Total[i] = Total[i-1] +Plan[i]

    ans = [Total[11],PRICE[3]]

    print(f'#{t} {min(ans)}')