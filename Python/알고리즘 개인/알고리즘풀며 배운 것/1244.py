import copy
T=int(input())

for t in range(1,T+1):
    A=list(input().split(' '))
    B=[]
    for i in A[0]:
        B.append(i)
    print(B)
    Deep_copy = copy.deepcopy(B)

    ANS=[]
    for i in range(int(A[1])):
       
        for j in range(len(B)):
            B=copy.deepcopy(Deep_copy)
            B[i],B[j] = B[j], B[i]
            ANS.append(B)

    print(ANS)