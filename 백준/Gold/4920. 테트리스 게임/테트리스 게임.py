t = 1

while True:
    n = int(input())
    maxSum = float('-inf')
    if n == 0:
        break
        
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    blocks = [[[0, 0], [0, 1], [0, 2], [0, 3]], # 1번 블록
              [[0, 0], [1, 0], [2, 0], [3, 0]], # 1번 블록 오른쪽으로 90도 회전
              [[0, 0], [0, 1], [1, 1], [1, 2]], # 2번 블록
              [[0, 1], [1, 0], [1, 1], [2, 0]], # 2번 블록 오른쪽으로 90도 회전
              [[0, 0], [0, 1], [0, 2], [1, 2]], # 3번 블록
              [[0, 1], [1, 1], [2, 0], [2, 1]], # 3번 블록 오른쪽으로 90도 회전
              [[0, 0], [1, 0], [1, 1], [1, 2]], # 3번 블록 180도 회전
              [[0, 0], [0, 1], [1, 0], [2, 0]], # 3번 블록 왼쪽으로 90도 회전
              [[0, 0], [0, 1], [0, 2], [1, 1]], # 4번 블록
              [[0, 1], [1, 0], [1, 1], [2, 1]], # 4번 블록 오른쪽으로 90도 회전
              [[0, 1], [1, 0], [1, 1], [1, 2]], # 4번 블록 180도 회전
              [[0, 0], [1, 0], [1, 1], [2, 0]], # 4번 블록 왼쪽으로 90도 회전
              [[0, 0], [0, 1], [1, 0], [1, 1]]] # 5번 블록

    for i in range(n):
        for j in range(n):
            for block in blocks:
                numberSum = 0
                isAble = True
                for position in block:
                    row = position[0]
                    col = position[1]
                    if 0 <= i + row < n and 0 <= j + col < n:
                        numberSum += board[i + row][j + col]
                    else:
                        isAble = False
                        break
                if isAble:
                    maxSum = max(numberSum, maxSum)
                    
    print(f"{t}. {maxSum}")
    t += 1