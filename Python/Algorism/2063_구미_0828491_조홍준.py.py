data= []
n=2

for i in range(n):
    data.append(list(input().split()))

key=int(data[0][0])

answer=[]

for element in data:
    answer +=element

del answer[0]   
answer.sort(key=int)

lastans=[]
for v in answer:
    if v not in lastans:
        lastans.append(v)

ky=len(lastans)
le=int(ky/2+1)
la=lastans[le]

print(la)
