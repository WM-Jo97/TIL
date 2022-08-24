import sys
sys.stdin=open('BECK_12.text')


def Check(P, Q):
    dx = [1, -1, -1, -1]
    dy = [1, 1, -1, 1]
    t = 1
    ANSWER = []
    while True:
        for k in range(4):
            x = P + dx[k]
            y = Q + dy[k]
            while True:
                if W + 1 > x >= 0 and H + 1 > y >= 0 and Arr[y][x] == 0:
                    t += 1
                    P = x
                    Q = y
                    ANSWER.append(t)
                    ANSWER.append((Q, P))
                    x = P + dx[k]
                    y = Q + dy[k]
                    if t == T+1:
                        return ANSWER
                else:
                    break


W,H = map(int, input().split())
P,Q = map(int, input().split())
T= int(input())

Arr=[[0]*(W+1) for _ in range(H+1)]


NUM_List = Check(P,Q)
print(NUM_List)
for i in range(len(NUM_List)):
    if NUM_List[i]==T+1:
        print(f'{NUM_List[i+1][-1]} {NUM_List[i+1][0]}')