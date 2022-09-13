import sys
sys.stdin = open('example.text')

N= int(input())

Res = []
Price = []
Pay = [0]*(N)

for i in range(N):
    T, P = map(int,input().split())
    Res.append(T)
    Price.append(P)

Pay_total = 0
for i in range(N):
    if (i+1) >= Res[N-1-i]:
        for j in range(N-1-i,N-1-i+Res[N-1-i]):
            if Pay[j] != 0:
                Pay_ex = 0
                for x in range(N-1-i,(N-1-i)+Res[N-1-i]):
                    Pay_ex += Pay[x]
                if Pay_ex < Price[N-1-i]:
                    Pay_total -= Pay_ex
                    Pay_total += Price[N-1-i]
                    for y in range(N-1-i,(N-1-i)+Res[N-1-i]):
                        if y == N-1-i:
                            Pay[y] = Price[N-1-i]
                        else:
                            Pay[y] = 0
                break
        else:
            Pay_total += Price[N-1-i]
            for x in range(N-1-i,(N-1-i)+Res[N-1-i]):
                if x == N-1-i:
                    Pay[x] = Price[N-1-i]
                else:
                    Pay[x] = 0

print(Pay_total)