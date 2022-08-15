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
            RETURN_ROOM[i][0],RETURN_ROOM[i][1] = RETURN_ROOM[i][1], RETURN_ROOM[i][0]  # 400->1 로 가는 경우의 수가 있으면, 1-> 400으로

    for i in range(len(RETURN_ROOM)):
        for j in range(i+1,len(RETURN_ROOM)):
            if int(RETURN_ROOM[i][1])>=int(RETURN_ROOM[j][0]) and int(RETURN_ROOM[j][1])>=int(RETURN_ROOM[i][0]):
                count+=1
                break
      1 3 5
      2 4 6
    # 1 2 3 4 5 6 7 8 9 10
      1   1 2   2 +1
      1   2 1   2
    print(f'#{t} {count}')