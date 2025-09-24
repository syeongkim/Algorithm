from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))  # 시작점
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0 <= newR < n and 0 <= newC < m and maps[newR][newC] == 1:
                maps[newR][newC] = maps[r][c] + 1
                q.append((newR, newC))

    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]