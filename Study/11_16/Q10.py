def solution(key, lock):
    answer = False
    result_num = 0

    num_list = []
    for i in range(len(key)-1,0,-1):
        num_list.append(-i)
    for i in range(len(key)):
        num_list.append(i)

    count = 0
    while result_num != 4:
        reverse_key = key[::-1]
        rotated_key = list(zip(*reverse_key))

        open = []
        for x in range(len(lock)):
            temp = []
            for y in range(len(lock)):
                temp.append(lock[x][y])
            open.append(temp)

        for number in num_list:
            for i in range(len(key)):
                for j in range(len(key)):
                    if 0<= i+number <len(key):
                        open[i][j] = open[i][j] + rotated_key[i+number][j]

            total = 0
            for q in range(len(open)):
                for p in range(len(open[q])):
                    if open[q][p] == 1:
                        total += 1

            if total == len(key) * len(key):
                count += 1

            open = []
            for x in range(len(lock)):
                temp = []
                for y in range(len(lock)):
                    temp.append(lock[x][y])
                open.append(temp)

            for i in range(len(key)):
                for j in range(len(key)):
                    if 0 <= j + number < len(key):
                        open[i][j] = open[i][j] + rotated_key[i][j+number]

            total = 0
            for q in range(len(open)):
                for p in range(len(open[q])):
                    if open[q][p] == 1:
                        total += 1

            if total == len(key) * len(key):
                count += 1

            open = []
            for x in range(len(lock)):
                temp = []
                for y in range(len(lock)):
                    temp.append(lock[x][y])
                open.append(temp)


            for i in range(len(key)):
                for j in range(len(key)):
                    if 0 <= i + number < len(key) and 0<= j+ number < len(key):
                        open[i][j] = open[i][j] + rotated_key[i+number][j+number]

            total = 0
            for q in range(len(open)):
                for p in range(len(open[q])):
                    if open[q][p] == 1:
                        total += 1

            if total == len(key) * len(key):
                count += 1

            open = []
            for x in range(len(lock)):
                temp = []
                for y in range(len(lock)):
                    temp.append(lock[x][y])
                open.append(temp)

        result_num += 1
    if count != 0:
        answer = True

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key,lock)