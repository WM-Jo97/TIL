import sys
sys.stdin = open('example_4.text')

def dfs(start,end,x,num,ANS):
    global visited , N, COSTOMER, JOB
    if sum(visited) == N:
        print(ANS)
        return

    else:
        if visited[x] == 1:
            return
        else:
            print(x)
            visited[x] = visited[x]+1
            print(visited)
            x,y = start
            a,b = end
            ANS+=abs(a-x)+abs(b-y)
            for x in range(N):
                dfs(end, COSTOMER[x], x, num + 1, ANS)
                visited[x] = visited[x]-1

T = int(input())

for t in range(1,T+1):
    N = int(input())
    TEMP = list(map(int,input().split()))
    loca_list = []
    for i in range(0,len(TEMP),2):
        loca_list.append((TEMP[i],TEMP[i+1]))

    JOB = loca_list[0]
    HOME = loca_list[1]
    COSTOMER = loca_list[2:]

    visited = [0]*N

    num = 1
    ANS = 0
    for i in range(N):
        visited[i] = 1
        dfs((0,0),COSTOMER[i],i,num,ANS)
        num = 1
        ANS = 0