def solution(key, lock):
    answer = False
    result_num = 1
    while result_num != 6:
        for _ in range(result_num):
            result = [[0]*len(lock) for _ in range(len(lock))]
            for i in range(len(lock)):
                for j in range(len(lock)):
                    result[j][len(lock)-i-1] = key[i][j]

        for i in range(len(key)):
            for j in range(len(key)):
                x_p = i
                y_p = j
                print(x_p, y_p)
                answer_list = []
                lock_plus = [[0]*len(lock) for _ in range(len(lock))]
                lock_minus = [[0] * len(lock) for _ in range(len(lock))]
                for y in range(len(lock)):
                    for x in range(len(lock)):
                        if 0<=y+y_p<len(lock) and 0<=x+x_p<len(lock):
                            lock_plus[y][x] = lock[y][x] + key[y+y_p][x+x_p]


                        if 0<=y-y_p<len(lock) and 0<=x-x_p<len(lock):
                            lock[y][x] = lock[y][x] + key[y-y_p][x-x_p]

                count_plus=0
                for i in range(len(lock_plus)):
                    for j in range(len(lock_plus)):
                        if lock_plus[i][j] == 1:
                            pass
                        else:
                            break

                if count_plus == len(lock_plus)**2:
                    answer_list.append(lock_plus)

                count_minus = 0
                for i in range(len(lock_minus)):
                    for j in range(len(lock_minus)):
                        if lock_minus[i][j] == 1:
                            count_minus+=1
                        else:
                            break
                if count_minus == len(lock_minus)**2:
                    answer_list.append(lock_minus)
                print(answer_list)
        result_num += 1
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key,lock)