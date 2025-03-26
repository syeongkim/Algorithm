def solution(ineq, eq, n, m):
    answer = 0
    if (ineq == ">"):
        if (eq == "="):
            if (n >= m):
                answer = 1
            else:
                pass
        else:
            if (n > m):
                answer = 1
            else:
                pass
    else:
        if (eq == "="):
            if (n <= m):
                answer = 1
            else:
                pass
        else:
            if (n < m):
                answer = 1
            else:
                pass
    return answer