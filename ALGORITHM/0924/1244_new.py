import sys
sys.stdin = open('example_3.text')

def index_check(M_NUM):
    Max_index = 0
    for i in range(len(NUM_LIST)-1,-1,-1):
        if NUM_LIST[i] == M_NUM:
            Max_index = i
            break

    return Max_index


T = int(input())

for t in range(1,T+1):
    NUM, CHANGE = input().split()

    NUM_LIST = []
    CHECK_LIST = []
    MIN_LIST = []
    CHANGE = int(CHANGE)
    for i in NUM:
        NUM_LIST.append(int(i))
        CHECK_LIST.append(int(i))
        MIN_LIST.append(int(i))

    MAX_NUM = max(NUM_LIST)
    print(MAX_NUM)

    change = 0
    while change != CHANGE:
        if CHECK_LIST[change] != MAX_NUM:
            Location = index_check(MAX_NUM)
            CHECK_LIST[change], CHECK_LIST[Location] = CHECK_LIST[Location], CHECK_LIST[0]
            NUM_LIST.pop(Location)
            change += 1
        else:





    print(NUM_LIST)