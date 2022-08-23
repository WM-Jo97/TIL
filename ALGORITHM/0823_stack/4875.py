import sys
sys.stdin=open('4875.text')

def Maz(Location):
    idx = [-1, 0, 0, 1]
    jdx = [0, 1, -1, 0]

    Stack = []

    while True:
        a=[]
        for k in range(4):
            x = Location[0] + idx[k]
            y = Location[1] + jdx[k]

            if x >= 0 and y >= 0 and x <= N - 1 and y <= N - 1:
                if Arr[x][y] == 3:
                    return 1

                elif Arr[x][y] == 0:
                    Location = [x,y]
                    Stack.append([Location[0], Location[1]])
                    Arr[x][y] = 1
                    break

        else:
            if Stack:
                Location = Stack[-1][0], Stack[-1][1]
                Stack.pop()
            else:
                return 0

T = int(input())

for t in range(1,T+1):
    N = int(input())
    Arr=[]
    for i in range(N):
        TEMP=list(map(int,input()))
        Arr.append(TEMP)

    Location=[]

    for i in range(N):
        for j in range(N):
            if Arr[i][j]==2:
                Location=[i,j]

    print(f'#{t} {Maz(Location)}')