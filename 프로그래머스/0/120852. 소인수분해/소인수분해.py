def solution(n):
    answer = []
    cnt = 2
    while (n != 1):
        if (n % cnt == 0):
            if (cnt not in answer):
                answer.append(cnt)
            n = n / cnt
        else:
            cnt += 1
    return answer