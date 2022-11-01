def solution(words, queries):
    answer = []
    for i in range(len(queries)):
        count_word = 0
        for  j in range(len(words)):
            if len(queries[i]) == len(words[j]) and (queries[i][0] == words[j][0] or queries[i][-1]== words[j][-1]):
                count = 0
                for x in range(len(queries[i])):
                    if queries[i][x] == words[j][x]:
                        count += 1
                    elif queries[i][x] == '?':
                        count += 1
                if count == len(queries[i]):
                    count_word += 1
        answer.append(count_word)
    return answer