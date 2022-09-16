import sys
sys.stdin = open('example_3.text')

def search(R,C):
    if 0<=R<N and 0<=C<M and arr[R][C] != 0:
        if visited[R][C] == 0:
            if arr[R][C] == 1:
                visited[R][C]=1
                answer.append(1)
                search(R,C+1)
                search(R,C-1)
                search(R+1,C)
                search(R-1,C)
            elif arr[R][C] == 2:
                if (0<=R+1<N and 0<=C<M and arr[R+1][C] !=0) or (0<=R+1<N and 0<=C<M and arr[R-1][C]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R+1,C)
                    search(R-1,C)
            elif arr[R][C] == 3:
                if (0<=R<N and 0<=C-1<M and arr[R][C-1] !=0) or (0<=R<N and 0<=C+1<M and arr[R][C+1]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R,C-1)
                    search(R,C+1)
            elif arr[R][C] == 4:
                if (0<=R-1<N and 0<=C<M and arr[R-1][C] !=0) or (0<=R<N and 0<=C+1<M and arr[R][C+1]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R-1,C)
                    search(R,C+1)
            elif arr[R][C] == 5:
                if (0<=R+1<N and 0<=C<M and arr[R+1][C] !=0) or (0<=R<N and 0<=C+1<M and arr[R][C+1]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R+1,C)
                    search(R,C+1)
            elif arr[R][C] == 6:
                if (0<=R+1<N and 0<=C<M and arr[R+1][C] !=0) or (0<=R<N and 0<=C-1<M and arr[R][C-1]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R+1,C)
                    search(R,C-1)
            elif arr[R][C] == 7:
                if (0<=R-1<N and 0<=C<M and arr[R-1][C] !=0) or (0<=R<N and 0<=C-1<M and arr[R][C-1]!=0):
                    visited[R][C] = 1
                    answer.append(1)
                    search(R-1,C)
                    search(R,C-1)
    else:
        return


T = int(input())
for t in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = []
    for i in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)


    visited = [[0]*M for _ in range(N)]

    answer=[]
    search(R, C)
    print(len(answer))