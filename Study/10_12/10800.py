import sys
sys.stdin=open('example_10800.text')

from sys import stdin
input = stdin.readline

N = int(input())
BALL = []
BALL_ORI = []
for i in range(N):
    A, B = map(int,input().split())
    BALL.append([B,A,i])
BALL.sort()
print(BALL)

VALUE = 0
COLOR = [0]*(N+1)
PRE = 0
PRE_COLOR = 0

for j in range(N):
    B, A = BALL[j][0] , BALL[j][1]
    C = VALUE - COLOR[A]
    if PRE == B and PRE_COLOR == A:
        VALUE -= B
        COLOR[A] -= B
        BALL[j].append(VALUE-COLOR[A])
        VALUE += B
    elif PRE == B:
        VALUE -= B
        BALL[j].append(VALUE-COLOR[A])
        VALUE += B
    else:
        BALL[j].append(C)
    COLOR[A] += B
    VALUE += B
    PRE = B
    PRE_COLOR = A

BALL.sort(key=lambda x:x[2])
for i in range(N):
    print(BALL[i][3])