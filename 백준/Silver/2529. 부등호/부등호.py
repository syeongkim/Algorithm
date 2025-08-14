k = int(input())
signList = input().split()

def checkSign(num1, sign, num2):
    if sign == "<":
        return num1 < num2
    else:
        return num1 > num2

def getNumbers(numLists, depth):
    if depth == k:
        return numLists
    newNumLists = []
    for num in numLists:
        availableNumbers = []
        for i in range(10):
            if str(i) not in num:
                availableNumbers.append(str(i))
        for j in availableNumbers:
            prev = num[-1]
            if (checkSign(prev, signList[depth], j)):
                newNumber = num + j
                newNumLists.append(newNumber)
    return getNumbers(newNumLists, depth+1)
    
answers = getNumbers([str(i) for i in range(10)], 0)
        
print(max(answers))
print(min(answers))