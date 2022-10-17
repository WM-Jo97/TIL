import sys
sys.stdin = open('example_1.text')

def make_lineup(BAT_NUM, potential, visited):
    global lineup

    if len(lineup) == 8:
        lineup.insert(3,0)
        temp = []
        for i in range(len(lineup)):
            temp.append(lineup[i])
            potential.append(temp)
        lineup.remove(0)
        return

    for i in range(len(BAT_NUM)):
        if visited[i] == 0:
            visited[i] = 1
            lineup.append(BAT_NUM[i])
            make_lineup(BAT_NUM,potential,visited)
            visited[i] = 0
            lineup.pop(-1)
    return


def make_score(inning, num_i):
    global potential

    inning_num = 0
    score = 0
    base = [0]* 3
    batting_num = 0
    out = 0

    while True:
        if inning_num == N:
            break

        else:
            j = potential[num_i][batting_num]

            if inning[inning_num][j] == 0:
                out += 1

            elif inning[inning_num][j] == 1:
                for i in range(2,-1,-1):
                    if i == 2:
                        if base[2] == 1:
                            score += 1
                            base[2] = 0
                    elif i == 1:
                        if base[1] == 1:
                            base[2] = 1
                            base[1] = 0
                    elif i == 0:
                        if base[0] == 1:
                            base[1] = 1
                        base[0] = 1

            elif inning[inning_num][j] == 2:
                for i in range(2,-1,-1):
                    if i == 2:
                        if base[2] == 1:
                            score += 1
                            base[2] = 0
                    elif i == 1:
                        if base[1] == 1:
                            score += 1
                            base[1] = 0
                    elif i == 0:
                        if base[0] == 1:
                            base[2] = 1
                            base[0] = 0
                        base[1] = 1

            elif inning[inning_num][j] == 3:
                for i in range(2,-1,-1):
                    if i == 2:
                        if base[2] == 1:
                            score += 1
                            base[2] = 0
                    elif i == 1:
                        if base[1] == 1:
                            score += 1
                            base[1] = 0
                    elif i == 0:
                        if base[0] == 1:
                            score += 1
                            base[0] = 0
                        base[2] = 1

            elif inning[inning_num][j] == 4:
                for i in range(2,-1,-1):
                    if i == 2:
                        if base[2] == 1:
                            score += 1
                            base[2] = 0
                    elif i == 1:
                        if base[1] == 1:
                            score += 1
                            base[1] = 0
                    elif i == 0:
                        if base[0] == 1:
                            score += 1
                            base[0] = 0
                        score += 1

            if out == 3:
                inning_num += 1
                out = 0

            if batting_num == 8:
                batting_num = 0
            else:
                batting_num += 1

    return score


N = int(input())

inning = []
for i in range(N):
    BATTER = list(map(int,input().split()))
    inning.append(BATTER)

BAT_NUM = list(range(1,9))

lineup = []
potential = []
visited = [0]*8
make_lineup(BAT_NUM, potential, visited)

max_score = 0
for i in range(len(potential)):
    num_i = i
    score = make_score(inning, num_i)

    if score >= max_score:
        max_score = score

print(max_score)

