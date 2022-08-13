import sys

sys.stdin = open('practice1.text')

N = int(input())

for t in range(1,N+1):
    SQ=int(input())
    SQ_group=[]
    for i in range(SQ):
        ROW=list(map(int,input().split()))
        SQ_group.append(ROW)

    # 2차원 리스트를 통해서 체크형 방들 만들기 완료.

    def Abs(number):
        if number >=0:
            return number
        else:
            return -number

    di = [0, 1, 0, -1] # 델타 사용해서 우하좌상 순서로 확인 (오늘 배운 내용이라 우하좌상 순서, 순서 변경 가능)
    dj = [1, 0, -1, 0]
    Delta=[]
    Delta_ele=[]
    for i in range(SQ):
        for j in range(SQ):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < SQ and 0 <= nj <SQ: #반드시 0보다 크거나 같아야함. 같은거 빼고 큰거만 하면 첫 행이 통쨰로 출력이 안되요
                    Delta_ele.append(Abs(SQ_group[ni][nj]-SQ_group[i][j]))
    total=0
    for i in Delta_ele:
        total+= i

    print(f'#{t} {total}')
