def solution(num, k):
    answer = -1
    numStr = str(num)
    
    for i in range(len(numStr)):
        if numStr[i] == str(k):
            answer = i + 1
            break
    return answer