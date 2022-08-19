import sys
sys.stdin=open('beck_3.text')

arr = [[0] * 100 for _ in range(100)]
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] += 10
    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] > 0:
                cnt += 1
print(cnt)