import sys
sys.stdin = open('example_1242.text')

def scanner(arr):
    total = 0
    for row in range(N):
        col = M*4 - 1
        while col >= 55:
            if arr[row][col] == '1' and arr[row-1][col]=='0':
                pwd = []
                for _ in range(8):
                    n2 = n3 = n4 = 0

                    while arr[row][col] =='0':
                        col -= 1

                    while arr[row][col] == '1':
                        n4 += 1
                        col -= 1

                    while arr[row][col] == '0':
                        n3 += 1
                        col -= 1

                    while arr[row][col] == '1':
                        n2 += 1
                        col -= 1

                    min_n = min(n2,n3,n4)

                    if min_n != 0:
                        (n2 // min_n, n3// min_n , n4//min_n)

                if len(pwd) == 8:
                    even_sum = sum(pwd[::2])
                    odd_sum = sum(pwd[1::2])
                    if (odd_sum*3 + even_sum)%10 == 0:
                        total += even_sum+odd_sum
                    return total
            else:
                col-=1

patterns = {
    (2,1,1) : 0,
    (2,2,1) : 1,
    (1,2,2) : 2,
    (4,1,1) : 3,
    (1,3,2) : 4,
    (2,3,1) : 5,
    (1,1,4) : 6,
    (3,1,2) : 7,
    (2,1,3) : 8,
    (1,1,2) : 9,
}




T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [''] * N
    for i in range(N):
        temp = input()

        bit = ''
        for j in range(M):
            val = f'{int(temp[j], base=16):044b}'
            bit += val

        arr[i] = bit

    res = scanner(arr)
    print(f'#{t} {res}')