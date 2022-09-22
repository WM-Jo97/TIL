import sys
sys.stdin = open('example_2.text')

N = int(input())
'''
                   1 
1                  1

10                 2               1

101 100            1 2             1

1010 1000 1001     1+ 1 + 2         1 
 
10101 10001 10000 10010 1 + 1 + 2 + 2     2

101010 100010 100000 100001 100100 100101   2 + 2+ 2+ 1+ 2+ 1  2

1010100 1010101 1000100 1000101 1000000 1000001 1000010 1001000 1001001 1001010     4

10101000 10101001 10101010 10001000 10001001 10001010 10000000 1000001 10000010 10000100 10000101 10010000 10010001 10010010 10010100 10010101 6

101010101 100010101 100010000 100010001 100010010 100001010 100001000 100001001 100000101 100000010 100000000 100000001 101010101 13
'''

CHINSU = '1'
ANS = ['1']
COUNT = 0

while True:
    NUM = ANS.pop(0)
    if NUM[-1] == '1':
        CHINSU = NUM + '0'
        if len(NUM) < N:
            ANS.append(CHINSU)
            if CHINSU == N:
                COUNT+=1
        else:
            break

    elif NUM[-1] == '0':
        CHINSU = NUM+'0'
        ANS.append(CHINSU)
        if len(CHINSU) == N:
            COUNT+=1
        CHINSU = NUM+'1'
        ANS.append(CHINSU)
        if len(CHINSU) == N:
            COUNT+=1

        if len(NUM) > N:
            break

print(COUNT)
