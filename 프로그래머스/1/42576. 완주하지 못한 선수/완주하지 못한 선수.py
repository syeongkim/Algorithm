def solution(participant, completion):
    answer = ''
    hashDictionary = {}
    sumHash = 0
    
    for p in participant:
        hashDictionary[hash(p)] = p
        sumHash += hash(p)
        
    for c in completion:
        sumHash -= hash(c)
        
    answer = hashDictionary[sumHash]
    return answer