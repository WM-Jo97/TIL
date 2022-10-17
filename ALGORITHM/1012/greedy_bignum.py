N,M,K = 5,8,3
num_list = [2, 4, 5, 4, 6]

num_list.sort(reverse=True)

total = 0
while True:
    for i in range(K):
        if M == 0:
            break
        total += num_list[0]
        M -= 1
    if M==0:
        break
    else:
        total += num_list[1]
        M -= 1

print(total)

print(int(M/(K+1))*K + M%(K+1))
print((M//K+1)*K + M%(K+1))
print(9//2)