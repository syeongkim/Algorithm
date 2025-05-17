def solution(message):
    answer = 0
    
    word = message.split()
    answer += len(word) - 1
    
    for i in word:
        answer += len(i)
    
    answer *= 2
    return answer