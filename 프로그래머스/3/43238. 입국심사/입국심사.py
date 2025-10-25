def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            
        if cnt < n:
            start = mid + 1
        elif cnt >= n:
            answer = mid
            end = mid - 1

    return answer