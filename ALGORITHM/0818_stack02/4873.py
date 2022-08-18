import sys
sys.stdin=open('4873.text')

T= int(input())

for t in range(1,T+1):
    Stack=[]                     # 스택 생성
    Alpha = input()              # 문자열 받기
    for i in Alpha:              # 문자열 순회
        if not Stack:            # Stack 비어있으면
            Stack.append(i)      # Stack에 i 넣기
        else:
            if Stack[-1]==i:     # Stack 마지막이 i랑 같으면
                Stack.pop()      # i 뺴기
            else:
                Stack.append(i)  # 같지않으면 Stack에 추가

    print(f'#{t} {len(Stack)}')