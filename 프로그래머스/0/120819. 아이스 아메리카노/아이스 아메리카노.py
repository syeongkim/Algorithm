def solution(money):
    answer = []
    unit = money // 5500
    change = money % 5500
    answer.append(unit)
    answer.append(change)
    return answer