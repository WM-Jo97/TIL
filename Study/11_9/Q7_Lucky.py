import sys
sys.stdin = open('example_1.text')

Score = input()
Num_list = list(map(int,Score))

N = len(Num_list)//2
if sum(Num_list[0:N]) == sum(Num_list[N:]):

    print('LUCKY')
else:
    print('READY')