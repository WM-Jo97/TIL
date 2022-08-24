import sys
sys.stdin=open('BECK_9.text')

Arr=[]
for _ in range(5):
    TEMP=list(map(int,input().split()))
    Arr.append(TEMP)

MC=[]
for _ in range(5):
    TEMP=list(map(int,input().split( )))
    MC.append(TEMP)

ANSWER=[]
LEN=[]

for i in range(5):
    for j in range(5):
        A = MC[i][j]
        LEN.append(A)
        for x in range(5):
            for y in range(5):
                bingo_num = 0
                if Arr[x][y]==A:
                    Arr[x][y]='*'
                    break

        for n in range(5):
            count_x = 0
            for m in range(5):
                if Arr[n][m] == '*':
                    count_x+=1
                if count_x==5:
                    bingo_num+=1

        for Q in range(5):
            count_y = 0
            for W in range(5):
                if Arr[W][Q] == '*':
                    count_y+=1
                if count_y==5:
                    bingo_num+=1

        count_cross_1=0
        for P in range(5):
            if Arr[P][P]=='*':
                count_cross_1 +=1

        count_cross_2=0
        for f in range(5):
            if Arr[4-f][f] == '*':
                count_cross_2 +=1


        if count_cross_1==5:
            bingo_num+=1

        if count_cross_2 == 5:
            bingo_num+=1

        if bingo_num>=3:
            ANSWER.append(len(LEN))

print(ANSWER[0])
