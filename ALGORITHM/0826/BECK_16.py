import sys
sys.stdin=open('BECK_16.text')

Switch_num = int(input())
Switch=list(map(int,input().split()))
Member= int(input())

for i in range(Member):
    Gender, Num = map(int,input().split())

    if Gender == 1:
        j=1
        while True:
            if Num*j <= Switch_num:
                if Switch[(Num*j)-1]==0:
                    Switch[(Num*j)-1]=1
                    j+=1
                else:
                    Switch[(Num*j)-1]= 0
                    j+=1
            else:
                break

    elif Gender == 2:
        i = 1
        if Switch[Num-1]==0:
            Switch[Num-1]= 1
        else:
            Switch[Num-1]= 0

        while True:
            if Num-1-i>=0 and Num-1+i<Switch_num:
                if Switch[Num-1-i] == Switch[Num-1+i]:
                    if Switch[(Num-1)-i]==0:
                        Switch[(Num-1)-i]= 1
                        Switch[(Num-1)+i]= 1
                        i+=1
                    else:
                        Switch[Num-1-i] = 0
                        Switch[Num-1+i] = 0
                        i+=1
                else:
                    break
            else:
                break

while True:
    for i in range(20):
        if Switch:
            print(f'{Switch.pop(0)}',end=' ')
        else:
            break
    print()
    if not Switch:
        break
