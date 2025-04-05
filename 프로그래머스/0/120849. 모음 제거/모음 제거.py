def solution(my_string):
    answer = ''
    remove_list = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i in remove_list:
            pass
        else:
            answer += i
    return answer