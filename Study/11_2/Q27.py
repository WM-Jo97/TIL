import sys
sys.stdin = open('example_1.text')

N, x = map(int,input().split())
NUM_LIST = list(map(int,input().split()))

front_number = 0
end_number = N-1

f_num = x-1
b_num = x+1

front_index = 0
back_index = 0


if NUM_LIST[0] == x:
    while True:
        middle_number = (front_number + end_number) // 2
        if NUM_LIST[middle_number] < b_num:
            front_number = middle_number + 1

        elif NUM_LIST[middle_number] > b_num:
            end_number = middle_number - 1

        elif NUM_LIST[middle_number] == b_num:
            back_index = middle_number
            break
    print(back_index-1)

elif NUM_LIST[-1] == x:
    while True:
        middle_number = (front_number + end_number) // 2
        if NUM_LIST[middle_number] < f_num:
            front_number = middle_number + 1

        elif NUM_LIST[middle_number] > f_num:
            end_number = middle_number - 1

        elif NUM_LIST[middle_number] == f_num:
            front_index = middle_number
            break
    print(N-1 - front_index)

else:
    while True:
        middle_number = (front_number + end_number)//2
        if NUM_LIST[middle_number] < b_num:
            front_number = middle_number+1

        elif NUM_LIST[middle_number] > b_num:
            end_number = middle_number-1

        elif NUM_LIST[middle_number] == b_num:
            back_index = middle_number
            break

    front_number = 0
    end_number = N - 1
    while True:
        middle_number = (front_number + end_number)//2
        if NUM_LIST[middle_number] < f_num:
            front_number = middle_number+1

        elif NUM_LIST[middle_number] > f_num:
            end_number = middle_number-1

        elif NUM_LIST[middle_number] == f_num:
            front_index = middle_number
            break
    print(back_index - front_index - 1)