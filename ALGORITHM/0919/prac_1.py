import sys
sys.stdin = open('example.text')

T = int(input())

for t in range(1,T+1):
    NUM = input()
    NUM_LIST = []
    for i in range(0,len(NUM),7):
        NUM_LIST.append(NUM[i:i+7])

    ANS_LIST = []

    for i in range(len(NUM_LIST)):
        ANS = 0
        for j in range(len(NUM_LIST[i])-1,-1,-1):
            if int(NUM_LIST[i][j]) == 1:
                ANS+= 2**((len(NUM_LIST[i])-1)-j)
        ANS_LIST.append(ANS)
    print(*ANS_LIST)