import sys
sys.stdin = open('example_2.text')

Alpa = input()
print(Alpa)
N=len(Alpa)
New_list = []

for i in range(1,N):
    AL = Alpa[0:i]
    print(AL)
    Spt_num = len(Alpa)//len(AL)
    Spt_gar = len(Alpa)%len(AL)
    print(Spt_num)
    print(Spt_gar)
    for j in range(N):
        target = 0
'''
for n in range(1,N):
    for i in range(N):
        cnt = 0
        for j in range(i,N):
            if Alpa[i] == Alpa[j]:
                cnt += 1
            else:
                break
        if cnt != 1:
            New_list.append(cnt)
        else:
            New_list.append(Alpa[i])

        print(New_list)
'''