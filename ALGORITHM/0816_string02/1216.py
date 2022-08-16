import sys

sys.stdin = open('1216.text')

T = 10

# 최대 길이 회문 확인
def palindrome(N, M, arr):
    max_palidrome = 0
    for r_idx in range(N):
        for idx in range(N - M + 1):
            if arr[r_idx][idx:idx + M] == arr[r_idx][idx:idx + M][::-1]:  # 회문이라면
                if max_palidrome < len(arr[r_idx][idx:idx + M]):
                    max_palidrome = len(arr[r_idx][idx:idx + M])

    return max_palidrome


for t in range(1, T + 1):
    # N 배열 길이 M은 회문 길이 arr 입력받은 배열
    t = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    result = -10000

    # 가로 회문
    for M in range(N):
        max_len = palindrome(N, M, arr)
        if result < max_len:
            result = max_len

    # 세로를 가로로 재배렬하기 zip 함수 사용
    col_list = list(zip(*arr))

    # 세로 회문
    for M in range(N):
        max_len = palindrome(N, M, col_list)
        if result < max_len:
            result = max_len

    print(f'#{t} {result}')