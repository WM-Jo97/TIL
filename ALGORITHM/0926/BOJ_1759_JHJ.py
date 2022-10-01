import sys
sys.stdin = open('example_1.text')

from itertools import combinations

L,C = map(int,input().split())
alpa = list(input().split())

a_list = ['a','e','i','o','u'] # 모음으로 이루어진 리스트

password = list(combinations(alpa,L))  # alph 에서 L개를 뽑는 comination 이용

PASS_LIST = []

PASSWORD_LIST = []
for i in range(len(password)):
    TEMP = []
    for j in range(len(password[i])):
        TEMP.append(password[i][j])
    PASSWORD_LIST.append(TEMP)
print(PASSWORD_LIST)

for i in range(len(PASSWORD_LIST)):
    count = 0
    word = ''
    PASSWORD_LIST[i].sort()           # 각각의 리스트들에 대해서

    for j in range(len(PASSWORD_LIST[i])):
        word += PASSWORD_LIST[i][j]          # 출력하기 편하게 편집
        if PASSWORD_LIST[i][j] in a_list:    # 모듬에 있으면
            count += 1

    if 1<= count <L-1:                       # 모음이 하나 이상이고 전체에서 2개를 제외한 갯수 이하이면
        PASS_LIST.append(word)

PASS_LIST.sort()                           # 출력을 위한 정렬
for i in PASS_LIST:
    print(i)
