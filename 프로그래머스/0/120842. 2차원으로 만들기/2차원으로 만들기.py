def solution(num_list, n):
    answer = []
    while (len(num_list)):
        answer.append(num_list[0:n])
        num_list = num_list[n:]
    return answer