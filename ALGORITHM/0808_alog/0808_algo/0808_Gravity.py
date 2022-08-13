import sys

sys.stdin = open("input.text")

T = int(input())

for i in range(T):
    N = int(input())

    col_list = list(map(int, input().split()))

    count_0=0
    col_list_1=[]
    for i in col_list:
        if i != 0:
            col_list_1.append(i)
        else:
            count_0+=1

    count_col=0
    for i in col_list_1:
        count_col+=1

    count_list=[]
    for i in range(count_col):
        count = 0
        for j in range(i+1,count_col):
            if col_list_1[i] > col_list_1[j]:
                count+= 1
            else:
                pass
        count_list.append(count)

    def max(x) :
        max=0
        for i in x:
            if i > max:
                max=i
            else:
                pass
        return max

    print(count_0+max(count_list))
