import sys
sys.stdin=open('4871.text')

def DFS(v):
    result=[]
    Stack.append(v)
    while Stack:
        Point[v] = 1
        for next in adj_List[v]:
            if Point[next] != 1:
                Stack.append(v)
                v=next
                result.append(v)
                break
        else:
            v = Stack.pop()
    return result                     # 갔던 목적지를 기록한 리스트 리턴받기


T= int(input())
for t in range(1,T+1):
    V, E = map(int, input().split())
    adj_List = [[] for _ in range(V+1)]           # 비어있는 갈 수 있는 목적지 리스트

    for i in range(E):
        frm, to = map(int, input().split())
        adj_List[frm].append(to)
        #adj_List[to].append(frm)             #문제가 장난을 조금 쳐놨네요... 방향성이 일방향이므로 이 부분을 뺴야합니다.

    Start, Goal = map(int, input().split())


    Stack = []
    Point = [0 for _ in range(V+1)]

    if Goal in DFS(Start):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')