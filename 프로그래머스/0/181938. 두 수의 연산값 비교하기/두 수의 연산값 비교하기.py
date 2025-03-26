def solution(a, b):
    answer = 0
    ans1 = str(a) + str(b)
    ans2 = 2 * a * b
    if (int(ans1) >= ans2):
        answer = int(ans1)
    else:
        answer = ans2
    return answer