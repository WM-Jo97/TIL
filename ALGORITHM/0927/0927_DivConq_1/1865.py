import sys
sys.stdin = open('example_4.text')

def Tast_distrbute(task_num,Employee):
    global Probability
    global ANS
    if task_num == N:
        if Probability*100 > ANS:
            ANS = Probability*100
            return
        else:
            return
    else:
        for i in range(len(Employee)):
            if Task[task_num][Employee[i]] != 0:
                TEMP = Task[task_num][Employee[i]] / 100
                Probability = Probability*TEMP
                A = Employee[i]
                Employee.remove(A)
                Tast_distrbute(task_num+1,Employee)
                Probability = Probability/TEMP
                Employee.append(A)
                Employee.sort()

        return

T = int(input())

for t in range(1,T+1):
    N = int(input())
    Task = []
    for i in range(N):
        Temp = list(map(int,input().split()))
        Task.append(Temp)

    Employee = list(range(N))
    Probability = 1
    task_num = 0
    ANS = 0
    Tast_distrbute(task_num,Employee)
    #print(Task)
    print(f'#{t} {format(ANS,".6f")}')