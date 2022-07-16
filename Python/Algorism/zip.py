A=int(input()) #첫째 줄

for i in range(1,A):
    B=i
    data = []
    for i in range(int(B)):
        data.append(list(input().split()))

    X=int(data[0][0])

    for i in range(X):
        data.append(list(input().split()))

    del data[0]

    ANS=[]
    for i in range(0,X):
        ANS.append(data[i][0]*int(data[i][1]))

    PANS=''.join(s for s in ANS)
    LEN=len(PANS)
    unit=10
    QU = [PANS[i:i+unit] for i in range(0,LEN,unit)]

    for i in range(0,X):
        print(QU[i])

