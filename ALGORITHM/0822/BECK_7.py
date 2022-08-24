import sys
sys.stdin=open('BECK_7.text')

N, M = map(int, input().split())
Arr=[[0]*N for _ in range(M)]

K = int(input())

CUT_X = []
CUT_Y = []
for i in range(K):
    A,B = map(int,input().split())

    if A == 1:
        CUT_Y.append(B)
    else:
        CUT_X.append(B)
CUT_X.append(0)
CUT_X.append(M)
CUT_Y.append(0)
CUT_Y.append(N)

if len(CUT_X) > 1:
    for i in range(len(CUT_X)):
        for j in range(len(CUT_X)-1):
            if CUT_X[j]>CUT_X[j+1]:
                CUT_X[j],CUT_X[j+1] = CUT_X[j+1], CUT_X[j]

if len(CUT_Y) > 1:
    for x in range(len(CUT_Y)):
        for y in range(len(CUT_Y)-1):
            if CUT_Y[y]> CUT_Y[y+1]:
                CUT_Y[y],CUT_Y[y+1] = CUT_Y[y+1], CUT_Y[y]

count=1
for x in range(len(CUT_X)-1):
    count+=1
    for y in range(len(CUT_Y)-1):
        count+=1
        for j in range(CUT_Y[y], CUT_Y[y + 1]):
            for i in range(CUT_X[x],CUT_X[x+1]):
                Arr[i][j]=count

Max=[]
for i in range(M):
    Max.append(max(Arr[i]))

count_list=[]
for t in range(max(Max)+1):
    count=0
    for i in range(M):
        for j in range(N):
            if Arr[i][j] == t:
                count+=1
    count_list.append(count)

print(max(count_list))