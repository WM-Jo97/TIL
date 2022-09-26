import sys
sys.stdin = open('example_1.text')

from itertools import combinations

L,C = map(int,input().split())
alpa = list(input().split())

a_list = ['a','e','i','o','u']

password = list(combinations(alpa,L))

PASS_LIST = []

PASSWORD_LIST = []
for i in range(len(password)):
    TEMP = []
    for j in range(len(password[i])):
        TEMP.append(password[i][j])
    PASSWORD_LIST.append(TEMP)

for i in range(len(PASSWORD_LIST)):
    count = 0
    word = ''
    PASSWORD_LIST[i].sort()

    for j in range(len(PASSWORD_LIST[i])):
        word += PASSWORD_LIST[i][j]
        if PASSWORD_LIST[i][j] in a_list:
            count += 1

    if 1<= count <L-1:
        PASS_LIST.append(word)

PASS_LIST.sort()
for i in PASS_LIST:
    print(i)
