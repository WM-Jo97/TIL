N= int(input())

for i in range(N):
    x,y = input().split()
    y = list(y)
    New_Str = ''

    for i in y:
        New_Str += i * int(x)

    print(New_Str)