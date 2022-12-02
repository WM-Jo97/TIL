def hansu(x):
    count = 0
    for i in range(1,x+1):
        if i < 100:
            count+=1

        elif i < 1000:
            if (int(str(i)[2]) - int(str(i)[1])) == (int(str(i)[1])-int(str(i)[0])):
                count+=1

        else:
            if (int(str(i)[2]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[0])):
                if (int(str(i)[3]) - int(str(i)[2])) == (int(str(i)[2]) - int(str(i)[1])):
                    count += 1

    print(count)


N = int(input())
hansu(N)
