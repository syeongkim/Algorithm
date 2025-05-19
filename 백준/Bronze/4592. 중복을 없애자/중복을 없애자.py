while True:
    a = input()
    num = a.split(' ')
    temp = []
    if (num[0] == '0'):
        break
    else:
        for j in range(int(num[0])):
            if (len(temp) == 0):
                temp.append(num[j+1])
            else:
                if (temp[-1] != num[j+1]):
                    temp.append(num[j+1])
        for k in temp:
            print(k, end = " ")
        print ("$")
            