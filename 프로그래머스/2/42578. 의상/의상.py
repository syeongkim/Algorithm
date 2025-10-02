def solution(clothes):
    answer = 1
    hashDictionary = {}
    for cloth in clothes:
        item, category = cloth[0], cloth[1]
        if category in hashDictionary:
            hashDictionary[category] += 1
        else:
            hashDictionary[category] = 1
            
    for category in hashDictionary:
        answer *= (hashDictionary[category] + 1)
    answer -= 1
    return answer