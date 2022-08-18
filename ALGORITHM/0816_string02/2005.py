import sys
sys.stdin=open('2005.text')

T= int(input())
for t in range(1,T+1):
    N = int(input())
    pascal = [1]
    
    for _ in range(1, N):
        my_pascal = []
        my_pascal.append(1) #왼쪽 끝에 1 추가

        # 중간은 이전 줄의 좌우 계산한 값
        for i in range(len(pascal) -1 ):
            my_pascal.append(pascal[i]+ pascal[i+1])

        my_pascal.append(1) # 우측 끝에 1 추가

    print(my_pascal)