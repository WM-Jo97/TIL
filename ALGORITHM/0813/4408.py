import sys
sys.stdin=open('4408.text')

T=int(input())

for t in range(1,T+1):
    N=int(input())
    RETURN_ROOM=[]
    for i in range(N):
        NOW, RETURN = input().split()
        RETURN_ROOM.append([NOW,RETURN])

    count_set=[1]
    for i in range(len(RETURN_ROOM)):
        if RETURN_ROOM[i][0]>RETURN_ROOM[i][1]:
            RETURN_ROOM[i][0],RETURN_ROOM[i][1] = RETURN_ROOM[i][1], RETURN_ROOM[i][0]

        for j in range(i+1,len(RETURN_ROOM)):
            if int(RETURN_ROOM[i][1])>int(RETURN_ROOM[j][0]) and RETURN_ROOM[i]!=RETURN_ROOM[j]:
                count_set.append(RETURN_ROOM[i][0])

    set_A=set(count_set)
    list_A=list(set_A)
    print(f'#{t} {len(list_A)}')