import sys
sys.stdin=open('BECK_15.text')

NUM, DAY = map(int,input().split())
TEMP = list(map(int,input().split()))


Arr=[]
for i in range(len(TEMP)-(DAY-1)):
    ANS = 0
    for j in range(DAY):
        ANS+=TEMP[i+j]
    Arr.append(ANS)


print(max(Arr))