import sys
sys.stdin = open('11444.text')

def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num = 2
        a = 0
        b = 1
        while num != n+1:
            value = a+b
            a = b
            b = value
            num+= 1
        return b

N = int(input())

print(Fibo(N)%1000000007)
