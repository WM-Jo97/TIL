def pre_process(pattern):
    #전처리를 위한 테이블을 작성 (LPS longest prefix suffix)
    lps = [0] *len(pattern)
    j=0 #lps를 만들기 위한 prefix index

    for i in range(1,len(pattern)): #0번째 자리는 패턴 확인할 필요 없음

        #prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:                                                      #AABAA
            lps[i]=j+1       # i 의 앞에 중복되는 패턴이 존재한다                         #AABAA
            j+=1             # j 는 중복된 글자의 자리 수                                 #LPS=[0,1,0,1,2]
        else:
            j=0
            #여기서 0으로 이동한 다음 prefix idx 비교를 한번 더 해야함.

            if pattern[i] == pattern[j]:
                lps[i] = j+1
                j+=1

    return lps
print(pre_process('AABAA'))
def KMP(text, pattern):
    lps = pre_process(pattern) #전처리로 lps 테이블 생성

    i=0 # text index
    j=0 # pattern index
    while i < len(text):

        if pattern[j] == text[i]:
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+= 1

        if j == len(pattern): #pattern 이 전부 일치할 때
            return  i-j       #text의 위치

    return -1                 #일치하는 문장이 없는 경우


pattern='ABCDABD'
text = 'ABC ABCDAB ABCDABCDABDE'
print(KMP(text,pattern))

