import sys

sys.stdin = open("input_baby.text")

T = int(input())

for i in range(T):
    number = input()
    baby_jin_list=[]
    for i in number:
        baby_jin_list.append(i)
    baby_jin_int_list=list(map(int,baby_jin_list))

    count_list=[]
    for i in baby_jin_int_list:
        count_same=0
        for j in baby_jin_int_list:
            if i == j:
                count_same+=1
        count_list.append(count_same)
    triplet=0
    for i in count_list:
        if i >=3:
            triplet+=1

    print(baby_jin_int_list)


    Pop = []
    Group = []
    v = baby_jin_int_list.pop(0)
    Group.append(v)
    while (len(baby_jin_int_list) > 0):
        vv = baby_jin_int_list.pop(0)
        if v + 1 == vv:
            Group.append(vv)
            v = vv
        else:
            Pop.append(Group)
            Group = []
            Group.append(vv)
            v = vv

    Pop.append(Group)
    run=[]
    for i in Pop:
        count = 0
        for j in i:
            count+=1
        if count>=3:
            run.append(count)
    print(Pop)
    run.append(triplet)
    total=0
    for i in run:
        total+=i
    print(total)
