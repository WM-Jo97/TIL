def pre_process(pattern):
    M = len(pattern) #패턴의 길이

    skip_table = dict()
    for i in range(M-1):
        skip_table[pattern[i]] = M- i -1

    return skip_table




def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    M = len(pattern)
    print(pre_process(pattern))
    i = 0 #text index
    while i <= len(text) - M:
        j = M -1 #뒤에서 비교해야하기 때문에 j 를 끝 인덱스로 설정
        k = i+(M-1) #비교를 시작할 위치 (현재 위치 + M번째 인덱스)

        while j>=0 and pattern[j] == text[k]: #비교할 j가 남아있고, text와 pattern 이 일치하면 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
            j-=1
            k-=1

        if j==-1 : #일치함
            return i

        else: #일치하지 않으면
            i += skip_table.get(text[i+M-1], M) #i를 비교할 시작 위치를 skip_table에서 가져온다.

    return -1

print(boyer_moore('ABC ABCDAB ABCDABCDABDE','ABCDABD'))