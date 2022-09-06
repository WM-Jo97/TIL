import sys
sys.stdin=open('example.text')

T = int(input())

for t in range(1,T+1):
    charge_list = list(map(int,input().split()))
    day_year = list(map(int,input().split()))

    print(charge_list)
    print(day_year)

    for i in range(len(charge_list)):