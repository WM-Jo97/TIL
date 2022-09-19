import sys
sys.stdin = open('example.text')

T = int(input())

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}


for t in range(1,T+1):
    N, M= map(int,input().split())
    arr = []
    for i in range(N):
        temp = input()
        location = 0
        if arr:
            continue
        while location < M-7:
            location += 1
            if temp[location:location+7] in password and not int(temp[location+7]):
                arr.append(password[temp[location:location+7]])
                location += 6

    if (sum(arr)+2*sum(arr[0:7:2]))%10==0:
        SUM = sum(arr)
    else:
        SUM = 0

    print(f'#{t} {SUM}')
