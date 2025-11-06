function solution(board) {
    var answer = 0;
    dx = [-1, 0, 1, 0, -1, -1, 1, 1, 0]
    dy = [0, -1, 0, 1, -1, 1, -1, 1, 0]
    newBoard = []
    var row = board.length
    var col = board[0].length
    
    for (i = 0; i < row; i++) {
        var temp = []
        for (j = 0; j < col; j++) {
            temp.push(0)
        }
        newBoard.push(temp)
    }
    
    for (r = 0; r < row; r++) {
        for (c = 0; c < col; c++) {
            if (board[r][c] == 1) {
                for (i = 0; i < 9; i++) {
                    if (r + dx[i] >= 0 && r + dx[i] < row) {
                        if (c + dy[i] >= 0 && c + dy[i] < col) {
                            newBoard[r + dx[i]][c + dy[i]] = 1;
                        }
                    }
                }
            }
        }
    }
    
    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            if (newBoard[i][j] == 0) {
                answer += 1
            }
        }
    }
    
    return answer;
}