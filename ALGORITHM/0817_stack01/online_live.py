'''
# 팩토리얼 함수
def f(n):
    if n <= 1:
        return 1
    else:
        return n*f(n-1)

for i in range(21):
    print(i,f(i))
'''

'''
# 피보나치 함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo((n-1))

for i in range(101):
    print(i, fibo(i))
'''
'''
#memo 이용
def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1]*150
memo[0] = 0
memo[1] = 1
for i in range(150):
    print(i, fibo(i))
'''
'''
#피보나치 수 DP 적용 알고리즘
def fibo_dp(n):
    table[0]=0
    table[1]=1
    for i in range(2,n+1):
        table[i] = table[i-1] + table[i-2]
    return

table = [0]*101
fibo_dp(100)
print(table[100])
'''

a=0
b=1
n=20
for _ in range(n-1):
    a, b = b, a+b
print(b)