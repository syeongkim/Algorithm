def solution(my_string):
    answer = ''
    index = -1
    for i in range(len(my_string)):
        answer += my_string[index]
        index -= 1
    return answer