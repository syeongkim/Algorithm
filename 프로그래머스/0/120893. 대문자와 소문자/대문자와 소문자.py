def solution(my_string):
    answer = ''
    for i in my_string:
        if (i.lower() == i):
            answer += i.upper()
        else:
            answer += i.lower()
    return answer