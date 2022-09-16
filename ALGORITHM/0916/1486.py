import sys
sys.stdin=open('example_5.text')

T = int(input())
for t in range(1,1+T):
    N,B = map(int,(input().split()))
    H_list = list(map(int,input().split()))

    n = len(H_list)

    ANS = []
    for i in range(1<<n):
        TEMP = []
        for j in range(n):
            if i&(1<<j):
                TEMP.append(H_list[j])
        ANS.append(TEMP)

    A_List = []
    for i in range(len(ANS)):
        if sum(ANS[i]) >= B:
            A_List.append(sum(ANS[i]))

    print(f'#{t} {min(A_List)-B}')
