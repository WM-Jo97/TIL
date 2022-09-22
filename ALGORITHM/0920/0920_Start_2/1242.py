import sys
sys.stdin =open('example_3.text')

def bit(arr):
    arr_list = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '0':
                continue
            arr_list.append(arr[r])

    bit_num_list = []
    for i in range(len(arr_list)):
        bit_num = '000000'
        for j in range(len(arr_list[i])):
            if arr_list[i][j] == 0:
                continue
            bit_num = bit_num+BIT[arr_list[i][j]]
        bit_num_list.append(bit_num)

    return bit_num_list

def scanner(BIT_LIST):
    pwd_list = []
    for i in range(len(BIT_LIST)):
        COUNT = [0,0,0,0]
        for j in range(len(BIT_LIST[i])-1,-1,-1):
            if BIT_LIST[i][j] != '0':
                idx = j
                NUM = 1
                COUNT_NUM = 3
                while True:
                    if BIT_LIST[i][idx] == BIT_LIST[i][idx-1]:
                        NUM+=1
                        idx-=1
                    else:
                        COUNT[COUNT_NUM] = NUM
                        NUM = 1
                        idx-=1
                        COUNT_NUM -= 1
                    if COUNT_NUM == -1:
                        break
                break
        D_num = min(COUNT)
        for i in range(len(COUNT)):
            COUNT[i] = COUNT[i]//D_num

        print(COUNT)
        if COUNT in PASSWORD:
            for x in range(len(BIT_LIST[i])-1,-1,-1):
                if BIT_LIST[i][x] != 0:




    return pwd_list


T = int(input())

BIT = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

PASSWORD = {
    '[3,2,1,1]': 0,
    '[2,2,2,1]': 1,
    '[2,1,2,2]': 2,
    '[1,4,1,1]': 3,
    '[1,1,3,2]': 4,
    '[1,2,3,1]': 5,
    '[1,1,1,4]': 6,
    '[1,3,1,2]': 7,
    '[1,2,1,3]': 8,
    '[3,1,1,2]': 9,
}

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(input())

    bit_num_list = bit(arr)
    Set_bit = set(bit_num_list)
    BIT_LIST = list(Set_bit)
    print(BIT_LIST)

    scanner(BIT_LIST)
    #pwd_list = scanner(bit_num_list)
    print()