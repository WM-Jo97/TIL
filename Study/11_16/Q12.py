def solution(n, build_frame):
    construction = [[0]*(n+2) for _ in range(n+2)]
    answer = []

    for task in build_frame:
        x, y, beam, install = task[0], task[1], task[2], task[3]

        if install == 1:
            if beam == 0:
                if y == 0 and construction[y][x]==0:
                    construction[y][x] = 1
                    construction[y+1][x] = 1
                    answer.append([x,y,beam])

                elif construction[y][x] != 0:
                    construction[y][x] = 1
                    construction[y + 1][x] = 1
                    answer.append([x, y, beam])
            else:
                if x+2 < n+1:
                    if (construction[y][x]==1 and construction[y][x+1]!=2) or (construction[y][x+2] == 1 and construction[y][x+1]!=2):
                        construction[y][x+1] = 2
                        answer.append([x, y, beam])

                    elif construction[y][x+1] == 1:
                        construction[y][x+1] = 2
                        answer.append([x,y,beam])

                    elif construction[y][x] == 2 and construction[y][x+2]== 2 and construction[y][x+1]!=3:
                        construction[y][x+1] = 3
                        answer.append([x, y, beam])
                else:
                    if construction[y][x]==1 and construction[y][x+1]!=2:
                        construction[y][x+1] = 2
                        answer.append([x, y, beam])

                    elif construction[y][x+1] == 1:
                        construction[y][x+1] = 2
                        answer.append([x,y,beam])

                    elif construction[y][x] == 2 and construction[y][x+2] == 2 and construction[y][x+1]!=3:
                        construction[y][x+1] = 3
                        answer.append([x, y, beam])
        else:
            if beam== 0:
                if construction[y+1][x-1] == 2 and construction[y+1][x+1] == 2:
                    construction[y+1][x] = 3
                    construction[y][x] = 0
                    answer.remove([x,y,beam])

                elif construction[y+1][x-1] == 1 or construction[y+1][x+1] == 1:
                    construction[y+1][x] = 2
                    construction[y][x] = 0
                    answer.remove([x,y,beam])

    answer.sort()
    # print(answer)
    # print(construction)
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

solution(n,build_frame)