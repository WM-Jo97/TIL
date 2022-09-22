import sys
sys.stdin=open('example_5.text')

def midorder(n,arr):
    if n:
        midorder(son1[n],arr)
        midorder(son2[n],arr)
        arr.append(n)

T = 10
for t in range(1,T+1):
    N = int(input())
    son1 =[0]*(N+1)
    son2 =[0]*(N+1)
    NUM = [0]*(N+1)

    for i in range(N):
        a = list(input().split())
        P = 0
        for j in range(len(a)):
            if j == 0:
                P = int(a[j])
            elif j == 1:
                if a[j] == '+' or '-' or '*' or '/':
                    NUM[P] = a[j]
                else:
                    NUM[P] = int(a[j])
            elif son1[P]==0:
                son1[P] = int(a[j])
            elif son2[P]==0:
                son2[P] = int(a[j])
    arr = []
    midorder(1,arr)
    TOTAL = []
    for i in range(len(arr)):
        if NUM[arr[i]] == '+':
            A=TOTAL.pop(-1)
            B=TOTAL.pop(-1)
            TOTAL.append(B+A)
        elif NUM[arr[i]] == '-':
            A = TOTAL.pop(-1)
            B = TOTAL.pop(-1)
            TOTAL.append(B-A)
        elif NUM[arr[i]] == '*':
            A = TOTAL.pop(-1)
            B = TOTAL.pop(-1)
            TOTAL.append(A*B)
        elif NUM[arr[i]] == '/':
            A = TOTAL.pop(-1)
            B = TOTAL.pop(-1)
            TOTAL.append(B/A)
        else:
            TOTAL.append(int(NUM[arr[i]]))
    print(f'#{t} {int(TOTAL[0])}')