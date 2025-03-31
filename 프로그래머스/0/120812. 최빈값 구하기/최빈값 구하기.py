def solution(array):
    answer = 0
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1
    maxnum = 0
    for i in count:
        if i == max(count):
            maxnum += 1
    if maxnum > 1:
        answer = -1
    else:
        answer = count.index(max(count))
    return answer