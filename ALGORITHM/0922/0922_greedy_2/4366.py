import sys
sys.stdin = open('example_5.text')

def BIT_2_SACN(BIT_2):
    TOTAL = 0
    for i in range(len(BIT_2)-1,-1,-1):
        if BIT_2[i] == 1:
            TOTAL += 2**(len(BIT_2)-1-i)

    return TOTAL

def BIT_3_SCAN(BIT_3):
    TOTAL = 0
    for i in range(len(BIT_3)-1,-1,-1):
        if BIT_3[i] != 0:
            TOTAL += BIT_3[i]*(3**(len(BIT_3)-1-i))
    return TOTAL

def CHECK(BIT_2, BIT_3):
    for i in range(len(BIT_2)):
        B = int(BIT_2[i])
        if BIT_2[i] == 1:
            BIT_2[i] = 0
        else:
            BIT_2[i] = 1
        BIT_2_NUM = BIT_2_SACN(BIT_2)
        if BIT_2_NUM == BIT_3_SCAN(BIT_3):
                return BIT_2_NUM
        else:
            for j in range(len(BIT_3)):
                A = int(BIT_3[j])
                for x in range(3):
                    BIT_3[j] = x
                    BIT_3_NUM = BIT_3_SCAN(BIT_3)
                    if BIT_3_NUM == BIT_2_NUM:
                        return BIT_3_NUM

                BIT_3[j] = A
        BIT_2[i] = B


T = int(input())

for t in range(1,T+1):
    BIT_2 = list(map(int,input()))
    BIT_3 = list(map(int,input()))

    print(f'#{t} {CHECK(BIT_2,BIT_3)}')


