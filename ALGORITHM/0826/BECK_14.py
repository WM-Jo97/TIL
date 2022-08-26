import sys
sys.stdin=open('BECK_14.text')

Fruit = int(input())
Stack=[]
Arr = []
Sm=[]
Arr_2=[]

for _ in range(6):
    Dir, Dist = map(int, input().split())
    Arr_2.append([Dir, Dist])

for i in range(2):
    for i in Arr_2:
        Arr.append(i)


max_1=0
max_2=0
for j in Arr:
    if j[0]==1 or j[0]==2:
        if j[1]>=max_1:
            max_1=j[1]
    if j[0]==3 or j[0]==4:
        if j[1]>=max_2:
            max_2=j[1]

Bg_SQ=max_1*max_2

for i in range(len(Arr)-3):
    if Arr[i][0]==Arr[i+2][0]:
        if Arr[i+1][0]==Arr[i+3][0]:
            Sm_SQ=Arr[i+1][1]*Arr[i+2][1]

print((Bg_SQ-Sm_SQ)*Fruit)

