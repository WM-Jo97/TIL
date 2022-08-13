import sys

sys.stdin = open('sum.text')

T = int(input())
for t in range(1,T+1):
    (N,M) = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    total_number_list=[]
    for i in range(len(numbers)-M+1): #0 1 2 3 4 5 6 ^7 8 9
        total_number=0
        for j in range(i,i+M):
            total_number+=numbers[j]
        total_number_list.append(total_number)
    print(total_number_list)

    min_num=max_num=total_number_list[0]
    for i in total_number_list:
        if i <min_num:
            min_num=i

    for i in total_number_list:
        if i >max_num:
            max_num=i

    print(f'#{t} {max_num-min_num}')