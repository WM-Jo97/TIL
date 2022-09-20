import sys
sys.stdin = open('example_2.text')

T = int(input())

for t in range(1,T+1):
    NUM = float(input())

    BIT = ''
    idx = 1
    while True:
        if NUM-2**(-idx)>=0:
            BIT = BIT+'1'
            NUM = NUM-2**(-idx)
            idx +=1
        else :
            BIT = BIT+'0'
            idx +=1

        if NUM == 0:
            print(f'#{t} {BIT}')
            break

        if len(BIT) >= 13:
            print(f'#{t} overflow')
            break