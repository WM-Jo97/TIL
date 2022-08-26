import sys
sys.stdin=open('BECK_15.text')

NUM, DAY = map(int,input().split())
TEMP = list(map(int,input().split()))

Arr=[]
ANS = 0
for j in range(DAY):
    ANS+=TEMP[j]

Arr.append(ANS)

for i in range(1,NUM-(DAY-1)):
    ANS = ANS-TEMP[i-1]+TEMP[i+(DAY-1)]
    Arr.append(ANS)

print(max(Arr))

