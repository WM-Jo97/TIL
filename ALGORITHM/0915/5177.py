import sys
sys.stdin = open('example_4.text')

def check(V,Number):
    if V:
        if Number[V-1] > Number[son1[V]-1]:
            if son1[V]!=0:
                Number[V-1], Number[son1[V]-1] = Number[son1[V]-1],Number[V-1]
        elif Number[V-1] > Number[son2[V]-1]:
            if son2[V] !=0:
                Number[V-1], Number[son2[V]-1] = Number[son2[V]-1], Number[V-1]
        check(son1[V],Number)
        check(son2[V], Number)

def find_father(n,record):
    record.append(n)
    for i in range(len(son1)):
        if son1[i] == n:
            find_father(i,record)
    for j in range(len(son2)):
        if son2[j] == n:
            find_father(j,record)

T = int(input())
for t in range(1,T+1):
    N =int(input())
    son1 = [0] * (N + 1)
    son2 = [0] * (N + 1)
    for i in range(2, N + 1):
        if i % 2 == 0:
            for j in range(1, N + 1):
                if son1[j] == 0:
                    son1[j] = i
                    break
        elif i % 2 == 1:
            for j in range(1, N + 1):
                if son2[j] == 0:
                    son2[j] = i
                    break
    Number = list(map(int,input().split()))
    #print(son1)
    #print(son2)
    print(Number)
    check(1,Number)
    print(Number)

    record=[]
    find_father(N,record)
    print(record)

    Total = 0
    for i in range(1,len(record)):
        Total += Number[record[i]-1]
    print(Total)