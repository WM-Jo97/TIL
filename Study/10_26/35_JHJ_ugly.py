import sys
sys.stdin = open('example_5.text')

N = int(input())

Dp_table = [0]*N
Dp_table[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for i in range(1,N):
    Dp_table[i] =min(next2,next3,next5)

    if Dp_table[i] == next2:
        i2 += 1
        next2 = Dp_table[i2]*2
    if Dp_table[i] == next3:
        i3 += 1
        next3 = Dp_table[i3] *3
    if Dp_table[i] == next5:
        i5 += 1
        next5 = Dp_table[i5] *5

print(Dp_table[N-1])