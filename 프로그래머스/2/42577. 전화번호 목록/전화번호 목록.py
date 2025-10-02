def solution(phone_book):
    answer = True
    hashDictionary = {}
    
    for phone in phone_book:
        hashDictionary[phone] = 1
        
    for phone in phone_book:
        temp = ''
        for num in phone:
            temp += num
            if temp in hashDictionary and temp != phone:
                answer = False
                return answer
    return answer