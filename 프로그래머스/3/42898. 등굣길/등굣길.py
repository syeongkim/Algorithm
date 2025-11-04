def solution(m, n, puddles):
    answer = 0
    cnt = [[0 for _ in range(m+1)] for _ in range(n+1)]
    cnt[1][1] = 1
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            if [c, r] in puddles:
                cnt[r][c] = 0
            else:
                cnt[r][c] += cnt[r-1][c] + cnt[r][c-1]
                
    answer = cnt[n][m] % 1000000007
    return answer