def solution(n):
    answer = 0
    fac = 1
    while (fac <= n):
        answer += 1
        fac *= answer
    answer -= 1
    return answer