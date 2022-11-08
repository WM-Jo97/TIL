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
second = 1
move = (0,1)
print(Change_list)
print(arr)
snake = [(0,1)]
Num_cg, Chg = Change_list.pop(0)
while True:
    y,x = snake[-1]
    print(snake[-1])

    if 0<=y<N and 0<=x<N or (y,x) not in snake:
        if second == Num_cg:
            print(Chg)
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

            if Change_list:
                Num_cg,Chg = Change_list.pop(0)


            y_o, x_o = move
            location = (y+y_o, x+x_o)

            if arr[y][x] == 2:
                snake.append(location)
                second += 1
            else:
                snake.pop(0)
                snake.append(location)
                second += 1

        else:
            y_o, x_o = move
            location = (y + y_o, x + x_o)
            if arr[y][x] == 2:
                snake.append(location)
                second += 1
            else:
                snake.pop(0)
                snake.append(location)
                second += 1
    else:
        print(snake)
        print(second)
        print(-1)
        break