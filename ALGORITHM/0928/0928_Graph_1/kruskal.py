def find_set(x):
    if


V,E = map(int,input().split())
edge = []
for _ in range(E):
    u , v, w = map(int,input().split())
    edge.append([u,v,w])

edge.sort(key=lambda x:x[2])
rep = [i for i in range(V+1)]

