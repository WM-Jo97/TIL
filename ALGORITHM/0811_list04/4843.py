import sys
sys.stdin=open('4843.text')

T=int(input())
for t in range(1,1+T):
    N=int(input())
    numbers=list(map(int,input().split()))


    for i in range(N-1,0,-1):                                       # 4213  ---> 1234  pop 1,4
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

    Ans=[]
    for _ in range(5):
        Ans.append(numbers.pop(len(numbers)-1))
        Ans.append(numbers.pop(0))

    print(f'#{t}',end=' ')
    for i in Ans:
        print(i,end=' ')
    print()
