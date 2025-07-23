while True:
    n = int(input())
    if (n == 0):
        break
    else:
        words = []
        for _ in range(n):
            words.append(input())
        wordsLower = [i.lower() for i in words]
        minIndex = wordsLower.index(min(wordsLower))
        print(words[minIndex])