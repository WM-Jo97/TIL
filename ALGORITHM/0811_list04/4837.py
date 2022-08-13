import sys
sys.stdin=open('4837.text')

T = int(input())
A=list(range(1,13))

for t in range(1,T+1):
    N,K=(map(int,input().split()))   # N = 요소의 갯수 K = 요소끼리의 합
    Num=12                           # 1~ 12 니까 주어진 숫자의 갯수
    Group_2D=[]                      # 2차원리스트
    for i in range(1<<Num):          # 부분집합들을 모아놓은 리스
        Group = []
        for j in range(Num):
            if i&(1<<j):
                Group.append(A[j])
        Group_2D.append(Group)

    ans_count = 0
    for i in Group_2D:
        ele_count=0
        ele_total=0
        for j in i:
            ele_count+=1
            ele_total+=j

        if ele_count==N and ele_total==K:
            ans_count+=1

    print(f'#{t} {ans_count}')

