def solution(board, skill):
    answer = 0

    for i in range(len(skill)):
        effect, start_y, start_x, end_y, end_x, value = skill[i][0],skill[i][1],skill[i][2],skill[i][3],skill[i][4],skill[i][5]
        if effect == 1:
            for x in range(start_y,end_y+1):
                for y in range(start_x,end_x+1):
                    board[x][y] -= value

        else:
            for x in range(start_y, end_y+1):
                for y in range(start_x, end_x+1):
                    board[x][y] += value
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] > 0:
                answer+= 1
    return answer

board =[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]

skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board,skill))

