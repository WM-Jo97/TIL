import sys
sys.stdin = open('example_1.text')

def make_lineup(BAT_NUM,potential, visited):

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

N = int(input())

inning = []
for i in range(N):
    BATTER = list(map(int,input().split()))
    inning.append(BATTER)

print(inning)
BAT_NUM = list(range(1,9))

lineup = []
potential = []
visited = [0]*8

make_lineup(BAT_NUM, potential, visited)

print(potential)

num_i = 0
inning_num = 0
out = 0
base = [[0]*3]
score = 0
batting_num = 0
while inning_num != N:
    i = potential[num_i][batting_num]
    if inning[inning_num][i] ==0:
        out += 1

    elif inning[inning_num][i] == 1:
        for i in range(2,-1,-1):
            if i == 2:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 1:
                if base[i] == 1:
                    base[2] = 1
                    base[i] = 0
            elif i == 0:
                if base[i] == 1:
                    base[1] = 1
                base[0] = 1

    elif inning[inning_num][i] == 2:
        for i in range(2, -1, -1):
            if i == 2:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 1:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 0:
                if base[i] == 1:
                    base[2] = 1
                    base[i] = 0
                base[1] = 1

    elif inning[inning_num][i] == 3:
        for i in range(2, -1, -1):
            if i == 2:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 1:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 0:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
                base[2] = 1

    elif inning[inning_num][i] == 4:
        for i in range(2, -1, -1):
            if i == 2:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 1:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
            elif i == 0:
                if base[i] == 1:
                    score += 1
                    base[i] = 0
                score += 1

    if out == 3:
        inning_num += 1

print(inning)