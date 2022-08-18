import sys
sys.stdin=open('1219.text')

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

for i in range(1,11):
    t, E = map(int, input().split())
    input_list = list(map(int, input().split()))

    V=99
    adj_List = [[] for _ in range(V+1)]           # 비어있는 갈 수 있는 목적지 리스트
    for i in range(0,E):
        adj_List[input_list[2*i]].append(input_list[2*i+1])


    Stack = []
    Point = [0 for _ in range(V+1)]

    if 99 in DFS(0):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
