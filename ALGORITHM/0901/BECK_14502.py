import sys
sys.stdin = open('example.text')

from itertools import combinations

N, M = map(int,input().split())

Arr = []

for i in range(N):
    A = list(map(int,input().split()))
    Arr.append(A)

print(Arr)

blank_list = []
for i in range(N):
    for j in range(M):
        if Arr[i][j] == 0:
            blank_list.append([i,j])

print(blank_list)
n = len(blank_list)

Combi = list(combinations(blank_list,3))

for i in range(len(Combi)):
    for j in range(3):


"""
for i in range(1<<n):
    for j in range(n):
        Num_list = []
        if i & (1<<j):
            print(blank_list[j], end=', ')
    print()
print()
"""