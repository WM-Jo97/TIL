import sys
sys.stdin=open('5432.text')

T=int(input())

for t in range(1, T+1):
    M = input()
    count=0  #쇠막대기의 수
    num=0    # 쇠막대기 도막의 수
    for i in range(len(M)):
        if M[i]=='(' and M[i+1]==')':   #() 는 레이저 이므로 만약 레이저 이면 쇠막대기의 수만큼 도막이 생김
            num+=count
        elif M[i]=='(' and M[i+1]!=')':
            count+=1                    #( 는 쇠막대기가 생성되는 것이므로 쇠막대의 수를 하나 추가
            num+=1                      # 쇠막대에 레이저를 쏘면 도막의 수는 레이저의 수+1이 됨. 따라서 처음에 도막의 수를 하나 추가
        elif M[i]==')'and M[i-1]!='(':
            count-=1                    # )가 나오면 도막이 끝나므로 쇠막대의 수 하나 감소

    print(f'#{t} {num}')