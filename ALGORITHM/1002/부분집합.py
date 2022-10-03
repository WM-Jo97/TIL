arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(0,(1<<n)):
    for j in range(0,n):
        if i&(1<<j):
            print(arr[j],end='')
    print()