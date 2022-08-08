import sys

sys.stdin = open("input_1206.text")


for t in range(1,11):

    N = int(input())
    num_list= list(map(int,input().split()))

    count=0
    for _ in num_list:
        count+=1

    view_list=[]
    view_list_list=[]
    for i in range(2,count-2):
        if num_list[i]-num_list[i-1]>0 and num_list[i]-num_list[i-2]>0 and num_list[i]-num_list[i+1]>0 and num_list[i]-num_list[i+2]>0:
            view_list=[num_list[i]-num_list[i-2],num_list[i]-num_list[i-1],num_list[i]-num_list[i+1], num_list[i]-num_list[i+2]]
            view_list_small=1000
            for i in view_list:
                if i<view_list_small:
                    view_list_small=0
                    view_list_small+=i
            view_list_list.append(view_list_small)

    total=0
    for i in view_list_list:
        total+=i

    print(f'#{t} {total}')
"""""            
    minimum=1000
    mininumber=[]
    minimun_group=[]
    for i in view_list_list:
        for j in i:
            if j < minimum:
                minimum=0
                minimum+=j
            else:
                pass
            mininumber.append(minimum)
            minimun_group.append(mininumber)
            print(minimun_group)
    minimum_set = set(mininumber)
    minimum_list = list(minimum_set)

    total=0
    for i in minimum_list:
        total+=i
    print(total)
"""