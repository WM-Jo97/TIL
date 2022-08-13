arr = [3,6,7,1,5,4]

n = len(arr)
jip=[]
group=[]
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            group.append(i)
    jip.append(group)
print(jip)