def solution(n):
    answer = []
    index = -1
    for i in range(len(str(n))):
        answer.append(int(str(n)[index]))
        index -= 1
    return answer