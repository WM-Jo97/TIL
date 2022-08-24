import sys
sys.stdin = open('BECK_11.text')

C, R = map(int,input().split())
Arr = [[0]*C for _ in range(R)]
K = int(input())
Q = 1
i=0
NN = 0
while True:
    for j in range(R-1,-1,-1):
        if Arr[j][i]==0:
            Arr[j][i]=Q
            Q+=1
            NN+=1
    for n in range(C):
        if Arr[i][n]==0:
            Arr[i][n]=Q
            Q+=1
            NN+=1
    for m in range(R):
        if Arr[m][C-1-i]==0:
            Arr[m][C-1-i]=Q
            Q+=1
            NN+1
    for k in range(C-1,-1,-1):
        if Arr[R-1-i][k]==0:
            Arr[R-1-i][k]=Q
            Q+=1
            NN+=1
    i+=1
    if i==C-1 or i==R-1 or NN==C*R:
        break

Ans=[]
for i in range(C):
    for j in range(R):
        if Arr[j][i] == K:
            Ans.append(i+1)
            Ans.append(R-j)

if not Ans:
    print(0)
else:
    print(*Ans)


