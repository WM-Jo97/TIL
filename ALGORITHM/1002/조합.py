def comb(n,r):
    if r == 0:
        print(ans)
        return

    elif n < r:
        return

    else:
        ans.append(arr[n-1])
        comb(n-1,r-1)
        ans.pop(-1)
        comb(n-1,r)

ans = []
arr = [1,2,3,4]

comb(4,3)