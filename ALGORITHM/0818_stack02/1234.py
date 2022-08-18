import sys
sys.stdin=open('1234.text')

T=10
for t in range(1,11):
    N , Alpha = input().split()
    Stack = []
    for i in range(int(N)):
        if not Stack:
            Stack.append(Alpha[i])

        else:
            if Alpha[i] == Stack[-1]:
                Stack.pop()
            else:
                Stack.append(Alpha[i])

    print(f'#{t}', end=' ')
    for i in Stack:
        print(i,end='')
    print()
