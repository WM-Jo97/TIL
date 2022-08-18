import sys
sys.stdin = open('4869.text')

def paper(n):
    if n == 1:
        return 1
    if n % 2:
        return 2*paper(n-1) -1
    else:
        return 2*paper(n-1) +1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N = N//10
    print(f'#{tc} {paper(N)}')