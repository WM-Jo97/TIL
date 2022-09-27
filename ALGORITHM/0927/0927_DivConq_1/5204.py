import sys
sys.stdin = open('example_1.text')

def divide(numbers):
    if len(numbers) <= 1:
        return numbers

    left = []
    right = []
    middle = len(numbers)//2

    for i in range(middle):
        left.append(numbers[i])
    for i in range(middle,len(numbers)):
        right.append(numbers[i])

    left_after = divide(left)
    right_after = divide(right)

    return merge(left_after,right_after)

def merge(left,right):
    result = []
    global ans

    if left[-1] > right[-1]:
        ans += 1

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


T= int(input())

for t in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))

    ans = 0
    numbers = divide(numbers)


    print(f'#{t} {numbers[len(numbers)//2]}',ans)