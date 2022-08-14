import sys
sys.stdin=open('5356.text')

T=int(input())

for t in range(1,T+1):
    arr = [['*'] * 15 for _ in range(5)]
    for i in range(5):
        ALP=list(input().split())

        for j in range(len(ALP[0])):
            arr[i][j]=ALP[0][j]

    print(f'#{t} ',end='')
    for m in range(len(arr[0])):
        for n in range(5):
            if arr[n][m]!='*':
                print(arr[n][m],end='')
    print()