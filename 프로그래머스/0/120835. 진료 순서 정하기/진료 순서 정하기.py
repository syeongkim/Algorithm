def solution(emergency):
    answer = [0] * len(emergency)
    prior = 1
    while (prior != len(emergency) + 1):
        maxval = max(emergency)
        answer[emergency.index(maxval)] = prior
        prior += 1
        emergency[emergency.index(maxval)] = -1
    return answer