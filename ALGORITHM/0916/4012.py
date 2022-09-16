import sys
sys.stdin=open('example_6.text')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        TEMP = list(map(int,input().split()))
        arr.append(TEMP)
    print(arr)