import sys
sys.stdin=open('4408.text')

T=int(input())

for t in range(1,T+1):
    N=int(input())
    RETURN_ROOM=[]
    for i in range(N):
        NOW, RETURN = input().split()
        RETURN_ROOM.append([NOW,RETURN])

    count=1
    for i in range(len(RETURN_ROOM)):
        if RETURN_ROOM[i][0]>RETURN_ROOM[i][1]:
            RETURN_ROOM[i][0],RETURN_ROOM[i][1] = RETURN_ROOM[i][1], RETURN_ROOM[i][0]

    for i in range(len(RETURN_ROOM)):
        for j in range(i+1,len(RETURN_ROOM)):
            if int(RETURN_ROOM[i][1])>=int(RETURN_ROOM[j][0]) and int(RETURN_ROOM[j][1])>=int(RETURN_ROOM[i][0]):
                count+=1
                break


    print(f'#{t} {count}')