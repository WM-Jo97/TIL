import sys
sys.stdin=open('BECK_12.text')

W,H = map(int, input().split())
P,Q = map(int, input().split())
t= int(input())

Arr=[[0]*(W+1) for _ in range(H+1)]
print(Arr)

Arr[Q][P]=1
print(Arr)