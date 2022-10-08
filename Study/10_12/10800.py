import sys
sys.stdin=open('example_10800.text')

from sys import stdin
input = stdin.readline

N = int(input())
BALL = []
for i in range(N):
    A, B = map(int,input().split())
    BALL.append([A,B,0])

for i in range(N):
    for j in range(N):
        if BALL[i][0] != BALL[j][0] and BALL[i][1] > BALL[j][1]:
            BALL[i][2] += BALL[j][1]

for i in range(N):
    print(BALL[i][2])
