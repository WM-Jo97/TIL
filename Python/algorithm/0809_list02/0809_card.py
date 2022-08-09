import sys

sys.stdin = open('card.text')

T = int(input())
for t in range(1, T+1):
    Card_num = int(input())
    Card = list(map(int,input()))

    Card_count=[]

    for i in range(len(Card)):
        count = 0
        for j in range(len(Card)):
            if Card[i]==Card[j]:
                count+=1
                Card_count.append((Card[i],count))
    Card_set=set(Card_count)
    Card_set_list=list(Card_set)
    #print(Card_set_list)

    max_Card=0
    for i in Card_set_list:
        if i[1]>max_Card:
            max_Card=i[1]

    Max_Same_Card=[]
    for i in range(len(Card_set_list)):
        if Card_set_list[i][1]==max_Card:
            Max_Same_Card.append(Card_set_list[i][0])

    Mas_Same=0
    for i in Max_Same_Card:
        if i > Mas_Same:
            Mas_Same=i

    print(f'#{t} {Mas_Same} {count}')