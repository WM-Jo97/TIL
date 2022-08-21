A=[1,2,6,7,88,3,77]

for i in range(len(A)):
    for j in range(len(A)-1):
        if A[j]>A[j+1]:
            A[j],A[j+1] = A[j+1], A[j]

print(A)