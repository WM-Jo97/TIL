import sys
sys.stdin = open('example_3.text')

N,C = map(int,input().split())

num_list = []
for i in range(N):
    num_list.append(int(input()))

print(num_list)

num_list.sort()
print(num_list)