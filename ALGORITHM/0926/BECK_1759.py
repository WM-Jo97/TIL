import sys
sys.stdin = open('example_1.text')

from itertools import combinations

L,C = map(int,input().split())
alpa = list(input().split())

a_list = ['a','e','i','o','u']

print(alpa)

password = list(combinations(alpa,L))
for i in range(len(password)):
    if password[i] in


print(password)