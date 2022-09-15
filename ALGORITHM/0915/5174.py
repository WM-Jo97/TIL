import sys
sys.stdin=open('example_1.text')

def preorder(n, count):
    if n:
        preorder(SON1[n],count)
        preorder(SON2[n],count)
        count.append(1)


T = int(input())
for t in range(1,T+1):
    E , N = map(int,input().split())
    arr = list(map(int,input().split()))

    SON1 = [0]*(E+2)
    SON2 = [0]*(E+2)

    for i in range(E):
        P,C = arr[i*2], arr[i*2+1]
        if SON1[P] == 0:
            SON1[P] = C
        else:
            SON2[P] = C
    count = []
    preorder(N , count)
    print(f'#{t} {sum(count)}')
