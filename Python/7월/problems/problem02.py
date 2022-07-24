def over(scores):
    count=0
    for i in range(len(scores)):
        if scores[i]>=60:
            count+=1
        else:
            pass
    return count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
