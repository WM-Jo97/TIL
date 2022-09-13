import sys
sys.stdin = open('eample.text')

def find_root(v):
    for i in range(1, v+1):
        if par[i] == 0:
            return i

#전위 순회
def preorder(n):
    if n:
        print(n, end=' ')
        preorder(son1[n])
        preorder(son2[n])

v = int(input())
arr = list(map(int, input().split()))
e = v - 1
son1 = [0]*(v+1)
son2 = [0]*(v+1)
par = [0]*(v+1)
for i in range(e):
    p, c = arr[i*2], arr[i*2+1]
    if son1[p] == 0:
        son1[p] = c
    else:
        son2[p] = c
    par[c] = p
root = find_root(v)
preorder(root)
print()