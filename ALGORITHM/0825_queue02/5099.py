import sys
sys.stdin=open('5099.text')

T= int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())

    Pizza = list(map(int,input().split()))

    Arr=[]

    P_num = 0
    for i in range(N):
        P_num += 1
        Arr.append([P_num,Pizza.pop(0)])
    # 처음 피자를 화덕에 넣기 (N개 까지 들어갈 수 있으므로)


    while len(Arr) != 1:
        TEMP = Arr.pop(0)
        if TEMP[1]//2 !=0:
            Arr.append([TEMP[0],TEMP[1]//2])
        else:
            if Pizza:
                P_num += 1
                Arr.append([P_num,Pizza.pop(0)])

    print(f'#{t} {Arr[0][0]}')