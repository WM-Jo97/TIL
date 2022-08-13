import sys
sys.stdin = open('input.txt')   #표준 입력에 input.txt 파일을 넣겠다

# number = int(input())
# res = '홀수' if number % 2 else '짝수'
# print(f'{res}')


#  정수가 1개
# 이상이라면 공백으로 구분되서 입력되어 진다.
# 입력되는 두 수를 더하시오.
#l = []
#l = list(map(int, input().split()))  # 1,   2
#print(l)

N = int(input())

lists = []
for _ in range(N):
    lists.append(list(map(int,input().split())))

print(lists)