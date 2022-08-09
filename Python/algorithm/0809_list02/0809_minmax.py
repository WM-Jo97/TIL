import sys

sys.stdin = open('minmax.text')


T = int(input())

for t in range(1,T+1):
    times= int(input())
    numbers = list(map(int,input().split()))
    #숫자 입력받기

    max_number = 0

    for i in numbers:
        if i > max_number:
            max_number=0
            max_number+=i

    # max값 구하기


    min_number = 1000000
    for i in numbers:
        if i< min_number:
            min_number=0
            min_number+=i
    # min 값 구하기

    print(f'#{t} {max_number-min_number}')