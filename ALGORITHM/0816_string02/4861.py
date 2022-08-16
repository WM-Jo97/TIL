import sys
sys.stdin=open('4861.text')

T = int(input())

for t in range(1,T+1):
    N,M= map(int,input().split())

    arr=[]
    for i in range(N):
        A=input().split()
        arr.append(A)

# 가로 회문 찾기
    if N>M:
        for x in range(N-M+1):
            for i in range(N):
                check_front = ''
                check_back = ''
                for j in range(M // 2):
                    check_front += arr[i][0][j+x]
                    check_back += arr[i][0][-(j+(N-M))+x - 1]
                if check_front == check_back:
                    print(f'#{t} {arr[i][0][(j+x)-M//2+1:]}')

    else:
        for i in range(N):
            check_front = ''
            check_back = ''
            for j in range(M//2):
                check_front+= arr[i][0][j]
                check_back+= arr[i][0][-j-1]
            if check_front==check_back:
                print(f'#{t} {arr[i][0]}')

#세로 회문 찾기
    if N > M:
        for x in range(N - M + 1):
            for i in range(N):
                check_front = ''
                check_back = ''
                for j in range(M // 2):
                    check_front += arr[j + x][0][i]
                    check_back += arr[-(j+(N-M))+x - 1][0][i]
                if check_front == check_back:
                    answer=''
                    for j in range(M):
                        answer+= arr[j+x][0][i]
                    print(f'#{t} {answer}')
    else:
        for i in range(N):
            check_front = ''
            check_back = ''
            for j in range(M // 2):
                check_front += arr[j][0][i]
                check_back += arr[-(j)-1][0][i]
            if check_front == check_back:
                answer = ''
                for j in range(M):
                    answer += arr[j][0][i]
                print(f'#{t} {answer}')

