enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

parents = [[] for _ in range(len(enroll))]
benefit = [0]*len(enroll)

def solution(enroll, referral, seller, amount):
    for i in range(len(enroll)):
        if referral[i] == "-":
            pass
        else:
            mom = enroll.index(referral[i])
            parents[mom].append(enroll[i])
    print(parents)
    for j in range(len(seller)):
        seller_index = enroll.index(seller[j])
        benefit[seller_index] += amount[j]*90
        sell_person = seller[j]
        benefit_per = amount[j]*10
        while benefit_per > 1:
            for x in range(len(parents)):
                if sell_person in parents[x]:
                    benefit[x] += benefit_per - benefit_per//10
                    benefit_per = benefit_per//10
                    sell_person = enroll[x]
                    break
            else:
                break

    for i in range(len(benefit)):
        benefit[i] = int(benefit[i])

    return benefit

print(solution(enroll, referral, seller, amount))