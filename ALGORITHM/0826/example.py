import sys
sys.stdin=open('BECK_17.text')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

ret = 0
fwd = lst[0]
for i in range(len(lst)):                       # 앞 ~ max까지 구간 넓이 계산
    if lst[i][1] > fwd[1]:
        ret += fwd[1]*(lst[i][0] - fwd[0])
        fwd = lst[i]

bwd = lst[-1]
for i in range(len(lst)-1, -1, -1):             # 뒤 ~ max까지 구간 넓이 계산
    if lst[i][1] > bwd[1]:
        ret += bwd[1]*(bwd[0] - lst[i][0])
        bwd = lst[i]

ret += fwd[1]*(bwd[0]+1 - fwd[0])               # max구간 넓이 계산

print(ret)