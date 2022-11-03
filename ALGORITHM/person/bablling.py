
babbling = ["aya", "yee", "u", "maa", "wyeoo"]

def solution(babbling):
    answer = 0
    pro = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(len(pro)):
            if pro[j] in babbling[i]:
                print(babbling[i])

    return answer

print(solution(babbling))