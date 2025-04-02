def solution(num_list):
    answer = []
    index = -1
    for i in range(len(num_list)):
        answer.append(num_list[index])
        index -= 1
    return answer