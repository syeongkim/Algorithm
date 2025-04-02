def solution(seoul):
    answer = ''
    for i in seoul:
        if (i == 'Kim'):
            index = seoul.index(i)
    answer = "김서방은 " + str(index) + "에 있다"
    return answer