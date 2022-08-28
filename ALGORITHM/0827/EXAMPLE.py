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
    print(SQ)
    if SQ[0][0] < SQ[2][0]:
        if SQ[1][0] == SQ[2][0]:
            Tem = SQ[2][1]
            print(Tem , SQ[0][1] , SQ[1][1])
            if SQ[0][1] <= Tem < SQ[1][1]:
                print('b')
                check = True
        elif SQ[1][0] == SQ[2][0] and (SQ[0][1] < SQ[3][1] <= SQ[1][1]):
            print('b')
            check = True
        elif SQ[1][1] == SQ[2][1] and (SQ[0][0] <= SQ[2][1] < SQ[1][0]):
            print('b')
            check = True