from collections import deque

def solution(users, emoticons):
    answer = []
    minDiscountRate = ((min([user[0] for user in users]) + 9) // 10) * 10
    discountRates = [rate for rate in [10, 20, 30, 40] if rate >= minDiscountRate]
    combinations = []
    queue = deque()
    queue.append([])
    while queue:
        curr = queue.popleft()
        if len(curr) == len(emoticons):
            combinations.append(curr)
        else:
            for rate in discountRates:
                newArray = [c for c in curr]
                newArray.append(rate)
                queue.append(newArray)
    
    result = []
    for combination in combinations:
        discountedPrices = []
        for i in range(len(combination)):
            discountedPrice = int(((100 - combination[i]) * emoticons[i]) / 100)
            discountedPrices.append(discountedPrice)
        
        totalRegisters = 0
        totalSoldAmount = 0
        
        for u in users:
            userPayAmount = 0
            for e in range(len(emoticons)):
                if combination[e] >= u[0]:
                    userPayAmount += discountedPrices[e]
            if userPayAmount >= u[1]:
                totalRegisters += 1
            else:
                totalSoldAmount += userPayAmount
        
        result.append([totalRegisters, totalSoldAmount])
    sortedResult = sorted(result, key = lambda x: (-x[0], -x[1]))
    answer = sortedResult[0]
    
    return answer