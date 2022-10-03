def Perm(n,k):
    global arr
    if n == k:
        print(p)
        return

    else:
        for i in range(len(arr)):
            if not used[i]:
                p[n] = arr[i]
                used[i] = True
                Perm(n+1,k)
                used[i] = False

k = 3
p = [0]*k
arr = [1,5,6,7]
used = [0]*len(arr)

Perm(0,k)

