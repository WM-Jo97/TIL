def max_score(scores):
    Ans=[]
    for i in range(len(scores)):
        if scores[i]>scores[i-1]:
            Ans=[]
            Ans.append(scores[i])
        else: pass
    return Ans


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
