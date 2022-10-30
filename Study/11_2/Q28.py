import sys
sys.stdin = open('example_2.text')

N = int(input())
NUM_LIST = list(map(int,input().split()))

print(NUM_LIST)
front = 0
end = N-1

visited = [0]*(N+1)
answer = 0

while True:
    middle = (front + end) // 2
    if visited[middle] == 0:
        visited[middle] = 1
        if NUM_LIST[middle] == middle:
            answer = middle
            break
        elif NUM_LIST[middle] < middle:
            front = middle

        elif NUM_LIST[middle] > middle:
            end = middle

    else:
        answer = -1
        break

print(answer)
