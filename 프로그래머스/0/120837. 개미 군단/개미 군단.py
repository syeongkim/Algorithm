def solution(hp):
    answer = 0
    numof5 = hp // 5
    hp = hp % 5
    numof3 = hp // 3
    hp = hp % 3
    numof1 = hp
    answer = numof5 + numof3 + numof1
    return answer