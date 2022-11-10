import sys
sys.stdin = open('example_1.text')

Word = list(input())
n_list = []
for i in range(len(Word)):
    try:
        n_list.append(int(Word[i]))
    except:
        n_list.append(Word[i])

n_list.sort(key=str)
arr = []
num=''
alpa=''
for j in range(len(n_list)):
    if type(n_list[j]) == int:
        num += str(n_list[j])
    else:
        alpa += n_list[j]

print(alpa+num)