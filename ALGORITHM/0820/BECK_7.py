import sys
sys.stdin=open('BECK_7.text')

from itertools import combinations

NUMS=[]
for _ in range(9):
    A=int(input())
    NUMS.append(A)

NUM_list=list(combinations(NUMS,7))
for i in NUM_list:
    if sum(i)==100:
        LIST=list(i)


LIST.sort()
for i in LIST:
    print(i)