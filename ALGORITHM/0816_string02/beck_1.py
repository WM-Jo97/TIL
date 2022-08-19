import sys
sys.stdin=open('beck_1.text')

T = int(input())
Num=list(map(int,input().split()))
#Num=[0 1 1 3 2]

Order = list(range(1,T+1))
#Order=[1 2 3 4 5]

for i in range(T):
    if Num[i]!=0: #Num=0일때는 움직이지 않으므로 바꿔줄 필요 없음
        for j in range(Num[i]):
            Order[i],Order[i-Num[i]+j] = Order[i-Num[i]+j],Order[i]
        # Num은 결국 바꾸는 횟수를 나타냄.
        # Num[3]= 일때 N[3],N[0] N[3],N[1] N[3],N[2] 를 순서대로 위치를 바꿔주면
        # 숫자를 편입시키고 기존 숫자들을 미는것과 같은 효과를 얻을 수 있음

for i in Order:
    print (i,end=' ')


