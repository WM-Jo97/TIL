import sys
sys.stdin=open('example_2.text')

N = int(input())

arr = []
for i in range(N):
    if i == 0:
        arr.append([int(input())])
    else:
        arr.append(list(map(int,input().split())))

#print(arr)

DP_TABLE=[]
for i in range(N):
    DP_TABLE.append([0]*(i+1))

DP_TABLE[0][0] = arr[0][0]
#print(DP_TABLE)

dx = [-1,0]
for i in range(1,len(arr)):
    for j in range(len(arr[i])):
        for x in range(2):
            DX = j+dx[x]
            if 0<= DX < len(arr[i-1]):
                DP_TABLE[i][j] = max(DP_TABLE[i][j],arr[i][j]+DP_TABLE[i-1][DX])

#print(DP_TABLE)

print(max(DP_TABLE[-1]))