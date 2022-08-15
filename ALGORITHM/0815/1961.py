import sys
sys.stdin=open('1961.text')

T=int(input())

for t in range(1,T+1):
    N=int(input())

    NUM=[]
    for i in range(N):
        NUM.append(list(map(int,input().split())))

    print(f'#{t}')

    A=[]
    for i in range(N):
        for j in range(N-1,-1,-1):
            A.append(NUM[j][i])

    B=[]
    C=[]
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            B.append(NUM[i][j])

        for j in range(N):
            C.append(NUM[j][i])

    for i in range(N):
        for j in range(N):
            print(f'{A[j+(N*i)]}', end='')
        print(' ',end='')
        for j in range(N):
            print(f'{B[j+(N*i)]}', end='')
        print(' ', end='')
        for j in range(N):
            print(f'{C[j+(N*i)]}', end='')
        print()
