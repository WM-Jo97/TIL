import sys
sys.stdin = open('example_1.text')

T = int(input())
N, M = map(int,input().split())
TEMP = list(map(int, input().split()))
arr = []

for i in range(N):
    Temp = TEMP[i*M:(i*M)+M]
    arr.append(Temp)

land_list = []
answer_list = []
def gold(a):
    y, x = a
    land_list.append(arr[y][x])
    if x == M-1:
        answer_list.append(sum(land_list))
        return
    else:
        dy = [-1,0,1]
        for i in range(3):
            Dy = y+dy[i]
            if 0<=Dy<N:
                a = (Dy,x+1)
                gold(a)
                land_list.pop(-1)
        return

a= (0,0)
for j in range(N):
    A = (j,0)
    gold(A)
    land_list.pop(-1)

print(max(answer_list))