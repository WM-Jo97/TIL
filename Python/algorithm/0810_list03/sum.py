import sys

sys.stdin = open('sum.text')

for t in range(1,11):
    Test_case = int(input())
    numbers=[]
    for i in range(100):
        number = list(map(int, input().split()))
        numbers.append(number)

    max_value=0
    my_total = 0
    for i in range(100):
        my_total=0
        for j in range(100):
            my_total += numbers[i][j]

        if max_value < my_total:
            max_value = my_total

    for i in range(100):
        my_total=0
        for j in range(100):
            my_total += numbers[j][i]

        if max_value < my_total:
            max_value = my_total

    my_total=0
    for i in range(100):
        my_total+=numbers[i][99-i]

        if max_value < my_total:
            max_value = my_total

    print(f'#{t} {max_value}')