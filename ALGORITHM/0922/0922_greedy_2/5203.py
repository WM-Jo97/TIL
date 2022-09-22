import sys
sys.stdin = open('example_4.text')

T = int(input())

for t in range(1,T+1):
    NUM_LIST = list(map(int,input().split()))

    Player_1 = []
    Player_2 = []
    win = False
    res = 0
    for i in range(len(NUM_LIST)):
        if i%2 == 0:
            Player_1.append(NUM_LIST[i])
            Player_1.sort()
            if not win:
                if len(Player_1) >= 3:
                    for j in range(len(Player_1)):
                        if Player_1.count(Player_1[j]) == 3:
                            res = 1
                            # print(f'#{t} 1')
                            win = True


                    for j in range(len(Player_1)):
                        if Player_1[j]+1 in Player_1 and Player_1[j]+2 in Player_1:
                            res = 1
                            # print(f'#{t} 1')
                            win = True

        else:
            Player_2.append(NUM_LIST[i])
            Player_2.sort()
            if not win:
                if len(Player_2) >= 3:
                    for j in range(len(Player_2)):
                        if Player_2.count(Player_2[j]) == 3:
                            res = 2
                            # print(f'#{t} 2')
                            win = True


                    for j in range(len(Player_2)):
                        if Player_2[j]+1 in Player_2 and Player_2[j]+2 in Player_2:
                            res = 2
                            # print(f'#{t} 2')
                            win = True

    else:
        if not win:
            print(f'#{t} 0')
        else:
            print(f'#{t} {res}')