import sys
sys.stdin = open('example_1.text')

Day, A = map(int,input().split())
Arr = [0]*(Day+1)
Arr[1] = 1
Arr[2] = 1

while True:
    for i in range(3,Day+1):
        Arr[i] = Arr[i-2] + Arr[i-1]

    if Arr[Day] < A:
        Arr[2] += 1
    elif Arr[Day] > A:
        Arr[1] += 1
        Arr[2] = Arr[1]
    elif Arr[Day]  == A:
        break

print(Arr[1])
print(Arr[2])
