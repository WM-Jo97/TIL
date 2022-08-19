import sys
sys.stdin=open('1220.text')

T= 10

for t in range(1, T+1):
    N=int(input())

    Arr = [list(map(int,input().split())) for _ in range(N)]

    Total = 0
    for i in range(N):
        Stack = []
        for j in range(N):
            if not Stack:
                if Arr[j][i] == 1:
                    Stack.append(1)
            else:
                if Arr[j][i] == 2 and Stack[-1] == 1:
                    Stack.pop()
                    Total+=1
    print(f'#{t} {Total}')



