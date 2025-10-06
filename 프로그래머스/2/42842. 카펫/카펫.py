def solution(brown, yellow):
    answer = []
    for a in range(1, brown + yellow + 1):
        for b in range((brown + yellow) // a + 1):
            if a * b == brown + yellow:
                if (a-2) * (b-2) == yellow:
                    answer.append(a)
                    answer.append(b)
                    answer.sort(reverse = True)
                    return answer