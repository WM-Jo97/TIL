import sys
sys.stdin=open('example_2.text')

def preorder(n,total):
    if n:
        preorder(son1[n],total)
        preorder(son2[n],total)
        total.append(leaf[n])

T = int(input())
for t in range(1,T+1):
    N, M, L = map(int,input().split())
    son1 = [0]*(N+1)
    son2 = [0]*(N+1)
    root = [0]*(N+1)
    for i in range(2,N+1):
        if i%2 == 0:
            for j in range(1,N+1):
                if son1[j] == 0:
                    son1[j] = i
                    break
        elif i%2 == 1:
            for j in range(1, N + 1):
                if son2[j] == 0:
                    son2[j] = i
                    break

    leaf = [0]*(N+1)
    for i in range(M):
        A, B = map(int,input().split())
        leaf[A] = B

    total = []
    preorder(L,total)
    print(f'#{t} {sum(total)}')

