import sys
sys.stdin=open('PRACTICE.text')

T=int(input())

for t in range(1,T+1):
    Input_Check=input()
    Stack=[]
    i = 0
    while i<len(Input_Check):
        if Input_Check[i] == '(':
            Stack.append('A')
            i+=1

        elif Input_Check[i] == ')':
            if len(Stack)!=0:
                Stack.pop()
                i+=1
            else:
                Stack.append('A')
                Stack.append('A')
                i+=1

    if len(Stack)==0:
        print(f'#{t} 1')
    else:
        print(f'#{t} -1')

