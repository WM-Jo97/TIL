import sys
sys.stdin = open('example_3.text')

def index_check(M_NUM):
    Max_index = 0
    for i in range(len(CHECK_LIST)-1,-1,-1):
        if CHECK_LIST[i] == M_NUM:
            Max_index = i
            break

    return Max_index


T = int(input())

for t in range(1,T+1):
    NUM, CHANGE = input().split()

    NUM_LIST = []
    CHECK_LIST = []
    CHANGE = int(CHANGE)
    for i in NUM:
        NUM_LIST.append(int(i))
        CHECK_LIST.append(int(i))

    change_list = [CHECK_LIST]
    M_NUM = max(CHECK_LIST)

    change = 0
    check = False
    while change != CHANGE:
        for x in range(len(change_list)):
            ANS_CHECK_LIST = []
            for y in range(len(change_list[x])):
                ANS_CHECK_LIST.append(change_list[x][y])

            for i in range(len(change_list[x])-1):
                for j in range(i+1,len(change_list[x])):
                    ANS_CHECK_LIST[i], ANS_CHECK_LIST[j] = ANS_CHECK_LIST[j], ANS_CHECK_LIST[i]
                    ANSWER = []
                    for w in ANS_CHECK_LIST:
                        ANSWER.append(w)


                    if ANSWER not in change_list and ANSWER[0] == M_NUM:
                        change_list.append(ANSWER)

                    if ANSWER == change_list[0]:
                        check = True

                    for y in range(len(change_list[x])):
                        ANS_CHECK_LIST[y] = change_list[x][y]
        change+=1

    if not check:
        change_list.remove(change_list[0])

    VS_LIST = []
    for q in range(len(change_list)):
        VS_num = ''
        for a in range(len(change_list[q])):
            VS_num += str(change_list[q][a])
        VS_LIST.append(int(VS_num))

    Set_VS_list = set(VS_LIST)
    VS_LIST = list(Set_VS_list)

    print(f'#{t} {max(VS_LIST)}')

