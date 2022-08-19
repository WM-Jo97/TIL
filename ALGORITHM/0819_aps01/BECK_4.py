import sys
sys.stdin=open('BECK_4.text')

def Check(x,A,B):
    if x-1 <0:
        return 'D'
    if x in A:
        if x in B:
            if A.count(x)>B.count(x):
                return 'A'
            elif A.count(x)<B.count(x):
                return 'B'
            else:
                return Check(x-1,A,B)
        else:
            return 'A'
    else:
        if x in B:
            return 'B'
        else:
            return Check(x-1,A,B)

N = int(input())

for _ in range(N):
    A=list(map(int,input().split()))
    if A[0]!=0:
        A_card= A.pop(0)

    B=list(map(int,input().split()))
    if B[0]!=0:
        B_card=B.pop(0)

    print(Check(4,A,B))