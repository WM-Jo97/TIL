import sys
sys.stdin = open('3143.text')

tc = int(input())

for t in range(1, tc+1):
    A, B = input().split()
    text = len(A)
    pattern = len(B)
    cnt = 0
    result = 0
    idx=0

    while idx < text:
        for jdx in range(pattern):
            if B[jdx] != A[jdx + idx]:
                idx+=1
                break
        else:
            cnt += 1
            idx += pattern


    result = text - ((pattern - 1) * cnt)

    print(f'#{t} {result}')

