def solution(commands):
    answer = []
    board = [['' for _ in range(51)] for _ in range(51)]
    mergeList = [[[] for _ in range(51)] for _ in range(51)]
    for command in commands:
        commandValues = list(command.split(' '))
        operation = commandValues[0]
        if operation == 'UPDATE':
            if len(commandValues) == 4:
                r, c, value = int(commandValues[1]), int(commandValues[2]), commandValues[3]
                board[r][c] = value
                for position in mergeList[r][c]:
                    row = position[0]
                    col = position[1]
                    board[row][col] = value
            else:
                value1, value2 = commandValues[1], commandValues[2]
                for i in range(51):
                    for j in range(51):
                        if board[i][j] == value1:
                            board[i][j] = value2
            
        elif operation == 'MERGE':
            r1, c1 = int(commandValues[1]), int(commandValues[2])
            r2, c2 = int(commandValues[3]), int(commandValues[4])
            allPositions = [[r1, c1], [r2, c2]]
            for position in mergeList[r1][c1]:
                if position not in allPositions:
                    allPositions.append(position)
            for position in mergeList[r2][c2]:
                if position not in allPositions:
                    allPositions.append(position)
                    
            for position in allPositions:
                row = position[0]
                col = position[1]
                mergeList[row][col] = allPositions
            
            if board[r1][c1] == '':
                if board[r2][c2] == '':
                    pass
                else:
                    board[r1][c1] = board[r2][c2]
                    for position in mergeList[r1][c1]:
                        row = position[0]
                        col = position[1]
                        board[row][col] = board[r2][c2]
            else:
                board[r2][c2] = board[r1][c1]
                for position in mergeList[r2][c2]:
                    row = position[0]
                    col = position[1]
                    board[row][col] = board[r1][c1]
            
        elif operation == 'UNMERGE':
            r = int(commandValues[1])
            c = int(commandValues[2])
            prevValue = board[r][c]
            for position in mergeList[r][c]:
                row = position[0]
                col = position[1]
                board[row][col] = ''
                mergeList[row][col] = []
            mergeList[r][c] = []
            board[r][c] = prevValue
            
        elif operation == 'PRINT':
            r = int(commandValues[1])
            c = int(commandValues[2])
            if board[r][c] == '':
                answer.append('EMPTY')
            else:
                answer.append(board[r][c])

    return answer