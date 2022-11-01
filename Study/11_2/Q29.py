import sys
input = sys.stdin.readline

N,C = map(int,input().split())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

start = 1
end = num_list[-1] - num_list[0]
result = 0

while (start <= end):
    mid = (start+end)//2
    value = num_list[0]
    count = 1
    for i in range(1,N):
        if num_list[i] >= value + mid:
            value = num_list[i]
            count += 1

    if count >= C:
        start = mid +1
        result = mid

    else:
        end = mid -1

print(result)