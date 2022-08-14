import sys
sys.stdin=open('input.text')

def time(x,y,z):
    if y-z < 0:
        if x-1>0:
            x=x-1
            y=60+(y-z)
            if y < 0:
                if x - 1 > 0:
                    x = x-1
                    y = 60+y



        else:
            x=24+(x-1)
            y=60+(y-z)
            if y < 0:
                if x - 1 > 0:
                    x = x-1
                    y = 60+y

    else:
        x=x
        y=y-z

    if x==24:
        x=0

    return x,y

T=list(map(int, input().split()))
Z=int(input())
x=T[0]
y=T[1]
z=Z
a=time(x,y,z)
print(f'{a[0]} {a[1]}')