import sys
sys.stdin=open('1979.text')

def lenth(x):
    count=0
    for i in x:
        count+=1

    return count

T=int(input())

for t in range(1,T+1):
    N, K = map(int, input().split())

    Arr = [list(map(int, input().split())) for _ in range(N)]

    Stack_list=[]
    Count=0
    for i in range(N):
        Stack=[]
        for j in range(N):
            if Arr[i][j] == 1:
                Stack.append(1)
            else:
                Stack_list.append(lenth(Stack))
                Stack=[]
        Stack_list.append(lenth(Stack))

    for i in range(N):
        Stack=[]
        for j in range(N):
            if Arr[j][i] == 1:
                Stack.append(1)

            else:
                Stack_list.append(lenth(Stack))
                Stack=[]
        Stack_list.append(lenth(Stack))

    for i in Stack_list:
        if i == K:
            Count+=1

    print(f'#{t} {Count}')