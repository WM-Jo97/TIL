import sys
sys.stdin=open('BECK_12.text')

N= int(input())
NUM_LIST=list(map(int,input().split()))
Stack=[]

if N > 1:
    NUM_plus=1
    for i in range(N-1):
        if NUM_LIST[i] <= NUM_LIST[i+1]:
            NUM_plus+=1
        else:
            Stack.append(NUM_plus)
            NUM_plus=1

    Stack.append(NUM_plus)

    NUM_minus = 1
    for j in range(N-1):
        if NUM_LIST[j] >= NUM_LIST[j+1]:
            NUM_minus+=1
        else:
            Stack.append(NUM_minus)
            NUM_minus=1

    Stack.append(NUM_minus)

    print(max(Stack))
else:
    print(1)