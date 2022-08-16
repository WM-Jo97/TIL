import sys
sys.stdin=open('4865.text')

T=int(input())

for t in range(1,T+1):
    Str1=input()
    Str2=input()

    count_list=[]
    for i in Str1:
        count=0
        for j in Str2:
            if i == j:
                count+=1
        count_list.append(count)

    max_count=count_list[0]
    for i in count_list:
        if i > max_count:
            max_count=i

    print(f'#{t} {max_count}')