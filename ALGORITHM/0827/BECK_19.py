import sys
sys.stdin=open('BECK_19.text')

for i in range(4):
    SQ = []
    TEMP = list(map(int, input().split()))

    for j in range(4):
        Arr=[]
        for k in range(2):
            Arr.append(TEMP[k+2*j])
        SQ.append(Arr)

    POINT_1 = [SQ[0],[SQ[1][0],SQ[0][1]],[SQ[0][0],SQ[1][1]], SQ[1]]
    POINT_2 = [SQ[2],[SQ[3][0],SQ[2][1]],[SQ[2][0],SQ[3][1]], SQ[3]]

    check=False
    count = 0
    for n in range(len(POINT_1)):
        if POINT_1[n] in POINT_2:
            count+=1

    if count == 1:
        print('c')
        check = True
    elif count == 4:
        print('a')
        check = True

    if SQ[0][0] < SQ[2][0]:
        if SQ[0][1] <= SQ[3][1]:
            if SQ[1][0] == SQ[2][0] and SQ[2][1] < SQ[1][1] and check==False:
                print('b')
                check = True
        elif SQ[0][1] >= SQ[3][1]:
            if SQ[1][0] == SQ[2][0] and (SQ[0][1]< SQ[3][1]) and check==False:
                print('b')
                check = True

        if SQ[1][1] == SQ[2][1] and (SQ[2][0] < SQ[1][0]) and check==False:
            print('b')
            check = True

    elif SQ[0][0] > SQ[2][0]:
        if SQ[0][1] <= SQ[3][1]:
            if SQ[0][0] == SQ[3][0] and (SQ[0][1]<SQ[3][1]) and check==False:
                print('b')
                check = True
        if SQ[0][1] >= SQ[3][1]:
            if SQ[0][0] == SQ[3][0] and (SQ[2][1]<SQ[1][1]) and check==False:
                print('b')
                check = True
        if SQ[0][1] == SQ[3][1] and (SQ[0][0]<SQ[3][0]) and check==False:
            print('b')
            check = True

    else:
        pass


    if SQ[0][0] <= SQ[2][0]:
        if (SQ[1][0] > SQ[2][0] and SQ[1][1] > SQ[2][1]) and check == False :
            print('a')
            check = True
        elif (SQ[1][0] > SQ[2][0] and SQ[0][1] < SQ[3][1]) and check == False :
            print('a')
            check = True
        elif SQ[1][0] > SQ[3][0] and (SQ[0][1] < SQ[2][1] and SQ[1][1] > SQ[3][1]) and check == False :
            print('a')
            check = True
        elif (SQ[0][0] < SQ[2][0] < SQ[1][0]) and (SQ[2][1] < SQ[1][1]) and check == False:
            print('a')
            check = True
        elif (SQ[0][0] < SQ[2][0] < SQ[1][0]) and (SQ[0][1] < SQ[3][1]) and check == False:
            print('a')
            check = True
        elif (SQ[0][1] < SQ[2][1] < SQ[1][1]) and (SQ[2][0] < SQ[1][0]) and check == False:
            print('a')
            check = True

    elif SQ[0][0] >= SQ[2][0]:
        if (SQ[1][0] < SQ[2][0] and SQ[0][1] < SQ[2][1]) and check == False :
            print('a')
            check = True
        elif (SQ[1][0] < SQ[2][0] and SQ[0][1] > SQ[3][1]) and check == False:
            print('a')
            check = True
        elif SQ[1][0] < SQ[3][0] and (SQ[0][1] > SQ[2][1] and SQ[1][1] < SQ[3][1]) and check == False :
            print('a')
            check = True
        elif (SQ[2][0] < SQ[0][0] < SQ[3][0]) and (SQ[3][1] > SQ[0][1])and check == False:
            print('a')
            check = True
        elif (SQ[2][0] < SQ[0][0] < SQ[3][0]) and (SQ[1][1] > SQ[2][1])and check == False:
            print('a')
            check = True
        elif (SQ[2][1] < SQ[0][1] < SQ[3][1]) and (SQ[3][0] < SQ[0][0]) and check == False:
            print('a')
            check = True

    if check == False:
        print('d')