def Counting_Sort(A,B,k):
    c = [0]*(k+1)

    for i in range(0,len(A)):
        c[A[i]] +=1

    for i in range(1,len(c)):
        c[i] += c[i-1]

    for i in range(len(B)-1, -1, -1):
        c[A[i]] -=1
        B[c[A[i]]] = A[i]
    print(B)

A=[0,4,1,3,1,2,4,1]
B=[0]*len(A)
k=len(A)

Counting_Sort(A,B,k)