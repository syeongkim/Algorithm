import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))
    
def countCandies(candyList):
    cnt = 1
    maxCnt = 1
    prev = 'X'
    for candy in candyList:
        if candy == prev:
            cnt += 1
            if cnt > maxCnt:
                maxCnt = cnt
        else:
            prev = candy
            cnt = 1
    return maxCnt
    
def swapAndGetCandies(a, b, aValue, bValue):
    board[a[0]][a[1]] = bValue
    board[b[0]][b[1]] = aValue
    maxCandies = 0

    if a[0] == b[0]:
        maxCandies = max(maxCandies, 
                         countCandies(board[a[0]]), 
                         countCandies([board[i][a[1]] for i in range(N)]), 
                         countCandies([board[i][b[1]] for i in range(N)]))
    else:
        maxCandies = max(maxCandies, 
                     countCandies(board[a[0]]),
                     countCandies(board[b[0]]),
                     countCandies([board[i][a[1]] for i in range(N)]))

    board[a[0]][a[1]] = aValue
    board[b[0]][b[1]] = bValue
    return maxCandies

answer = 0
for i in range(N):
    answer = max(answer, countCandies(board[i]))

for i in range(N):
    answer = max(answer, countCandies([board[j][i] for j in range(N)]))
    
for i in range(N):
    for j in range(N-1):
        left = board[i][j]
        right = board[i][j+1]
        if left != right:
            answer = max(answer, swapAndGetCandies([i, j], [i, j+1], left, right))
         
for i in range(N):
    for j in range(N-1):
        up = board[j][i]
        down = board[j+1][i]
        if up != down:
            answer = max(answer, swapAndGetCandies([j, i], [j+1, i], up, down))
            
print(answer)