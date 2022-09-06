import sys
sys.stdin=open('example.text')

T = int(input())

for t in range(1,T+1):
    charge_list = list(map(int,input().split()))
    day_year = list(map(int,input().split()))

    print(charge_list)
    print(day_year)

    check_month = charge_list[1]//charge_list[0]
    check_3month = charge_list[2]//(3*charge_list[1])
    check_year_month = charge_list[3]/(12*charge_list[1])
    check_year_3mon = charge_list[3]/(4*charge_list[2])

    #print(check_month)
    #print(check_3month)
    #print(check_year_month)
    #print(check_year_3mon)

    check_month_list = [[0] for _ in range(12)]
    for i in range(len(day_year)):
        if charge_list[1] <= day_year[i]*charge_list[0]:
            check_month_list[i] = charge_list[1]
        else:
            check_month_list[i] = charge_list[0]*day_year[i]

    print(check_month_list)

    check_3month_list = [[0] for _ in range(12)]

    for j in range(len(day_year)-2):
        if charge_list[2] <= check_month_list[j]+check_month_list[j+1]+check_month_list[j+2]:
            check_3month_list[j] = charge_list[2]
            check_month_list[j+1] = 3000
            check_month_list[j+2] = 3000
        else:
            check_3month_list[j] = check_month_list[j]

    print(check_3month_list)
