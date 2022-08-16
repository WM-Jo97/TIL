import sys
sys.stdin=open("4865.text")

T=int(input())

for t in range(1,T+1):
    Str1=input()
    Str2=input()

    count=0
    for i in range(len(Str2)-len(Str1)+1):
        if Str1==Str2[i:i+len(Str1)]:
            count=1

    print(f'#{t} {count}')