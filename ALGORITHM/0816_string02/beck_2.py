import sys
sys.stdin=open('beck_2.text')

Students, Limit = map(int,input().split())

arr=[[0]*2 for _ in range(6)]

while True:
    try:
        A,B= map(int,input().split())
        arr[B-1][A]=arr[B-1][A]+1
    except:
        break

room=0
for i in range(len(arr)):
    for j in range(2):
        if arr[i][j] != 0:
            if arr[i][j]>Limit:
                if arr[i][j] % Limit !=0:
                    room+= arr[i][j]//Limit+1
                else:
                    room+= arr[i][j]/Limit
            else:
                room+=1

print(int(room))