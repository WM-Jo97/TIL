import sys
sys.stdin = open('example.text')

N = int(input()) # 사야하는 카드의 갯수
Card = [0] + list(map(int,input().split()))
# 제일 첫번째 항에 0을 추가해야 1개의 카드를 구할때부터라는 직관적인 코드 구성 가능합니다.
Price = [0 for _ in range(N+1)]
'''
최대 값을 저장하기 위한 리스트를 만들어줍니다.
DP에서는 이렇게 계산한 값을 저장해서 바로 불러옴으로써 
반복되는 계산 과정을 생략할 수 있습니다.
'''

for i in range(1,N+1): # 1개를 구하는 가장 비싼 값부터 N까지 차례로 올라가기 위해 for문 이용
    for k in range(1,i+1): # 1부터 i까지 범위를 설정해야 Price가 0 이하가 되지 않음
        Price[i] = max(Price[i], Price[i-k] + Card[k])
#Price[i-k] 와 Card[k] 를 이용하면 i와 k를 합해서 늘 i개를 유지 가능
print(Price[i])

'''
1장을 사는 방법
Price[1] = Card[1]
Price[2] = 카드 1장 + 카드 1장
           (카드 2장) 
Price[3] = (카드 2장) + 카드 1장
            카드 1장 + 카드 2장
            카드 0장 + 카드 3장

Price[4]
4장

i = 4
k = 1~4

Price[4] = max(Price[4], Price[4-k] + Card[k] )
k = 1
Price[3] + Card[1] # 3개를 사는 가장 비싼 방법 + 1개를 사는 카드팩의 가격
-> Price[4] = 위에꺼
k = 2
Price[4] = max(Price[4], Price[4-2] + Card[2] )

Price[4-2] -> 2개를 사는 가장 비싼 방법  + 2개를 사는 카드팩의 가격
              
4장
1장팩 + 3팩 (3개를 사는 가장 비싼 방법)
        2장 +1 장 
        1장 +1장 + 1장

2장팩 + 2장팩 (2개를 사는 가장 비싼 방법)
        1장 + 1장
4장팩 
'''