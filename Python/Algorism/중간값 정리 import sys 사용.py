import sys

data = []
n=2
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for j in range(len(data)):
    data[j] = sorted(data[j])

answer = []
for element in data:
    answer += element
    
y=int(data[0][0])

answer.remove(y)
lastans=[]
for v in answer:
    if v not in lastans:
        lastans.append(v)

key=len(lastans)
le=int(key/2+1)
la=lastans[le]
print(la)

