def Selection_sort(A):
    n = len(A)

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]

def Selection_sort_recur(A):


A = [34, 2, 4, 11, 6, 1]

Selection_sort(A)

print(A)
