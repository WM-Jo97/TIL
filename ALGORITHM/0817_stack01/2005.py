import sys
sys.stdin=open('2005.text')

T=int(input())

for t in range(1,T+1):
    N=int(input())
    B=[]
    for i in range(N):
        A=[0]*(1+2*i)
        A[0] = A[-1] = 1
        B.append(A)
    print(B)

    for i in range(2,N):
        for j in range((i-1)):
            B[i][2+j*2] = B[i-1][0+j*2]+B[i-1][2+j*2]

    print(f'#{t}')
    for i in B:
        for j in i:
            if j!=0:
                print(j ,end=' ')
        print()

'''
#0    0
#1    0
#2    0:2         2
#3    0:2 2:4     2  4
#4    0:2 2:4 4:6 2  4  6
#5    0:2 2:4 4:6 6:8
'''


'''
0001000
0010100
0102010
1030301




'''