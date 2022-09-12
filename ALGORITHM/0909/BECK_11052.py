import sys
sys.stdin = open('example.text')

N = int(input())
Price = list(map(int,input().split()))

Q=[]
Comb_n = []
COUNT = 0
Q.append(N)
arr = []
while Q:
    if sum(Q) == N:
        temp = []
        for i in Q:
            temp.append(i)
        arr.append(temp)
    Pop = Q.pop()
    if Pop != 1:
        if COUNT == 0:
            Q.append(Pop - 1)
            Q.append(1)

        else:
            Q.append(Pop -1)
            Q.append(COUNT)
            Q.append(1)
            COUNT = 0
    else:
        COUNT+=1
print(arr)

Check_price = 0
X = len(arr)
for i in range(X):
    Number = 0
    for j in range(len(arr[i])):
        Number += Price[arr[i][j]-1]
    if Number >= Check_price:
        Check_price = Number

print(Check_price)


'''
Max_conut=[]
for x in range(1,N):
    arr = []
    arr_num = range(1, N+1-x)
    for i in arr_num:
        num = N//i
        for j in range(num):
            arr.append(i)

    n = len(arr)
    comb = []
    for i in range(1<<n):
        com_x=[]
        for j in range(n):
            if i & (1<<j):
                com_x.append(arr[j])
        comb.append(com_x)

    check=[]
    for i in range(len(comb)):
        if sum(comb[i])== N:
            check.append(comb[i])

    for i in range(len(check)):
        count = 0
        for j in range(len(check[i])):
            count += Price[check[i][j]-1]
        Max_conut.append(count)

print(max(Max_conut))
'''