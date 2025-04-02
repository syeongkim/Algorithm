def solution(num_list):
    answer = []
    odds = 0
    evens = 0
    for i in num_list:
        if (i % 2 == 1):
            odds += 1
        else:
            evens += 1
    answer.append(evens)
    answer.append(odds)
    return answer