import sys
sys.stdin=open('example_4.text')

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    # 부모가 있고 부모 < 자식 인 경우 자리 교환 (부모가 없거나 부모 > 자식 조건을 만족할 때 까지)
    c = last
    p = c // 2  #완전 이진트르에서 부모 정점 번호
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for t in range(1,T+1):
    N =int(input())
    NUM = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    for i in NUM:
        enq(i)

    TOTAL = 0
    while N//2 > 0:
        TOTAL += heap[N//2]
        N = N//2

    print(f'#{t} {TOTAL}')