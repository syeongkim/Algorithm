def solution(sides):
    answer = 0
    maxnum = max(sides)
    sumofsides = 0
    for i in sides:
        sumofsides += i
    if (maxnum < sumofsides - maxnum):
        answer = 1
    else:
        answer = 2
    return answer