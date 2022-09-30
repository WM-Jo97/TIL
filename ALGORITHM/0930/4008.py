import sys
sys.stdin = open('example_4008.text')

from itertools import permutations

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    number = list(map(int,input().split()))

    calculate = []
    for i in range(len(arr)):
        if i == 0:
            for _ in range(arr[i]):
                calculate.append('+')
        elif i == 1:
            for _ in range(arr[i]):
                calculate.append('-')
        elif i == 2:
            for _ in range(arr[i]):
                calculate.append('*')
        elif i == 3:
            for _ in range(arr[i]):
                calculate.append('/')

    P_list = list(permutations(calculate,N-1))

    MAX = -10000
    MIN = 100000
    for i in range(len(P_list)):
        CAL_LIST = [number[0]]
        for j in range(N-1):
            CAL_LIST.append(P_list[i][j])
            CAL_LIST.append(number[j+1])


        for i in range(len(CAL_LIST)):
            if CAL_LIST[i] == '+':
                CAL_LIST[i+1] = CAL_LIST[i-1]+CAL_LIST[i+1]
            elif CAL_LIST[i] == '-':
                CAL_LIST[i+1] = CAL_LIST[i-1]-CAL_LIST[i+1]
            elif CAL_LIST[i] == '*':
                CAL_LIST[i+1] = CAL_LIST[i-1]*CAL_LIST[i+1]
            elif CAL_LIST[i] == '/':
                CAL_LIST[i+1] = int(CAL_LIST[i-1]/CAL_LIST[i + 1])


        A = CAL_LIST[-1]
        if A < MIN:
            MIN = A

        if A > MAX:
            MAX = A

    print(f'#{t} {MAX-MIN}')
