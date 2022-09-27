import sys
sys.stdin = open('example_2.text')
'''
def b_serach(n, arr, key):
    low = 0
    high = n - 1
    flag = 0

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            if flag == 1:
                return 0
            else:
                high = mid - 1
                flag = 1
        else:
            if flag == 2:
                return 0
            else:
                low = mid + 1
                flag = 2
    return 0

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    left = sorted(list(map(int, input().split())))
    right = list(map(int, input().split()))
    count = 0

    for i in right:
        count += b_serach(N, left, i)

    print (f'#{t} {count}')
'''

def Find(N,LIST,key):
    low = 0
    high = N- 1
    flag = 0

    while low <= high:
        mid = low + (high - low) // 2
        if LIST[mid] == key:
            return 1
        elif LIST[mid] > key:
            if flag == 1:
                return 0
            else:
                high = mid - 1
                flag = 1
        else:
            if flag == 2:
                return 0
            else:
                low = mid + 1
                flag = 2
    return 0


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    LIST_A = list(map(int,input().split()))
    LIST_A.sort()
    LIST_B = list(map(int,input().split()))

    count = 0
    for i in LIST_B:
        count += Find(N,LIST_A,i)

    print(f'#{t} {count}')
