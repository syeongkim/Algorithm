def solution(array, n):
    answer = array[0]
    for i in array[1:]:
        if (abs(answer- n) > abs(i - n)):
            answer = i
        elif (abs(answer - n) == abs(i - n)):
            answer = min(answer, i)
    return answer