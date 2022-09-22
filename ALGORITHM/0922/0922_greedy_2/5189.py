import sys
sys.stdin = open('example_1.text')

def f(i,k,r):
    if i == r:
        A = [1]
        for j in range(len(p)):
            A.append(p[j])
        A.append(1)
        Route_list.append(A)

    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = Num_list[j]
                f(i+1,k,r)
                used[j] = 0

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)

    Num_list = list(range(1,N+1))
    Num_list.pop(0)

    used = [0]*N
    n = len(Num_list)
    R = N-1
    p = [0]*R
    Route_list = []
    f(0,n,R)

    Ans = 10000000
    for i in range(len(Route_list)):
        Temp_ANS = 0
        for j in range(len(Route_list[i])-1):
            Temp_ANS += arr[Route_list[i][j]-1][Route_list[i][j+1]-1]
        if Temp_ANS < Ans:
            Ans = Temp_ANS

    print(f'#{t} {Ans}')