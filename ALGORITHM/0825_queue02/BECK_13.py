"""
1 : 동쪽
2 : 서쪽
3 : 남쪽
4 : 북쪽
"""

import sys
sys.stdin=open('BECK_13.text')

N = int(input())

Arr=[]
x=0
y=0
for i in range(6):
    Dir, Inst = map(int,input().split())
    if Dir == 4:
        y,x = y+Inst,x
    elif Dir == 3 :
        y,x = y-Inst,x
    elif Dir == 1 :
        y,x = y, x+Inst
    elif Dir == 2 :
        y,x = y, x-Inst
    Arr.append([y,x])

X_size=[]
Y_size=[]
for i in Arr:
    if i[0] == 3 or 4:
        X_size.append(i[1])
    elif i[0] == 1 or 2:
        Y_size.append(i[1])

max(X_size)

print(Arr)

