def solution(citations):
    answer = 0
    sortedCitations = sorted(citations)
    for h in range(len(citations) + 1):
        cnt = 0
        for c in sortedCitations:
            if c >= h:
                cnt += 1
            else:
                pass
        if cnt >= h:
            answer = h
        else:
            break
    return answer