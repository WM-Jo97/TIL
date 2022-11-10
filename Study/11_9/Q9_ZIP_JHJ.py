import sys
sys.stdin = open('example_2.text')

Alpa = input()
N=len(Alpa)
Max_N = N//2

Len_num_list = []

if len(Alpa) == 1:
        answer = 1

for i in range(1,Max_N+1):
    New_list = []
    Arr_list = []
    No_dub = []
    for j in range(0,N,i):
        AL = Alpa[j:j+i]
        Arr_list.append(AL)
    print(Arr_list)

    for x in range(len(Arr_list)):
        X = Arr_list[x]
        Cnt = 0
        for y in range(x,len(Arr_list)):
            if X == Arr_list[y]:
                Cnt+=1
            else:
                if Cnt == 1:
                    New_list.append(X)
                else:
                    if New_list:
                        if type(New_list[-1]) == int:
                            pass
                        else:
                            New_list.append(Cnt)
                    else:
                        New_list.append(Cnt)
                break
        else:
            if Cnt == 1:
                New_list.append(X)
                break
            else:
                New_list.append(Cnt)
                New_list.append(X)
                break

    print(New_list)
    voca = ''
    for i in New_list:
        i = str(i)
        if i != '1':
            voca += i
    print(voca)
    Len_num_list.append(len(voca))
    answer = min(Len_num_list)
print(answer)
