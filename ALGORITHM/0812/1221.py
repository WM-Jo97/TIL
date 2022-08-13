import sys
sys.stdin=open('1221.text')

def Bubble(List,lenth):
    for i in range(lenth-1, 0, -1):
        for j in range(0,i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1],List[j]

ATOI ={
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,          #총 3가지 정도 절차로 -> 1번 디렉토리 이용, 받은 string을 int로
        'THR' : 3,                                  #2번 -> 버블소팅 이용해서 0부터 9까지 정렬
        'FOR' : 4,                                  #3번 -> 디렉토리 이용 int를 string으로
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

ITOA = {
        0: 'ZRO',
        1: 'ONE',
        2: 'TWO',
        3: 'THR',
        4: 'FOR',
        5: 'FIV',
        6: 'SIX',
        7: 'SVN',
        8: 'EGT',
        9: 'NIN',
    }

T=int(input())

for t in range(1,1+T):
    Case, lenth = input().split( )
    Numbers=input().split()
    lenth=int(lenth)

    Int_list=[]
    for i in Numbers:
        Int_list.append(ATOI.get(i))

    Bubble(Int_list,lenth)

    print(f'#{t}')
    for i in Int_list:
        print(ITOA.get(i)+' ', end='')

    print()