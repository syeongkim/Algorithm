def solution(n, lost, reserve):
    answer = n - len(lost)
    dup = set(lost) & set(reserve)
    lost.sort()
    reserve.sort()
    for j in dup:
        lost.remove(j)
        reserve.remove(j)
        answer += 1
    for i in lost:
        if (i-1 in reserve):
            reserve.remove(i-1)
            answer += 1
        elif (i+1 in reserve):
            reserve.remove(i+1)
            answer += 1

    return answer