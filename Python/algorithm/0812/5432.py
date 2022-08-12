import sys
sys.stdin=open('5432.text')

T=int(input())

for t in range(1, T+1):
    M = input()

    for i in range(len(M)):
        count = 0
        if i == '(':
            while i<len(M):
                count+=1
                i+=1
        print(count)