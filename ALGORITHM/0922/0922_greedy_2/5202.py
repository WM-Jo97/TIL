import sys
sys.stdin = open('example_3.text')
T = int(input())

for t in range(1,T+1):
    N = int(input())
    Work_list = []
    for i in range(N):
        S, E =map(int,input().split())
        Work_list.append((E,S))

    Work_list.sort()

    time = 0
    COUNT = 0
    for i in range(N):
        if time <= Work_list[i][1]:
            COUNT += 1
            time = Work_list[i][0]
    print(f'#{t} {COUNT}')