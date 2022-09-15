import sys
sys.stdin=open('example_3.text')

def preorder(n,answer):
    if n:
        preorder(son1[n],answer)
        answer.append(n)
        preorder(son2[n],answer)


T = int(input())
for t in range(1,T+1):
    N = int(input())
    son1 = [0] * (N + 1)
    son2 = [0] * (N + 1)
    for i in range(2, N + 1):
        if i % 2 == 0:
            for j in range(1, N + 1):
                if son1[j] == 0:
                    son1[j] = i
                    break
        elif i % 2 == 1:
            for j in range(1, N + 1):
                if son2[j] == 0:
                    son2[j] = i
                    break

    answer = []*(N+1)
    preorder(1,answer)
    Ans1 = 0
    Ans2 = 0
    for i in range(len(answer)):
        if answer[i] == 1:
            Ans1 = i+1
        elif answer[i] ==N//2:
            Ans2 = i+1
    print(f'#{t} {Ans1} {Ans2}')