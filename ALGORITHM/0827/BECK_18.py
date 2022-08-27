import sys
sys.stdin=open('BECK_18.text')

X,Y = map(int,input().split())
N = int(input())
Arr=[]
for i in range(N+1):
    Dir, Dis = map(int,input().split())
    Arr.append([Dir,Dis])

NOW = Arr[-1]
Ans= 0
for i in range(len(Arr)-1):
    if Arr[i][0] == NOW[0]:
        if Arr[i][1]>NOW[1]:
            Ans+= Arr[i][1]-NOW[1]
        else: Ans+= NOW[1]-Arr[i][1]

    elif Arr[i][0] != NOW[0]:
        if NOW[0]==1:
            if Arr[i][0]==2:
                min_way=10000
                if NOW[1]+ Y + Arr[i][1]< min_way:
                    min_way = NOW[1]+ Y + Arr[i][1]
                if (X-NOW[1]) + Y + (X-Arr[i][1]) < min_way:
                    min_way = (X-NOW[1]) + Y + (X-Arr[i][1])
                Ans+=min_way

            elif Arr[i][0]==3:
                min_way = NOW[1]+Arr[i][1]
                Ans+=min_way

            elif Arr[i][0]==4:
                min_way = (X-NOW[1]) + Arr[i][1]
                Ans+=min_way

        elif NOW[0]==2:
            if  Arr[i][0] == 1:
                min_way = 10000
                if NOW[1] + Y + Arr[i][1] < min_way:
                    min_way = NOW[1] + Y + Arr[i][1]
                if (X - NOW[1]) + Y + (X - Arr[i][1]) < min_way:
                    min_way = (X - NOW[1]) + Y + (X - Arr[i][1])
                Ans += min_way

            elif Arr[i][0] == 3:
                min_way = NOW[1]+Y-Arr[i][1]
                Ans += min_way

            elif Arr[i][0] == 4:
                min_way = X-NOW[1] + Y - Arr[i][1]
                Ans += min_way

        elif NOW[0]==3:
            if Arr[i][0] == 1:
                min_way = NOW[1] + Arr[i][1]
                Ans += min_way

            elif Arr[i][0] == 2:
                min_way = Y-NOW[1] + Arr[i][1]
                Ans += min_way

            elif Arr[i][0] == 4:
                min_way = 10000
                if NOW[1] + X + Arr[i][1] < min_way:
                    min_way = NOW[1] + X + Arr[i][1]
                if (Y-NOW[1]) + X + (Y - Arr[i][1]) < min_way:
                    min_way = (Y - NOW[1]) + X + (Y - Arr[i][1])
                Ans += min_way

        elif NOW[0]==4:
            if Arr[i][0] == 1:
                min_way = NOW[1] + Y-Arr[i][1]
                Ans += min_way

            elif Arr[i][0] == 2:
                min_way = Y-NOW[1] + Y-Arr[i][1]
                Ans += min_way

            elif Arr[i][0] == 3:
                min_way = 10000
                if NOW[1] + X + Arr[i][1] < min_way:
                    min_way = NOW[1] + X + Arr[i][1]
                if (Y - NOW[1]) + X + (Y - Arr[i][1]) < min_way:
                    min_way = (Y - NOW[1]) + X + (Y - Arr[i][1])
                Ans += min_way

print(Ans)