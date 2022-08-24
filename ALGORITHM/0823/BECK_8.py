N = int(input())
Arr=[]
Many=[]
for N_2 in range(N,-1,-1):
    NUM = [N]
    NUM.append(N_2)
    while True:
        N_X = NUM[-2]-NUM[-1]
        if N_X <0:
            break
        else:
            NUM.append(N_X)
    Many.append([N_2, len(NUM)])

Max_num=0
Max_N_X=0
for i in Many:
    if i[1]>Max_num:
        Max_num=i[1]
        Max_N_X=i[0]
print(Max_num)

NUM_A = [N]
NUM_A.append(Max_N_X)
while True:
    N_X = NUM_A[-2]-NUM_A[-1]
    if N_X <0:
        break
    else:
        NUM_A.append(N_X)

print(*NUM_A)