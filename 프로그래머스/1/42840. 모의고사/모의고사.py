def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    oneCnt = 0
    twoCnt = 0
    threeCnt = 0
    for i in range(len(answers)):
        if one[i%len(one)] == answers[i]:
            oneCnt += 1
        if two[i%len(two)] == answers[i]:
            twoCnt += 1
        if three[i%len(three)] == answers[i]:
            threeCnt += 1
            
    maxCnt = max(oneCnt, twoCnt, threeCnt)
    if oneCnt == maxCnt:
        answer.append(1)
    if twoCnt == maxCnt:
        answer.append(2)
    if threeCnt == maxCnt:
        answer.append(3)
    return answer