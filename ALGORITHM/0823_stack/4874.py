import sys
sys.stdin=open('4874.text')

T= int(input())

for t in range(1,T+1):
    Stack = []
    TEMP=[]
    NUMS = list(input().split())

    try:
        for i in NUMS:
            if i == '+':
                TEMP.append(Stack.pop())
                TEMP.append(Stack.pop())
                Stack.append(int(TEMP[1])+int(TEMP[0]))
                TEMP=[]
            elif i == '-':
                TEMP.append(Stack.pop())
                TEMP.append(Stack.pop())
                NUMS.append(int(TEMP[1]) - int(TEMP[0]))
                TEMP = []
            elif i == '*':
                TEMP.append(Stack.pop())
                TEMP.append(Stack.pop())
                Stack.append(int(int(TEMP[1]) * int(TEMP[0])))
                TEMP = []
            elif i == '/':
                TEMP.append(Stack.pop())
                TEMP.append(Stack.pop())
                Stack.append(int(TEMP[1]) // int(TEMP[0]))
                TEMP = []
            elif i == '.':
                if len(Stack)==1:
                    print(f'#{t} {Stack.pop()}')
                else:
                    print(f'#{t} error')
            else:
                Stack.append(i)
    except:
        print(f'#{t} error')