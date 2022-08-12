text='This is a book!'
pattern='is'



def BruteForce(pattern, text):
    M= len(pattern) #패턴의 길이
    N= len(text)       # 텍스트의 길이
    for idx in range(N-M+1):
        for jdx in range(M):
            if pattern[jdx] != text[idx]:
                break
            else: #패턴이 매칭된 상태
                return idx
    else:
        return -1

print(BruteForce(pattern,text))