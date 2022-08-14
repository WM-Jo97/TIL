import sys
sys.stdin=open('1961.text')

T=int(input())

for i in range(1,T+1):
    N= int(input())
    arr=[]
    for i in range(N):
        arr.append(list(map(int,input().split())))
    print(arr)

    arr1=[]
    for i in range(N):
        for j in range(N-1,-1,-1):
            arr1.append(arr[j][i])
    print(arr1)

    arr2=[]
    for m in range(N-1,-1,-1):
        for n in range(N-1,-1,-1):
            arr2.append(arr[m][n])
    print(arr2)

    arr3=[]
    for x in range(N-1,-1,-1):
        for y in range(N):
            arr3.append(arr[y][x])
    print(arr3)

    print(arr1[0:N],end='')
    print(arr2[0:N],end='')
    print(arr3[0:N],end='')
    print()
