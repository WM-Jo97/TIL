import sys
sys.stdin = open('3143.text')

T= int(input())

for t in range(1,T+1):
    Text, Pattern=input().split()

    count=0
    i=0
    while i<len(Text):
        if Text[i:i+len(Pattern)]==Pattern:
            count+=1
            i+=len(Pattern)
        else:
            count+=1
            i+=1

    print(f'#{t} {count}')

