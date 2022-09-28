import sys
sys.stdin = open('example_1.text')

def GO_CAL(CAL_num, N,M,NUMBER):
    global ANS_NUM

    if N == M:
        if ANS_NUM > NUMBER-1:
            ANS_NUM = NUMBER-1
            print(ANS_NUM)
            return
        else:
            return

    else:
        if NUMBER > ANS_NUM:
            return
        else:
            if N <= 0:
                return
            elif N > M:
                if CAL_num == 0:
                    return
                elif CAL_num == 1:
                    return
                elif CAL_num == 2:
                    N = N-1
                elif CAL_num == 3:
                    N = N-10

                for i in range(4):
                    GO_CAL(i,N,M,NUMBER+1)
                    if i == 0:
                        N = N-1
                    elif i == 1:
                        N = N//2
                    elif i == 2:
                        N =N+1
                    elif i == 3:
                        N=N+10
                return

            else:
                if CAL_num == 0:
                    N = N + 1
                elif CAL_num == 1:
                    N = N *2
                elif CAL_num == 2:
                    return
                elif CAL_num == 3:
                    return

                for i in range(4):
                    GO_CAL(i,N,M,NUMBER+1)
                    if CAL_num == 0:
                        N = N-1
                    elif CAL_num == 1:
                        N = N//2
                    elif CAL_num == 2:
                        N = N+1
                    else:
                        N = N +10

                return

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    ANS = N
    CAL = ['+1','*2','-1','-10']
    ANS_NUM = 10000
    for i in range(len(CAL)):
        GO_CAL(i,N,M,0)
        N = ANS

    print(ANS_NUM)