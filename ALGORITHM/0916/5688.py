import sys
sys.stdin=open('example_4.text')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    ANS = round(N**(1/3),6)
    if abs(int(ANS)-ANS) > 0.000001:
        print(f'#{t} -1')
    else:
        print(f'#{t} {int(ANS)}')





