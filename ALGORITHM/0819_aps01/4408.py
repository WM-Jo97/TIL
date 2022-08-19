import sys
sys.stdin=open('4408.text')

T=int(input())

for t in range(1,T+1):
    N=int(input())
    RETURN_ROOM=[]
    for i in range(N):
        NOW, RETURN = map(int,input().split())
        if NOW%2!=0:
            NOW=NOW+1
        if RETURN%2!=0:
            RETURN=RETURN+1
        NOW=NOW//2
        RETURN=RETURN//2
        RETURN_ROOM.append([NOW,RETURN])

    for i in range(len(RETURN_ROOM)):
        if RETURN_ROOM[i][0]>RETURN_ROOM[i][1]:
            RETURN_ROOM[i][0],RETURN_ROOM[i][1] = RETURN_ROOM[i][1], RETURN_ROOM[i][0]

    for i in range(len(RETURN_ROOM)-1):
        for j in range(i,0,-1):
            if RETURN_ROOM[i][0]>RETURN_ROOM[i+1][0]:
                RETURN_ROOM[i],RETURN_ROOM[i+1]=RETURN_ROOM[i+1],RETURN_ROOM[i]


    Arr = [0 for _ in range(201)]
    for i in RETURN_ROOM:
        for j in range(i[0],i[1]+1):
            Arr[j]+=1

    Max_num=0
    for i in Arr:
        if i > Max_num:
            Max_num = i

    print(f'#{t} {Max_num}')