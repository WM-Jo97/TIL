import sys
sys.stdin = open('example_7.text')

def index_check(M_NUM):
    Max_index = 0
    for i in range(len(NUM_LIST)-1,-1,-1):
        if NUM_LIST[i] == M_NUM:
            Max_index = i
            break

    return Max_index

def MAX_CHECK(M_NUM):
    CHECK = 0
    for i in range(len(NUM_LIST)-1,-1,-1):
        if NUM_LIST[i] == M_NUM:
            CHECK+= 1
    return CHECK

def min_index(M_MIN):
    Min_index = 0
    for i in range(len(NUM_LIST)-1,-1,-1):
        if NUM_LIST[i] == M_MIN:
            Min_index=i
            break
    return Min_index


T = int(input())
for t in range(1,T+1):
    NUM , CHANGE = input().split()

    NUM_LIST = []
    MAX_LIST = []
    MIN_LIST = []
    CHANGE = int(CHANGE)
    for i in NUM:
        NUM_LIST.append(int(i))
        MAX_LIST.append(int(i))
        MIN_LIST.append(int(i))

    CH = 0

    M_MIN = min(MIN_LIST)
    M_NUM = max(MAX_LIST)

    #print(f'#최고 값 인덱스 : {index_check(M_NUM)}')
    #print(f'#최소 값 인덱스 : {min_index(M_MIN)}')
    CHECK_MAX_LIST = []
    for i in range(CHANGE):
        if len(MAX_LIST) != 1:
            M_NUM = max(MAX_LIST)
            CHECK_MAX_LIST.append(MAX_CHECK(M_NUM))
            location = index_check(M_NUM)
            min_location = min_index(M_MIN)
            for j in range(len(NUM_LIST)):
                if NUM_LIST[j] < M_NUM:
                    if j == location:
                        NUM_LIST[-2], NUM_LIST[-1] = NUM_LIST[-1], NUM_LIST[-2]
                    elif j > location:
                        EXTRA = []
                        for x in range(j,len(NUM_LIST)):
                            EXTRA.append(NUM_LIST[x])
                        A = max(EXTRA)
                        A_LO = index_check(A)
                        print(A_LO)
                        for y in range(j,len(NUM_LIST)):
                            if NUM_LIST[y] < A:
                                NUM_LIST[y], NUM_LIST[A_LO] = NUM_LIST[A_LO],NUM_LIST[y]

                    else:
                        NUM_LIST[j], NUM_LIST[location] = NUM_LIST[location],NUM_LIST[j]
                        MAX_LIST.remove(M_NUM)
                        break
        else:
            NUM_LIST[-1],NUM_LIST[-2] = NUM_LIST[-2], NUM_LIST[-1]

    C = MAX_CHECK(M_NUM)
    print(CHECK_MAX_LIST)

    for i in CHECK_MAX_LIST:
        if i >= CHANGE:
            CHECK_NUM_LIST = []
            for i in NUM_LIST:
                CHECK_NUM_LIST.append(i)

            for i in range(C-CHANGE):
                NUM_LIST[-1], NUM_LIST[-2] = NUM_LIST[-2], NUM_LIST[-1]

            PRICE = ''
            for i in NUM_LIST:
                PRICE += str(i)
            PRICE_CHECK = ''
            for j in CHECK_NUM_LIST:
                PRICE_CHECK+= str(j)

            if int(PRICE) >= int(PRICE_CHECK):
                print(f'#{t} {PRICE}')
            else:
                print(f'#{t} {PRICE_CHECK}')
            break

    else:
        PRICE = ''
        for i in NUM_LIST:
            PRICE+= str(i)
        print(f'#{t} {PRICE}')
