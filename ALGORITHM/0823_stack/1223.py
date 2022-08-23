import sys
sys.stdin=open('1223.text')

T=10
for t in range(1,T+1):
    N=int(input())
    NUM = []
    CUL = []
    line = input()
    TEMP=[]

    pri = {'+' : 0,
           '*' : 1
           }

    for i in line:
        if i == '+':
            if CUL:
                if pri.get(CUL[-1]) <= pri.get('+'):
                    CUL.append(i)
                else:
                    while True:
                        if CUL:
                            if pri.get(CUL[-1]) > pri.get('+'):
                                NUM.append(CUL.pop())
                            else:
                                CUL.append(i)
                                break
                        else:
                            CUL.append(i)
                            break
            else:
                CUL.append(i)
        elif i == '*':
            CUL.append(i)
        else:
            NUM.append(i)

    for j in range(len(CUL)):
        NUM.append(CUL.pop())

    for x in NUM:
        if x == '+':
            TEMP.append(CUL.pop())
            TEMP.append(CUL.pop())
            CUL.append(int(TEMP[0]) + int(TEMP[1]))
            TEMP=[]

        elif x == '*':
            TEMP.append(CUL.pop())
            TEMP.append(CUL.pop())
            CUL.append(int(TEMP[0]) * int(TEMP[1]))
            TEMP = []
        else:
            CUL.append(x)

    print(f'#{t} {CUL[0]}')