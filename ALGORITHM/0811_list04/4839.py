import sys
sys.stdin=open('4839.text')
T=int(input())
for t in range(1,T+1):
    P,A,B = (map(int,input().split()))

    count_A=0
    count_B=0

    l_A=1
    r_A=P
    c_A=int((l_A+r_A)/2)

    while True:
        c_A=int((l_A+r_A)/2)
        count_A+=1
        if c_A==A:
            break
        else:
            if A>c_A:
                l_A=c_A
            else:
                r_A=c_A

    l_B=1
    r_B=P
    c_B=int((l_B+r_B)/2)

    while True:
        c_B=int((l_B+r_B)/2)
        count_B+=1
        if c_B==B:
            break
        else:
            if B>c_B:
                l_B=c_B
            else:
                r_B=c_B

    if count_A<count_B:
        print(f'#{t} A')
    elif count_A==count_B:
        print(f'#{t} 0')
    else:
        print(f'#{t} B')