import sys
sys.stdin = open('example_1.text')

Alpa = input()

for i in range(len[Alpa]):
    X = Alpa[i]
    cnt = 0
    New_list = []

    for j in range(len[Alpa]):
        if X == Alpa[j]:
            cnt += 1
        else:
            New_list.append(cnt)
            New_list.append(X)
            break
