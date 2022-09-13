import sys
sys.stdin = open('example.text')

def find_root(v):
    for i in range(1, v+1):
        if par[i] == 0:
            return i

def midorder(n,alpa):
    if n:
        midorder(son1[n],alpa)
        print(alpa[n], end='')
        midorder(son2[n],alpa)

for t in range(1,11):
    v = int(input())
    e = v-1

    alpa = [0]*(v+1)

    son1 = [0]*(v+1)
    son2 = [0]*(v+1)
    par = [0]*(v+1)

    for i in range(v):
        a = list(input().split())
        p =0
        for j in range(len(a)):
            if j == 0:
                p = int(a[j])
            elif j == 1:
                alpa[p] = a[j]
            else:
                if son1[p] == 0:
                    son1[p] = int(a[j])
                else:
                    son2[p] = int(a[j])

                par[int(a[j])] = p

    root = find_root(v)
    print(f'#{t} ',end='')
    midorder(root,alpa)
    print()