import sys
sys.stdin = open('example_3.text')


def perm(money, c):
    global res
    temp = ''
    for mon in money:
        temp += mon
    if int(temp) in res[c]:
        return
    else:
        res[c].append(int(temp))
    if c == 0:
        return

    for i in range(len(money)):
        for j in range(i+1, len(money)):
            money[i], money[j] = money[j], money[i]
            perm(money,c-1)
            money[i], money[j] = money[j], money[i]

t = int(input())
for tc in range(1, t+1):

    money, c = input().split()
    money = list(money)
    res = [[] for _ in range(int(c)+1)]
    perm(money, int(c))
    print(f'#{tc} {max(res[0])}')