import sys
sys.stdin = open('example_1.text')

def BFS(N,M):
    front = rear = -1 #Queue 의 시작을 위한 초기화
    calculated[N] = 1

    rear += 1
    Q[rear] = N

    while front != rear:       #큐가 비어있는지 확인
        #Q에서 꺼내기 (선형 큐이기에 따로 삭제하지 않아도 됨)
        front += 1
        num = Q[front]
        operator = [num+1, num-1, num*2, num-10]
        
        for i in range(4):
            if operator[i] ==M: #만들려는 M이 완성이 되었다고 하면
                return calculated[num]

            if 0 < calculated[i] <= 1000000:
                if calculated[operator[i]] == 0:
                    calculated[operator[i]] = calculated[num] + 1
                    #QUEUE에 계산해야할 숫자를 추가
                    rear += 1
                    Q[rear] = operator[i]

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())

    Q = [0] * 1000001
    calculated = [0] * 1000001


    res = BFS(N,M)
    print(f'#{t} {res}')