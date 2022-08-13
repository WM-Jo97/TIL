import sys
sys.stdin=open('practice2.text')

N = int(input())

for t in range(1,N+1):
    numbers=list(map(int,input().split()))

    n=len(numbers)
    total_list = []
    for i in range(1,1<<n):
        number_group=[]
        for j in range(n):
            if i&(1<<j):
                number_group.append(numbers[j])
        total=0
        for i in number_group:
            total+=i
        total_list.append(total)

    for i in total_list:
        if i==0:
            print('# 1')
            break
    else:
        print('# 0')