import sys
sys.stdin=open('BECK_17.text')

N = int(input())
Arr = []
for i in range(N):
    location, col = map(int, input().split())
    Arr.append([location, col])

for i in range(len(Arr)):
    for j in range(len(Arr)-1):
        if Arr[j][0] > Arr[j+1][0]:
            Arr[j],Arr[j+1] = Arr[j+1], Arr[j]

max_roof = [0,0]
max_len = [0,0]
for i in Arr:
    if i[1]>= max_roof[1]:
        max_roof=i
    if i[0]>= max_len[0]:
        max_len=i

Block=[]
max_roof_1 = 0

x = []
for j in range(len(Arr)):
    if Arr[j][0] <= max_roof[0]:
        if max_roof_1==0:
            max_roof_1=Arr[j][1]
            x.append(Arr[j][0])
        else:
            if Arr[j][1] >= max_roof_1:
                TEMP = (Arr[j][0]-x.pop(0)) * max_roof_1
                max_roof_1 = Arr[j][1]
                Block.append(TEMP)
                x.append(Arr[j][0])

max_roof_2 = [0,0]
while True:
    if max_roof_2[0] != max_len[0]:
        for j in range(max_roof_2[0]+1,len(Arr)):
            if Arr[j][0] > max_roof[0]:
                if max_roof_2[1] <= Arr[j][1]:
                    max_roof_2 = Arr[j]

        Block.append(max_roof_2[1] * (max_roof_2[0] - max_roof[0]))
    else:
        break

print(sum(Block)+max_roof[1])