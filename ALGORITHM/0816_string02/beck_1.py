import sys
sys.stdin=open('beck_1.text')

T = int(input())

Num=list(map(int,input().split()))
Order = [1,2,3,4,5]

for i in range(T):
    Order[i],Order[i-Num[i]]=Order[i-Num[i]],Order[i]

    print(Order)

print(Num)