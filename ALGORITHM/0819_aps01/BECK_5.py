import sys
sys.stdin=open('BECK.text')

N=int(input())
SQ_list=[]
for i in range(N):
    SQ=list(map(int,input().split()))
    SQ_list.append(SQ)

Arr=[[0]*1002 for _ in range(1002)]

for i in range(len(SQ_list)):
    A=[]
    for j in range(0,len(SQ_list[i]),2):
        A.append([SQ_list[i][j],SQ_list[i][j+1]])
    A[1][0]=A[1][0]+A[0][0]
    A[1][1]=A[1][1]+A[0][1]

    for x in range(A[0][0],A[1][0]):
        for y in range(A[0][1],A[1][1]):
            Arr[x][y]=i+1

count=[[] for _ in range(len(SQ_list))]

for i in range(1002):
    for j in range(1002):
        for n in range(1,len(SQ_list)+1):
            if Arr[i][j]==n:
                count[n-1].append(n)

for i in count:
    count_paper = 0
    for _ in i:
        count_paper+=1
    print(count_paper)

