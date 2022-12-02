def self_num(x):
    self_number = []
    for i in range(x+1):
        if i < 10:
            X_2 = '0'+str(i)
            self = i + int(X_2[0]) + int(X_2[1])
            self_number.append(self)

        elif i<100:
            self = i + int(str(i)[0]) + int(str(i)[1])
            self_number.append(self)

        elif i< 1000:
            self = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
            self_number.append(self)

        elif i< 10000:
            self = i+ int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
            self_number.append(self)

        else:
            self = i+ int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4])
            self_number.append(self)

    for j in range(x+1):
        if j not in self_number:
            print(j)


self_num(10000)