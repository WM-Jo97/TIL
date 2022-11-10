import sys
sys.stdin=open('example_3.text')
input = sys.stdin.readline
N = input()
Target = N
if len(N) == 1:
    N = '0'+N[0]
count = 0
while True:
    A,B = N[0],N[1]
    C = str(int(A)+int(B))
    if len(C) == 1:
        C = '0'+C
    C = C[-1]
    N = B+C
    count+=1

    if int(N) == int(Target):
        break

print(count)
