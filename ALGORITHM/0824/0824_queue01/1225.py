import sys
sys.stdin=open('1225.text')

def PASSWORD(NUM):
    while True:
        for i in range(1,6):
            TEMP=NUM.pop(0)-i
            if TEMP>0:
                NUM.append(TEMP)
            else:
                NUM.append(0)
                return NUM

T = 10

for _ in range(T):
    t = int(input())
    NUM = list(map(int,input().split()))

    print(f'#{t}',end=' ')
    for i in PASSWORD(NUM):
        print(i, end=' ')
    print()