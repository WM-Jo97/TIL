import sys
sys.stdin=open('BECK_20.text')


def MAX_DICE(DICE, NOW_ALPHA):
    MAX_NUM = 0
    DICE_DUP =[]
    for i in range(len(DICE)):
        TEMP=[]
        for j in range(6):
            TEMP.append(DICE[i][j])
        DICE_DUP.append(TEMP)

    for j in range(N):
        DEL = []
        if NOW_ALPHA == DICE[j][0]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][5]
            DEL.append(NOW_ALPHA)

        elif NOW_ALPHA == DICE[j][1]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][3]
            DEL.append(NOW_ALPHA)

        elif NOW_ALPHA == DICE[j][2]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][4]
            DEL.append(NOW_ALPHA)

        elif NOW_ALPHA == DICE[j][3]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][1]
            DEL.append(NOW_ALPHA)

        elif NOW_ALPHA == DICE[j][4]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][2]
            DEL.append(NOW_ALPHA)

        elif NOW_ALPHA == DICE[j][5]:
            DEL.append(NOW_ALPHA)
            NOW_ALPHA = DICE[j][0]
            DEL.append(NOW_ALPHA)

        DICE_DUP[j].remove(DEL[0])
        DICE_DUP[j].remove(DEL[1])
        MAX_NUM+= max(DICE_DUP[j])

    return MAX_NUM

N= int(input())
DICE = []

for i in range(N):
    A, B, C, D, E, F = map(int,input().split())
    #A => F , B => D , C => E

    DICE.append([A,B,C,D,E,F])

X = []
for i in range(1,7):
    X.append(MAX_DICE(DICE, i))

print(max(X))