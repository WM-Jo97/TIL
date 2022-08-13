import sys
sys.stdin = open('1208.text')

N=10
for t in range(N):
    Count = int(input())

    blocks=list(map(int, input().split()))

    print(Count)
    print(blocks)

    def count_sort(A,K):
        C=[0]*K
        B=[0]*K
        for i in range(0,Count):
            C[A[i]]+=1
        for i in range(1,len(C)):
            C[i]+=C[i-1]

        for i in range(K-1,-1,-1):
            C[A[i]] -= 1
            B[C[A[i]]] = A[i]
        return B

    print(count_sort(blocks,Count))