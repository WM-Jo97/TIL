T = int(input())

for t in (1,T+1):
    N = int(input())
    value = ''
    for i in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)
        value += Ci*Ki
    print(f'#{t}')
    
    for i in range(len(value)):
        if (i+1)%10 == 0:
            print(value[i])
        else:
            print(value[i], end = "")
    print()
