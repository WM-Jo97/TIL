import sys
sys.stdin = open('example_3.text')

N= int(input())
arr = [[0]*N for _ in range(N)]
M = int(input())
for _ in range(M):
    y,x = map(int,input().split())
    arr[y][x] = 2

Change = int(input())
Change_list = []
for _ in range(Change):
    X,C = input().split()
    Change_list.append((int(X),C))

NUM = 0
location = (0,0)
second = 0
move = (0,1)
print(Change_list)
print(arr)

while True:
    Num_cg, Chg = Change_list[NUM]
    y,x = location
    y_o, x_o = move
    if arr[y][x] != 1:
        arr[y][x] = 1
        if second == Num_cg:
            if Chg == 'D':
                if move == (0,1):
                    move = (1,0)
                elif move == (1,0):
                    move = (0,-1)
                elif move == (0,-1):
                    move = (-1,0)
                elif move == (-1,0):
                    move = (0,1)
            elif Chg == 'L':
                if move == (0,1):
                    move = (-1,0)
                elif move == (-1,0):
                    move = (0,-1)
                elif move == (0,-1):
                    move = (1,0)
                elif move == (1,0):
                    move = (0,1)
            if arr[y][x] == 2:
                pass
            else:
                pass
        else:
            location = (y+y_o, x+x_o)
            if arr[y][x] == 2:
                pass
            else:
                pass
    else:
        break