
import sys
sys.stdin = open('11660.text')

from sys import stdin

N, M = map(int,stdin.readline().split())
Arr = []
for _ in range(N):
    temp = list(map(int,stdin.readline().split()))
    Arr.append(temp)

for i in range(M):
     x_start, y_start ,x_end , y_end = map(int,stdin.readline().split())
     ans = 0
     for x in range(x_start,x_end+1):
         for y in range(y_start,y_end+1):
             ans += Arr[x-1][y-1]
     print(ans)