def Find_set(x):
    while x !=p[x]:
        x = p[x]

    return x

def Union(x,y):
    p[Find_set(y)] = Find_set(x)

N = 5
p = [0]*(N+1)

for i in range(1,N+1):
    p[i] = i

print(p)

Find_set(x)