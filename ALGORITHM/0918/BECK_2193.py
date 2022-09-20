import sys
sys.stdin = open('example_2.text')

N = int(input())
'''
1  1 
10 2
101 100  5 4
1010 1000 1001 10 8 9

10101 10001 10000 10101
'''
CHINSU = '1'
ANS = ['1']
KEY = 0

while True:
    if CHINSU[-1] == '1':
        CHINSU = CHINSU+'0'
        if len(CHINSU) <= N:
            ANS.append(CHINSU)
            KEY = len(CHINSU)
        else:
            break
    elif CHINSU[-1] == '0':
        CHINSU = ANS[-1]+'0'
        ANS.append(CHINSU)
        CHINSU = ANS[-2]+'1'
        ANS.append(CHINSU)

        if len(CHINSU) > N:
            ANS.pop(-1)
            ANS.pop(-1)
            break
        else:
            KEY = len(CHINSU)

print(KEY)
print(ANS)
print(len(ANS)-KEY)