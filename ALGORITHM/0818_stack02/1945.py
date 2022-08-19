import sys
sys.stdin=open('1945.text')

T=int(input())


for i in range(1,T+1):
    List = [[] for _ in range(5)]

    Num=int(input())
    while int(Num) !=1:
        if Num/2 - Num//2==0:
            Num = int(Num/2)
            List[0].append(2)

        elif Num/3 - Num//3 == 0:
            Num= int(Num/3)
            List[1].append(3)

        elif Num/5 - Num//5 == 0:
            Num = Num / 5
            List[2].append(5)

        elif Num/7 - Num//7 == 0:
            Num = Num / 7
            List[3].append(7)

        elif Num/11 -Num//11 ==0:
            Num= Num/11
            List[4].append(11)


    print(f'#{t}',end=' ')
    for i in List:
        print(len(i),end=' ')
    print()