import sys
sys.stdin = open('4836.text')

T= int(input())
for t in range(1,T+1):
    N = int(input())
    arr_2D=list([0]*10 for _ in range(10))


    for i in range(N):
        color = list(map(int,input().split()))

        Start_x=color[0]
        Start_y=color[1]
        End_x=color[2]
        End_y=color[3]
        Block_color=color[4]

        Block_list=[]
        Block_list_2D=[]
        for i in range(Start_x,End_x+1):
            for j in range(Start_y,End_y+1):
                Block_list=[]
                Block_list.append(i)
                Block_list.append(j)
                Block_list_2D.append(Block_list)

        for i in Block_list_2D:
            if arr_2D[i[0]][i[1]]==0:
                arr_2D[i[0]][i[1]]=Block_color
            else:
                arr_2D[i[0]][i[1]]=3
        print(arr_2D)
    count=0

    for w in arr_2D:
        for j in w:
            if j==3:
                count+=1
    print(f'#{t} {count}')