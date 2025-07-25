n = int(input())
sumLists = []

for _ in range(n):
    cards = list(map(int, input().split()))
    maxNumber = 0
    for i in range(0, 5, 1):
        for j in range(i+1, 5, 1):
            for k in range(j+1, 5, 1):
                sum = (cards[i] + cards[j] + cards[k]) % 10
                if (sum >= maxNumber):
                    maxNumber = sum
    sumLists.append(maxNumber)

for i in range(n-1, -1, -1):
    if sumLists[i] == max(sumLists):
        print(i + 1)
        break