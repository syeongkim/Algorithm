def solution(order):
    answer = 0
    for i in str(order):
        if ((i == '3') | (i == '6') | (i == '9')):
            answer += 1
    return answer