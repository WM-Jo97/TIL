import sys
sys.stdin = open('example_7.text')

def index_check(M_NUM):
    Max_index = 0
    for i in range(len(NUM_LIST)-1,-1,-1):
        if NUM_LIST[i] == M_NUM:
            Max_index = i
            break
    return Max_index

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

    ch = 0
    for i in range(CHANGE):
        #print(MAX_LIST)
        if len(MAX_LIST) != 1:
            M_NUM = max(MAX_LIST)
            location = index_check(M_NUM)
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
                        for y in range(j,len(NUM_LIST)):
                            if NUM_LIST[y] < A:
                                NUM_LIST[y], NUM_LIST[A_LO] = NUM_LIST[A_LO],NUM_LIST[y]

                    else:
                        NUM_LIST[j], NUM_LIST[location] = NUM_LIST[location],NUM_LIST[j]
                        MAX_LIST.remove(M_NUM)
                        break
        else:
            NUM_LIST[-1],NUM_LIST[-2] = NUM_LIST[-2], NUM_LIST[-1]

    PRICE = ''
    for i in NUM_LIST:
        PRICE+= str(i)

    print(f'#{t} {PRICE}')