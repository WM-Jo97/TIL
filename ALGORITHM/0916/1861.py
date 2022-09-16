import sys
sys.stdin = open('example_2.text')

def Bfs(i,j): # 1~ N**2 정수
    Q = [(i,j)]
    visited = [[0]*N for _ in range(N)]
    result = []
    result.append(arr[i][j])
    visited[i][j] = 1
    while Q:
        i ,j = Q.pop(0)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for x in range(4):                           # 위치에서 델타 사용
            y = i + dy[x]
            x = j + dx[x]
            if 0<=y<N and 0<=x<N:
                if arr[y][x] == arr[i][j]+1 and visited[y][x] == 0:
                    Q.append((y,x))
                    result.append(arr[y][x])
                    visited[y][x] = 1
    return min(result), len(result)


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(N):
            arr[i][j] = temp[j]

    ANS = []
    for i in range(N):                 # 정수가 있는 위치를 찾고
        for j in range(N):
            start = [i, j]
            y = start[0]
            x = start[1]
            ANS.append(Bfs(y,x))

    ans=0
    point=0
    for i in range(len(ANS)):
        if ANS[i][1] > ans:
            ans = ANS[i][1]
            point = ANS[i][0]
        elif ANS[i][1] == ans:
            if point > ANS[i][0]:
                point = ANS[i][0]
    print(f'#{t} {point} {ans}')


