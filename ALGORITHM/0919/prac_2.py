import sys
sys.stdin = open('example.text')

T = int(input())

for t in range(1,T+1):
    NUM = input()
    NUM_LIST = []
    for i in range(0,len(NUM),7):
        NUM_LIST.append(NUM[i:i+7])

    print(NUM_LIST)

    ANS_LIST = []

    for i in range(len(NUM_LIST)):

        ZERO_OR_ONE = ''
        for j in range(len(NUM_LIST[i])):
            ANS = 0
            if NUM_LIST[i][j] == 'A' :
                ANS= 10
            elif NUM_LIST[i][j] == 'B' :
                ANS= 11
            elif NUM_LIST[i][j] == 'C' :
                ANS= 12
            elif NUM_LIST[i][j] == 'D' :
                ANS= 13
            elif NUM_LIST[i][j] == 'E' :
                ANS= 14
            elif NUM_LIST[i][j] == 'F' :
                ANS= 15
            else:
                ANS= int(NUM_LIST[i][j])

            while True:
                if ANS==1:
                    ZERO_OR_ONE = ZERO_OR_ONE + '1'
                    break
                elif ANS==0:
                    ZERO_OR_ONE = ZERO_OR_ONE + '0'
                    break
                elif ANS%2 == 0:
                    ZERO_OR_ONE = ZERO_OR_ONE+'1'
                    ANS = ANS//2
                elif ANS%2 == 1:
                    ZERO_OR_ONE = ZERO_OR_ONE+'0'
                    ANS = ANS//2
            ANS_LIST.append(ZERO_OR_ONE)
            ZERO_OR_ONE = ''
    print(ANS_LIST)

