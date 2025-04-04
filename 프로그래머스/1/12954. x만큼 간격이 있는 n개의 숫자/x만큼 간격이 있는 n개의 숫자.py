def solution(x, n):
    answer = []
    addition = x
    for i in range (n):
        answer.append(x)
        x += addition
    return answer