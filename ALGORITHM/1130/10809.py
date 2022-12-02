import string
alphabet = list(string.ascii_lowercase)

S = input()
# S = 'beckjoon'
n_list = []
for i in range(len(alphabet)):
    n_list.append(S.find(alphabet[i]))

print(*n_list)