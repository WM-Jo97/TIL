import sys
sys.stdin = open('example_1.text')

def f(i,k):
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri+=1
        if card[0]+1 == card[1] and card[1]+1 == card[2]:
            run += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri+=1
        if card[3]+1 == card[4] and card[4]+1 == card[5]:
            run += 1
        if tri+run == 2:
            return True
        else:
            return False

    else:
        for j in range(i, k):
            card[i], card[j] = card[j] , card[i]
            if f(i+1,k):
                return True
            card[i], card[j] = card[j], card[i]
        return False


T = int(input())

for t in range(1,T+1):
    card = list(map(int,input()))
    ans = f(0,6)

    print(f'#{t} {ans}')


