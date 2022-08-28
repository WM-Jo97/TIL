import sys
sys.stdin=open('BECK_19_2.text')

for i in range(4):
    SQ_1_X,SQ_1_Y,SQ_2_X,SQ_2_Y,SQ_3_X,SQ_3_Y,SQ_4_X,SQ_4_Y = map(int,input().split())

    if SQ_1_X > SQ_3_X:
        SQ_1_X,SQ_1_Y,SQ_2_X,SQ_2_Y,SQ_3_X,SQ_3_Y,SQ_4_X,SQ_4_Y = SQ_3_X,SQ_3_Y,SQ_4_X,SQ_4_Y,SQ_1_X,SQ_1_Y,SQ_2_X,SQ_2_Y

    if (SQ_2_X == SQ_3_X) and ((SQ_2_Y == SQ_3_Y) or (SQ_1_Y == SQ_4_Y)):
        result = 'c'
    elif (SQ_2_X < SQ_3_X) or (SQ_2_Y < SQ_3_Y) or (SQ_1_Y > SQ_4_Y):
        result = 'd'
    elif ((SQ_3_X < SQ_2_X) and ((SQ_1_Y == SQ_4_Y) or (SQ_2_Y == SQ_3_Y))) or ((SQ_2_X == SQ_3_X) and ((SQ_2_Y > SQ_3_Y) or (SQ_4_Y > SQ_1_Y))):
        result = 'b'
    else:
        result = 'a'
    print(result)