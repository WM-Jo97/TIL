import sys
sys.stdin=open('4866.text')

T= int(input())

for t in range(1, T+1):
    Check = input()
    Stack = []
    for i in Check:
        if i == '(':
            Stack.append('(')
        elif i == '{':
            Stack.append('{')
        elif i == ')':
            if Stack: # and Stack[-1]=='(':
                Stack.pop()
            else:
                Stack.append('(')
                Stack.append('(')
        elif i == '}':
            if Stack and Stack[-1]=='{':
                Stack.pop()
            else:
                Stack.append('(')
                Stack.append('(')

    if not Stack:
        print(f'#{t} 1')

    else:
        print(f'#{t} 0')