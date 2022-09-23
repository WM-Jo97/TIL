import sys
sys.stdin = open('example_1.text')

def month_3(CHECK, idx):
    if idx == 12:
        return
    elif idx == 11:
        check_3[idx] = CHECK[idx]
        month_3(CHECK,idx+1)
    elif idx == 10:
        check_3[idx] = (CHECK[idx]+CHECK[idx+1])
        month_3(CHECK,idx+1)
    else:
        if CHECK[idx] == 0:
            check_3[idx] = (CHECK[idx] + CHECK[idx + 1] + CHECK[idx + 2])
            month_3(CHECK, idx+1)
        else:
            check_3[idx]=(CHECK[idx] + CHECK[idx+1] + CHECK[idx+2])
            month_3(CHECK, idx+1)

def year(YEAR,check_3,idx):
    if idx == 12:
        return
    else:
        for i in range(len(YEAR)):
            YEAR[i] = CHECK[i]

        if check_3[idx] != 0 and check_3[idx] >= PRICE[2]:
            YEAR[idx] = PRICE[2]
            if idx== 11:
                pass
            elif idx == 10:
                YEAR[idx+1] = 0
            else:
                YEAR[idx+1] = YEAR[idx+2] = 0
        ANS.append(sum(YEAR))
        year(YEAR,check_3,idx+1)

        if idx+2 < 12 and check_3[idx+2] !=0 and check_3[idx] >= PRICE[2]:
            YEAR[idx+2] = PRICE[2]
            if idx == 0:
                pass
            elif idx == 1:
                YEAR[idx - 1] = 0
            else:
                YEAR[idx + 1] = YEAR[idx + 2] = 0

        for j in range(idx,11):
            if idx+3+j <= 11 and check_3[idx+3+j]!=0 and check_3[idx+3+j] >= PRICE[2]:
                for i in range(len(YEAR)):
                    YEAR[i] = CHECK[i]
                if check_3[idx] != 0 and check_3[idx] >= PRICE[2]:
                    YEAR[idx] = PRICE[2]
                    if idx == 11:
                        pass
                    elif idx == 10:
                        YEAR[idx + 1] = 0
                    else:
                        YEAR[idx + 1] = YEAR[idx + 2] = 0

                YEAR[idx+3+j] = PRICE[2]
                if idx+3+j == 11:
                    pass
                elif idx+3+j == 10:
                    YEAR[idx + 4+j] = 0
                else:
                    YEAR[idx + 4+j] = YEAR[idx + 5+j] = 0
                ANS.append(sum(YEAR))
                for x in range(idx+3+j,11):
                    if 3+x <= 11 and check_3[3+x] != 0 and check_3[3+x] > PRICE[2]:
                        YEAR[3+x] = PRICE[2]
                        if 3+x == 11:
                            pass
                        elif 3+x == 10:
                            YEAR[4+x] = 0
                        else:
                            YEAR[4+x] = YEAR[5+x] = 0
                        ANS.append(sum(YEAR))
                        for y in range(3+x,11):
                            if y+3 <= 11 and check_3[y+3] != 0 and check_3[y+3] > PRICE[2]:
                                YEAR[y+3] = PRICE[2]
                                if y+3 == 11:
                                    pass
                                elif y+3 == 10:
                                    YEAR[y+4] = 0
                                else:
                                    YEAR[y+4] = YEAR[y+5] = 0
                                ANS.append(sum(YEAR))
                                break
                        else:
                            break
                    else:
                        break
            else:
                break


T = int(input())

for t in range(1,T+1):
    PRICE = list(map(int,input().split()))
    Plan = list(map(int,input().split()))

    CHECK = [0]*12

    for i in range(len(Plan)):
        if Plan[i] != 0:
            if Plan[i]*PRICE[0] < PRICE[1]:
                CHECK[i] = Plan[i]*PRICE[0]
            else:
                CHECK[i] = PRICE[1]

    check_num  = 0
    check_3 = [0]*12
    month_3(CHECK,0)

    YEAR = [0]*12
    ANS=[]
    year(YEAR,check_3,0)

    ANS.append(PRICE[3])
    #print(CHECK)
    #print(check_3)
    #print(ANS)


    print(f'#{t} {min(ANS)}')

    #20 10 10 5000
    #1 2 2 0 0 9 1 5 0 1 2 3